import os
import sys

if sys.platform == "win32":
    # throw error it is not supported
    raise Exception("Windows is not supported. Only Linux supported.")

if sys.platform == "darwin":
    # throw error it is not supported
    raise Exception("MacOS is not supported. Only Linux supported.")

if sys.platform == "linux":
    os.system("sudo apt-get update")
    os.system("sudo apt-get install -y python3 python3-pip python3-venv")
    os.system("make setup")
