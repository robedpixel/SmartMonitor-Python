import threading
import os
import shutil
import platform
import subprocess
from glob import glob
from pathlib import Path


class GPhotoThread(threading.Thread):
    def __init__(self):
        self.cF = 0
        self.cFH = 0
        self.copy_point = ""
        self.stopped = False
        self.connected_camera = None

    def connect_to_camera(self, mount_point, copy_point):
        self.copy_point = copy_point
        if platform.system() == "Linux":
            import gphoto2 as gp
            cameras = gp.gp_camera_autodetect()
            if cameras[0] > 0:
                self.connected_camera = gp.Camera()
                self.connected_camera.init()
                # p = subprocess.run(["gphotofs", os.path.abspath(mount_point)])
                # if p.returncode == 0:
                print("camera filesystem mounted!")
                self.cFH = self.count_files_optimised(self.connected_camera)
                return True
        return False

    def run(self):
        while not self.stopped:
            self.cF = self.count_files_optimised(self.connected_camera)
            if self.cF != self.cFH:
                # TODO: try to convert to using gphoto2 --get-files if possible
                print("New files have been taken")
                if self.cF > self.cFH:
                    # uM = subprocess.Popen(['fusermount', "-u", os.path.abspath(mount_point)])
                    # m = subprocess.Popen(['gphotofs', os.path.abspath(mount_point)])
                    # result = [y for x in os.walk(os.path.abspath(mount_point)) for y in glob(os.path.join(x[0], '*.JPG'))]
                    raw_result = self.list_files(self.connected_camera)
                    result = list()
                    for id, row in enumerate(raw_result):
                        if row.endswith(".JPG"):
                            list.append((row, id))
                    latest_file = max(result, key=lambda item: self.get_file_time(item[0]))
                    print(latest_file)
                    # get file from latest_file[1] id
                    connect = subprocess.Popen(
                        ['gphoto2', '--filename', self.copy_point + "/temp.JPG", '--get-file', latest_file[1]],
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    # shutil.copy(latest_file, self.copy_point + "/" + Path(latest_file).name)
                self.cFH = self.cF
        print("unmounting camera...")
        self.connected_camera.exit()
        # p = subprocess.run(["fusermount", "-u", os.path.abspath(mount_point)])
        # if p.returncode == 0:
        print("camera filesystem unmounted!")

    def stop(self):
        self.stopped = True

    def openConnect(self):
        cExist = 0
        connect = subprocess.Popen(['gphoto2', '--auto-detect'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        connect = connect.stdout.read()
        connect = string.split(connect, '\n')
        for x in connect:
            if ('usb' in x):
                cExist += 1
                return cExist

    def countFiles(self):
        fcount = 0
        files = subprocess.Popen(['gphoto2', '-L'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        files = files.stdout.read()
        files = string.split(files, '\n')
        for x in files:
            if '#' in x:
                fcount += 1
        print("fcount: " + str(fcount))
        return fcount

    def list_files(self, camera, path='/'):
        result = []
        # get files
        for name, value in camera.folder_list_files(path):
            result.append(os.path.join(path, name))
        # read folders
        folders = []
        for name, value in camera.folder_list_folders(path):
            folders.append(name)
        # recurse over subfolders
        for name in folders:
            result.extend(self.list_files(camera, os.path.join(path, name)))
        return result

    def get_file_info(self, camera, path):
        folder, name = os.path.split(path)
        return camera.file_get_info(folder, name)

    def get_file_time(self, path):
        info = self.get_file_info(self.connected_camera, path)
        return info.file.mtime

    def count_files_optimised(self, camera):
        return len(self.list_files(camera))
