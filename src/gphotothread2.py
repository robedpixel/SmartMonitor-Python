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


class GPhotoThread2(threading.Thread):
    def __init__(self):
        super(GPhotoThread2, self).__init__()
        self.cF = 0
        self.cFH = 0
        self.copy_point = ""
        self.stopped = False
        self.connected_camera = None
        self.detector = None
        self.camera_is_connected = False

    def mount_camera(self):
        cameras = gp.gp_camera_autodetect()
        if cameras[0] > 0:
            self.connected_camera = gp.Camera()
            self.connected_camera.init()
            # p = subprocess.run(["gphotofs", os.path.abspath(mount_point)])
            # if p.returncode == 0:
            print("camera filesystem mounted!")
            self.cFH = self.count_files_optimised(self.connected_camera)
            self.camera_is_connected = True
            return True
        else:
            self.camera_is_connected = False
            return False
    
    def initialize(self, mount_point, copy_point):
        self.copy_point = copy_point
        if platform.system() == "Linux":
            # start hotplug detector
            self.mount_camera()
            return True
        return False

    def connect_to_camera(self, mount_point, copy_point):
        self.initialize(mount_point, copy_point)
    
    def get_updated_camera(self):
        if self.camera_is_connected:
            #add try catch block for camera
            if gp.check_result(self.connected_camera.exit()):
                self.connected_camera = gp.Camera()
                self.connected_camera.init()
            else:
                # Camera Disconnected, reset cFH
                self.cFH = 0
                self.mount_camera()
        else:
            self.mount_camera()

    def run(self):
        while not self.stopped:
            self.get_updated_camera()
            if self.camera_is_connected:
                self.cF = self.count_files_optimised(self.connected_camera)
                if self.cF != self.cFH:
                    print("New files have been taken")
                    if self.cF > self.cFH:
                        raw_result = self.list_files(self.connected_camera)
                        result = list()
                        for row in raw_result:
                            if row.endswith(".JPG"):
                                result.append(row)
                        latest_file = max(result, key=lambda item: self.get_file_time(item))
                        # get file from latest_file
                        folder, name = os.path.split(latest_file)
                        camera_file = gp.check_result(
                            gp.gp_camera_file_get(self.connected_camera, folder, name, gp.GP_FILE_TYPE_NORMAL))
                        gp.check_result(gp.gp_file_save(camera_file, self.copy_point + "/"+name))
                        camera_file = gp.check_result(
                            gp.gp_camera_file_get(self.connected_camera, folder, name.rsplit('.',1)[0] + ".NEF", gp.GP_FILE_TYPE_NORMAL))
                        gp.check_result(gp.gp_file_save(camera_file, self.copy_point + "/" + name.rsplit('.',1)[0] + ".NEF"))
                    self.cFH = self.cF
        if self.camera_is_connected:
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
