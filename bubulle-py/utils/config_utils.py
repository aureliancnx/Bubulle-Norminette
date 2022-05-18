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
import json
import os
import subprocess

config = None
forbidden_paths = None


def open_config_file():
    print("Opening Bubulle configuration file.")
    print(
        "\033[0;31mWARNING: This is experimental. A mistake can lead Bubulle to not work properly.\033[0;0m"
    )
    # Linux cases
    if "EDITOR" in os.environ:
        os.system(f"{os.getenv('EDITOR')} {get_config_path()}")
    else:
        # macOS case
        subprocess.call(["open", get_config_path()])


def get_config_path():
    return f"{os.path.dirname(os.path.realpath(__file__))}/../../config.json"


def load_config():
    global config
    try:
        with open(get_config_path(), "r") as file:
            content = file.read()
            config = json.loads(content)
        load_sub()
    except Exception as ex:
        print(ex)
        print("Unable to load Bubulle config file.")
        exit(1)


def load_sub():
    load_forbidden_paths()


def load_forbidden_paths():
    global forbidden_paths
    forbidden_paths = config["excluded_paths"]
    try:
        raw = os.popen("git check-ignore $(find . -type f -print) | cut -c3-").read()
        raw = raw.split("\n")
        if forbidden_paths is None:
            forbidden_paths = []
        for r in raw:
            forbidden_paths.append(r)
        if "" in forbidden_paths:
            forbidden_paths.remove("")

    except Exception as e:
        print(e)
