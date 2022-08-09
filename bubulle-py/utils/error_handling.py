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
import re

import args_handler
from .string_utils import Colors

errors = []
args = None


class BuError:
    """Class to handle errors."""

    def __init__(self, path, file_name, error_id, level, line, message):
        self.path = path
        self.file_name = file_name
        self.error_id = error_id
        self.level = level
        self.line = line
        self.message = message

    def print_error(self):
        try:
            highlight = "\33[44m "
            if self.level == 1:
                highlight = "\33[0;30;43m "
            elif self.level == 2:
                highlight = "\x1b[0;30;41m "

            line_st = ""
            if not isinstance(self.file_name, str):
                self.file_name = self.file_name[0]
            if len(self.file_name) > 19:
                self.file_name = f"{self.file_name[:15]}..."
            level_st = ""
            err_spaces = 22 - len(self.file_name)
            shown_err = ""
            for _ in range(1, err_spaces):
                shown_err = f"{shown_err} "
            shown_err = shown_err + str(self.error_id)
            line_spaces = 9 - len(self.error_id)
            if self.line != -1:
                line_st = line_st + highlight + str(self.line)
            level_spaces = 7 - len(str(self.line))
            for _ in range(1, level_spaces):
                level_st = f" {level_st}"
            if self.line == -1:
                line_st += "   "

            if self.level == 0:
                level_st = level_st + "\33[44m INFO " + Colors.ENDC
            elif self.level == 1:
                level_st = level_st + "\33[0;30;43m MINOR " + Colors.ENDC
            else:
                level_st = level_st + "\x1b[0;30;41m MAJOR " + Colors.ENDC
            for _ in range(1, line_spaces):
                line_st = f" {line_st}"
            level_space = 8 if self.level == 0 else 7
            details_spaces = level_space - len(line_st)
            details_spaces = max(details_spaces, 0)
            details_spaces += 6 if self.level == 0 else 5
            color = "\033[37m" if len(errors) % 2 == 1 else "\033[0m"
            message = color + self.message
            details_st = message
            for _ in range(1, details_spaces):
                details_st = f" {details_st}"
            line_st = line_st + " \033[0m"
            print(
                f"{color + self.file_name}{color + shown_err}{color + line_st}{level_st}{details_st}"
            )

        except Exception as e:
            print(e)


class BuErrors:
    @staticmethod
    def split_on_empty_lines(string):
        blank_line_regex = r"(?:\r?\n){2,}"
        return re.split(blank_line_regex, string.strip())

    @staticmethod
    def print_error(string, file_name, line, level, errid, message):
        if not can_print_error(level, errid):
            return

        error = BuError(string, file_name, errid, level, line, message)
        errors.append(error)
        error.print_error()


def can_print_error(level, errid):
    if errid.lower() in args_handler.ignored_tests:
        return 0
    if level == 0 and args.ignore_info:
        return 0
    if level == 1 and args.ignore_minor:
        return 0
    if level == 2 and args.ignore_major:
        return 0
    return 1
