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
import time

from args_handler import handle_args, parse_args, set_time_start
from report_generator import Report
from utils import file_utils, error_handling, version_utils
from utils.config_utils import init_config

args = None

if __name__ == '__main__':
    set_time_start(time.time())
    args = parse_args()
    handle_args(args)
    init_config()

    # Path & args
    error_handling.args = args
    path = file_utils.get_path(args)

    # Worker init
    #workers.init_workers()

    # Make a report
    report = Report(path)
    #workers.wait()