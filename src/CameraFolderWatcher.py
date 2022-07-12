from PySide2 import QtCore


# This object monitors the airnef directory to automatically load images taken by nikon camera
class CameraFolderWatcher:
    def __init__(self):
        self.folder_watcher = QtCore.QFileSystemWatcher()
        self.callback_list = list()
        self.activated = False

    def monitor_directory(self, folder_url: str):
        self.folder_watcher.addPath(folder_url)
        if not self.activated:
            self.folder_watcher.directoryChanged.connect(self._on_folder_changed_event)
            self.activated = True

    # Callback function takes in 1 argument, which is the file url of the new camera picture
    def register_callback(self, callback_function):
        self.callback_list.append(callback_function)

    def deregister_callback(self, callback_function):
        try:
            self.callback_list.remove(callback_function)
        except IndexError:
            print("unregistered callback is not deregisterable")
        except:
            print("error deregistering callback")

    def _on_folder_changed_event(self, folder_changed_url: str):
        for object in self.callback_list:
            object(folder_changed_url)
