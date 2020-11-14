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

v = None

class FunctionTooLong(AbstractCheck):

    def __init__(self, file_name, path, header_lines):
        self.message = self.get_config()['message']
        self.file_name = file_name
        self.path = path
        self.header_lines = header_lines
        self.v = None

    def check_function_decl(self, visitor, func):
        return 0

    def check_line(self, line, line_number):
        return 0

    def check_function_calls(self, func):
        return 0

    def check_variable_decl(self, var):
        return 0

    def check_visitor(self, visitor, lines):
        global v
        v = visitor
        return 0

    def check_inner(self, file_content, file_contentf):
        global v
        last_func = ''
        i = 0
        index = 0
        line_start = -1
        lines = file_contentf.split('\n')

        for line in lines:
            i += 1
            if v is not None and i in v.function_defs:
                last_func = v.function_defs[i]

            started_newindent = 0
            if '{' in line:
                started_newindent = 1
                if index == 0:
                    line_start = i
                index += 1
                if i - 1 >= 0 and v is not None and i - 1 in v.function_defs:
                    last_func = v.function_defs[i - 1]
            elif re.match(r'[ \t]*}[ \t]*', line):
                started_newindent = 0
                index -= 1
                if index <= 0:
                    index = 0
                    if line_start > 0 and i - line_start - 2 > self.get_config()['max_lines_per_function']:
                        BuErrors.print_error(self.path, self.file_name, line_start + self.header_lines,
                                             self.get_check_level(), self.get_check_id(),
                                             self.get_config()['message'].format(last_func, (i - line_start - 2)))
                    line_start = -1
                    last_func = ''
            else:
                started_newindent = 0