import os
import traceback

from run_check import RunCheck
from utils import file_utils, string_utils, error_handling, version_utils


class Report():
    def __init__(self, path):
        self.path = path
        self.generate_report()

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
            if string_utils.tosnake(sub) != sub:
                error_handling.BuErrors.print_error(subdir, -1, 2, "O4", "File name not in snake_case")
                return 0

            # print(func.body)

    def generate_report_header(self):
        version = version_utils.get_version()
        print("\033[0m-------------------------------------------------------------------------------")
        print("\033[1;34;40m                          \033[93mBubulle Code Norme Report v{0}".format(version))
        print("\033[0mDirectory: \033[93m{0}".format(self.path))
        print("\033[0m-------------------------------------------------------------------------------")
        print("\033[1;34;40mFile                 Error   Line    Severity   Details")

        print("\033[0m-------------------------------------------------------------------------------\033[1;34;00m")

    def generate_report_summary(self):
        style_err = self.summary_errors()
        print("\033[0m-------------------------------------------------------------------------------")
        print("\033[1;34;40mTOTAL\033[0m          Major: {0}       Minor: {1}       Info: {2}      Note: {3}".
              format(self.get_severity_col(style_err[2]), self.get_severity_col(style_err[1]),
                     self.get_severity_col(style_err[0]), style_err[3]))
        print("\033[0m-------------------------------------------------------------------------------")
        version_utils.check_version()

    def run_checks(self):
        checked_paths = []
        for pw, subdirs, files in os.walk(self.path):
            for name in files:
                self.check_norme_dir(subdirs)
                complete_path = pw + '/' + name
                if '.git' in complete_path:
                    continue
                if file_utils.is_tempfile(complete_path):
                    continue
                if complete_path in checked_paths:
                    continue
                checked_paths.append(complete_path)
                try:
                    runcheck = RunCheck(name, complete_path)
                    runcheck.run()
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