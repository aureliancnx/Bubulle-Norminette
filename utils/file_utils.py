import os
import urllib.request

version = -1
version_url = "https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/VERSION"

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
    version = read('VERSION')
    return version

def read(name):
    f = open(name, 'r')
    return f.read()

def get_path(args):
    path = args.p

    if path == '.':
        path = os.getcwd()
    return path

def is_tempfile(path):
    if path.endswith(".tmp"):
        try:
            os.remove(path)
        except:
            pass
        return 1
    return 0