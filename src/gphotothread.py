import threading
import os
import shutil
import platform
import subprocess
from datetime import datetime
from glob import glob
from pathlib import Path

if platform.system() == "Linux":
    import gphoto2 as gp


class GPhotoThread(threading.Thread):
    def __init__(self):
        super(GPhotoThread, self).__init__()
        self.cF = 0
        self.cFH = 0
        self.copy_point = ""
        self.stopped = False
        self.connected_camera = None

    def connect_to_camera(self, mount_point, copy_point):
        self.copy_point = copy_point
        if platform.system() == "Linux":
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

    def get_updated_camera(self):
        self.connected_camera.exit()
        self.connected_camera = gp.Camera()
        self.connected_camera.init()

    def run(self):
        while not self.stopped:
            self.get_updated_camera()
            self.cF = self.count_files_optimised(self.connected_camera)
            if self.cF != self.cFH:
                # TODO: try to convert to using gphoto2 --get-files if possible
                print("New files have been taken")
                if self.cF > self.cFH:
                    raw_result = self.list_files(self.connected_camera)
                    result = list()
                    for id, row in enumerate(raw_result):
                        if row.endswith(".JPG"):
                            result.append(row)
                    latest_file = max(result, key=lambda item: self.get_file_time(item))
                    # get file from latest_file
                    if os.path.exists(self.copy_point + "/temp.JPG"):
                        os.remove(self.copy_point + "/temp.JPG")
                    folder, name = os.path.split(latest_file)
                    camera_file = gp.check_result(
                        gp.gp_camera_file_get(self.connected_camera, folder, name, gp.GP_FILE_TYPE_NORMAL))
                    gp.check_result(gp.gp_file_save(camera_file, self.copy_point + "/temp.JPG"))
                self.cFH = self.cF
        print("unmounting camera...")
        self.connected_camera.exit()
        print("camera filesystem unmounted!")

    def stop(self):
        self.stopped = True

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
        return datetime.fromtimestamp(info.file.mtime)

    def count_files_optimised(self, camera):
        return len(self.list_files(camera))
