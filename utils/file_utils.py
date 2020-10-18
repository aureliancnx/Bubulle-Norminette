import os

version = -1

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