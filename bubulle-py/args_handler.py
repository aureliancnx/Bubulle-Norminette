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
import argparse

from utils import version_utils
from utils.config_utils import open_config_file

ignored_tests = []
time_start = 0


def set_time_start(time):
    global time_start
    time_start = time


def parse_args():
    # Parse args
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--p", default=".",
                        help="path to the desired folder")
    parser.add_argument("-e", "--exclude", default=None,
                        help="exclude a path from being checked")
    parser.add_argument("-f", "--no-forbidden", default=None,
                        help="exclude forbidden function checks")
    parser.add_argument("-a", "--aggressive", action='store_true',
                        help="enable aggressive mode for more advanced tests")
    parser.add_argument("-ic", "--ignore-compilation", help="ignore compilation errors",
                        action='store_true')
    parser.add_argument("-r", "--report", help="generate and open a report",
                        action='store_true')
    parser.add_argument("-c", "--config", help="edit the configuration of Bubulle (experimental)",
                        action='store_true')
    parser.add_argument("-i", "--ignore", help="ignore specific tests. (e.g: -i l2,f5)",
                        default="")
    parser.add_argument("-ii", "--ignore-info", help="ignore all info tests",
                        action='store_true')
    parser.add_argument("-imin", "--ignore-minor", help="ignore all minor tests",
                        action='store_true')
    parser.add_argument("-imaj", "--ignore-major", help="ignore all major tests",
                        action='store_true')
    parser.add_argument("-v", "--version", help="version information",
                        action='store_true')
    parser.add_argument("-verbose", "--verbose", help="verbose information",
                        action='store_true')
    parser.add_argument("-u", "--update", action='store_true')
    return parser.parse_args()


def handle_ignored_tests(args):
    global ignored_tests
    if args.ignore == '':
        return
    ignored_tests = args.ignore.split(',')
    ignored_tests = [x.lower() for x in ignored_tests]


def handle_update(args):
    # Update
    if args.update:
        version_utils.update()
        exit(0)

    if args.version:
        version_utils.check_version(show_version=True)
        exit(0)


def handle_config(args):
    if args.config:
        open_config_file()
        exit(0)


def handle_args(args):
    handle_update(args)
    handle_ignored_tests(args)
    handle_config(args)
