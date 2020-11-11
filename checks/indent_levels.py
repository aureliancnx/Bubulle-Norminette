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

from checks._check import AbstractCheck
from utils.error_handling import BuErrors

matches = ["if\s*\(((?!\s).+)\)", "while\s*\(((?!\s).+)\)", "for\s*\(((?!\s).+)\)"]

class IndentLevels(AbstractCheck):

    def __init__(self, file_name, path, header_lines):
        self.message = "Wrong indentation level"
        self.file_name = file_name
        self.path = path
        self.header_lines = header_lines

    def get_check_id(self):
        return "L2"

    def get_check_level(self):
        return 1

    def check_line(self, line, line_number):
        return 0

    def check_function_calls(self, func):
        return 0

    def check_function_decl(self, visitor, func):
        return 0

    def check_variable_decl(self, var):
        return 0

    def check_visitor(self, visitor, lines):
        return 0

    def check_inner(self, file_content, file_contentf):
        lines = file_contentf.split('\n')
        i = 0
        index = 0
        new_ind = 0
        last_dc = 0
        last = ''

        for line in lines:
            i += 1
            new_ind = 0
            dc = 0
            tmp_enclosing = 0

            if re.match(r'[ \t]*}[ \t]*', line) and '{' in line:
                tmp_enclosing = 1
            elif '{' in line:
                index += 1
                new_ind = 1
            elif re.match(r'[ \t]*}[ \t]*', line):
                index -= 1
                if index <= 0:
                    index = 0

            if index > 0 and not len(line) <= 0:
                spaces_diff = len(line) - len(line.lstrip())
                self.line = i + self.header_lines
                if not new_ind:
                    for match in matches:
                        if len(re.findall(match, line)) > 0 and not '{' in line:
                            last_dc = 2 if len(re.findall(match, last)) > 0 else last_dc + 2
                if last_dc <= 1:
                    ind_t = index
                    if last_dc == 1:
                        ind_t += 1
                    tmp_indx = 4 * (ind_t - new_ind - tmp_enclosing)
                    if spaces_diff != tmp_indx:
                        BuErrors.print_error(self.path, self.file_name, self.line, self.get_check_level(),
                                             self.get_check_id(), self.message)
                    if index >= 4:
                        BuErrors.print_error(self.path, self.file_name, self.line, 1,
                                             "C1", "3 or more conditionnal blocks.")

            if last_dc > 0:
                last_dc -= 1
            last = line
        return 0