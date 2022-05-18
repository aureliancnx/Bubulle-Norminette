#
# Copyright (c) 2020 aureliancnx
#
# MIT LICENSE
#
# This project is part of aureliancnx.
# See https://github.com/aureliancnx/Bubulle-Norminette for further info.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.#
import os
import time
import urllib.request

import args_handler
from . import file_utils

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

    path = f'{os.path.dirname(os.path.realpath(__file__))}/../../VERSION'
    version = file_utils.read(path)
    return version


def check_version(show_version=False):
    time_end = time.time() - args_handler.time_start
    if show_version:
        print("Version: \033[36m{0}".format(get_version()))
    if get_version_latest() != get_version():
        print("\033[91mBubulle is out to date. Please update by typing the following command: bubulle -u\033[0m")
        return
    print("\033[0mBubulle is up to date. Executed in %.2fs" % time_end)


def update():
    os.system(update_cmd)
    exit(0)
