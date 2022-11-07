import threading
import os
import shutil
import platform
import subprocess
from glob import glob

class GPhotoThread(threading.Thread):
    def __init__(self):
        self.cFH = 0
        self.copy_point = ""
        self.stopped = False

    def connect_to_camera(self, mount_point, copy_point):
        self.copy_point = copy_point
        if platform.system() == "Linux":
            import gphoto2 as gp
            cameras = gp.gp_camera_autodetect()
            if cameras[0] > 0:
                p = subprocess.run(["gphotofs", os.path.abspath(mount_point)])
                if p.returncode == 0:
                    print("camera filesystem mounted!")
                    self.cFH = self.countFiles()
                    return True
        return False

    def run(self):
        while not self.stopped:
            self.cF = self.countFiles()
            if self.cF != self.cFH:
                #TODO: try to convert to using gphoto2 --get-files if possible
                print("New files have been taken")
                uM = subprocess.Popen(['fusermount', "-u", os.path.abspath(mount_point)])
                m = subprocess.Popen(['gphotofs', os.path.abspath(mount_point)])
                result = [y for x in os.walk(os.path.abspath(mount_point)) for y in glob(os.path.join(x[0], '*.JPG'))]
                latest_file = max(result, key=os.path.getctime)
                shutil.copy(latest_file, self.copy_point+"/"+latest_file.name())
                self.cFH = self.cF
        print("unmounting camera...")
        p = subprocess.run(["fusermount", "-u", os.path.abspath(mount_point)])
        if p.returncode == 0:
            print("camera filesystem unmounted!")
            self.camera_mounted = False

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