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
import os.path
import traceback
from os import path

from html_report.html_report import HtmlReport
from run_check import RunCheck
from utils import file_utils, string_utils, c_utils, error_handling, version_utils, config_utils


class Report:
    def __init__(self, path):
        self.path = path
        self.check_path()
        c_utils.generate_includes(
            self.path,
            f'{os.path.dirname(os.path.realpath(__file__))}/fake_libc_include',
        )

        self.generate_report()

    def check_path(self):
        if not path.exists(self.path):
            print("Unknown path '{0}'.".format(self.path))
            exit(0)

    def get_severity_col(self, n):
        if n > 5:
            return "\033[31m" + str(n) + "\033[0m"
        if n >= 3:
            return "\033[33m" + str(n) + "\033[0m"
        if n > 1:
            return "\033[93m" + str(n) + "\033[0m"
        return "\033[32m" + str(n) + "\033[0m"

    def check_norme_dir(self, subdir):
        for sub in subdir:
            if string_utils.to_snake(sub) != sub and sub.endswith('.c'):
                error_handling.BuErrors.print_error(subdir, subdir, -1, 2, "O4", "File name not in snake_case")
                return 0

    def generate_report_header(self):
        version = version_utils.get_version()
        print("\033[0m-------------------------------------------------------------------------------")
        print("\033[1;34;40m                          \033[93mBubulle Code Norme Report v{0}".format(version))
        print("\033[0mPath: \033[93m{0}".format(self.path))
        print("\033[0m-------------------------------------------------------------------------------")
        print("\033[1;34;40mFile                 Error   Line    Severity   Details")

        print("\033[0m-------------------------------------------------------------------------------\033[1;34;00m")

    def generate_report_summary(self):
        # workers.wait()
        style_err = self.summary_errors()
        print("\033[0m-------------------------------------------------------------------------------")
        print("\033[1;34;40mTOTAL\033[0m          Major: {0}       Minor: {1}       Info: {2}      Note: {3}".
              format(self.get_severity_col(style_err[2]), self.get_severity_col(style_err[1]),
                     self.get_severity_col(style_err[0]), style_err[3]))
        print("\033[0m-------------------------------------------------------------------------------")
        version_utils.check_version()
        if error_handling.args.report:
            HtmlReport(style_err)
        if style_err[1] > 0 or style_err[2] > 0:
            exit(1)
            return
        exit(0)

    def run_checks(self):
        checked_paths = []
        if path.isfile(self.path):
            try:
                run_check = RunCheck(self.path, self.path)
                run_check.run()
            except Exception as e:
                print("\033[31m{0}: Unable to run all tests. -verbose for more info.\033[0m".format(self.path))
                if error_handling.args.verbose:
                    traceback.print_exc()
                    print(e)
                return

        for pw, sub_dirs, files in os.walk(self.path):
            for name in files:
                complete_path = f'{pw}/{name}'
                relative = (
                    complete_path.replace("//", "/")
                    .replace(f"{os.path.abspath(os.getcwd())}/", "")
                    .replace(os.path.abspath(os.getcwd()), "")
                    .replace(self.path, "")
                )

                c = False
                for excluded_path in config_utils.forbidden_paths:
                    if relative.startswith(excluded_path):
                        c = True
                if c:
                    continue
                if error_handling.args.exclude is not None and relative.startswith(error_handling.args.exclude):
                    continue
                self.check_norme_dir(sub_dirs)
                if file_utils.is_temp_file(complete_path) or complete_path in checked_paths:
                    continue
                checked_paths.append(complete_path)
                try:
                    run_check = RunCheck(name, complete_path)
                    run_check.run()
                except Exception as e:
                    traceback.print_exc()
                    print(e)
                    continue

    def summary_errors(self):
        style_err = [0, 0, 0, 0]

        for error in error_handling.errors:
            style_err[error.level] += 1
            style_err[3] -= 3 if error.level == 2 else (1 if error.level > 0 else 0)
        return style_err

    def generate_report(self):
        self.generate_report_header()
        self.run_checks()
        self.generate_report_summary()
