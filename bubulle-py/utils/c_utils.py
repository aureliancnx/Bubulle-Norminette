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

from utils import config_utils, error_handling

includes = []


def generate_includes(path, fake_lib_c):
    global includes
    includes.append(f"-I{fake_lib_c}")

    for pw, sub_dirs, files in os.walk(path):
        for name in files:
            complete_path = f"{pw}/{name}"
            relative = (
                complete_path.replace("//", "/")
                .replace(f"{os.path.abspath(os.getcwd())}/", "")
                .replace(os.path.abspath(os.getcwd()), "")
            )

            c = False
            for excluded_path in config_utils.forbidden_paths:
                if relative.startswith(excluded_path):
                    c = True
            if c:
                continue

            if error_handling.args.exclude is not None and relative.startswith(
                error_handling.args.exclude
            ):
                continue

            if not name.endswith(".h"):
                continue

            relative = pw.replace(f"{os.path.abspath(os.getcwd())}/", "")
            if f"-I{relative}" in includes:
                continue

            includes.append(f"-I{relative}")
