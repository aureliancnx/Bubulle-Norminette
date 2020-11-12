import os

from utils import config_utils, error_handling

includes = []


def generate_includes(path, fakelibc):
    global includes
    includes.append('-I' + fakelibc)
    h_files = []
    for pw, subdirs, files in os.walk(path):
        for name in files:
            complete_path = pw + '/' + name
            relative = complete_path.replace("//", "/") \
                .replace(os.path.abspath(os.getcwd()) + "/", "") \
                .replace(os.path.abspath(os.getcwd()), "")
            c = False
            for excluded_path in config_utils.forbidden_paths:
                if relative.startswith(excluded_path):
                    c = True
            if c:
                continue
            if error_handling.args.exclude is not None and relative.startswith((error_handling.args.exclude)):
                continue
            if not name.endswith(".h"):
                continue
            relative = pw.replace(os.path.abspath(os.getcwd()) + "/", "")
            if '-I' + relative in includes:
                continue
            includes.append('-I' + relative)