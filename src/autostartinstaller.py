import platform
import subprocess

#TODO: NOT COMPLETE

executable="./runprogram.sh"

def is_root():
    return os.geteuid() == 0

if __name__ == "__main__":
    quit()
    print("Installing autostart functionality for SmartMonitor on Raspbian")
    print("Checking if operating system is compatible:")
    if platform != "linux":
        print("Error! Installation only works on linux")
        input("Press Enter to continue...")
        quit()
    print("Success")
    print("checking for root access:")
    if not is_root():
        print("Error! Installation requires root access")
        input("Press Enter to continue...")
        quit()
    print("Success")
    print("Finding runprogram.sh")
    if not os.path.isfile(executable):
        print("Error! File not found")
        input("Press Enter to continue...")
        quit()
    print("Success")
    print("setting permissions")
    command = "chown root " + executable
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    process.wait()
    if process.returncode != 0:
        print("Error! Could not set ownership of file")
        input("Press Enter to continue...")
        quit()
    command = "chmod a+s " + executable
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    process.wait()
    if process.returncode != 0:
        print("Error! Could not set access properties of file")
        input("Press Enter to continue...")
        quit()
    executable_abs = os.path.abspath(executable)
    #TODO: get template of .desktop file and replace with absolute path to runprogram.sh
