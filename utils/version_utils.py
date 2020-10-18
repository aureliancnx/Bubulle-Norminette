import os
import urllib.request

from utils import file_utils

version = -1
version_url = "https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/VERSION"
update_cmd = "sudo sh -c \"$(curl -fsSL https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/install_bubulle.sh)\""

def get_version_latest():
    try:
        w = urllib.request.urlopen(version_url, timeout=1)
        data = w.read()
        return data.decode("utf-8")
    except Exception as e:
        return get_version()


def get_version():
    global version
    if version != -1:
        return version

    path = os.path.dirname(os.path.realpath(__file__)) + '/../VERSION'
    version = file_utils.read(path)
    return version

def check_version():
    if get_version_latest() != get_version():
        print("\033[91mBubulle is out to date. Please update by typing the following command: bubulle -u\033[0m")
        return
    print("\033[0mBubulle is up to date.")

def update():
    os.system(update_cmd)
    exit(0)