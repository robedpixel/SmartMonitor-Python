from PySide2 import QtCore


# This object monitors the airnef directory to automatically load images taken by nikon camera
class CameraFolderWatcher:
    def __init__(self):
        self.folder_watcher = QtCore.QFileSystemWatcher()
        self.callback_list = list()
        self.activated = False
        self.monitored_directory = None

    def monitor_directory(self, folder_url: str):
        if not self.activated:
            self.folder_watcher.addPath(folder_url)
            self.monitored_directory = folder_url
            self.folder_watcher.directoryChanged.connect(self._on_folder_changed_event)
            self.activated = True
        else:
            self.folder_watcher.removePath(self.monitored_directory)
            self.folder_watcher.addPath(folder_url)
            self.monitored_directory = folder_url

    def shutdown(self):
        if self.activated:
            self.folder_watcher.removePath(self.monitored_directory)
            self.callback_list.clear()
            self.folder_watcher.directoryChanged.disconnect()
            self.activated = False

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
