import os
import platform

def shutdown():
    current_os = platform.system().lower()
    if "windows" in current_os:
        os.system("shutdown /s /t 1")
    elif "linux" in current_os:
        os.system("sudo shutdown now")
    elif "darwin" in current_os:  # 'darwin' is the system name for macOS
        os.system("sudo shutdown -h now")
    else:
        print("Unsupported operating system")

if __name__ == "__main__":
    shutdown()

