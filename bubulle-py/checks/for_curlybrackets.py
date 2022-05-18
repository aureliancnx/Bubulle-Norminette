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

from pycparser.c_ast import For

from checks._check import AbstractCheck
from utils.error_handling import BuErrors


class ForCurlybrackets(AbstractCheck):

    tc = None

    def __init__(self, file_name, path, header_lines):
        self.message = self.get_config()['message']
        self.file_name = file_name
        self.path = path
        self.header_lines = header_lines

    def check_ast(self, ast):
        return 0

    def curly_process(self, dt):
        if not re.search(r'for\s*\(((?!\s).+)\)', tc[dt.coord.line - 1]):
            return 0
        if re.search(r'for\s*\(((?!\s*\{).+)\)\s*{', tc[dt.coord.line - 1]):
            return 0
        if re.search(r'for\s*\(((?!\s*\{).+)\)\s*;', tc[dt.coord.line - 1]):
            return 0
        if not tc[dt.coord.line].strip().startswith('{'):
            return 0
        self.line = dt.coord.line + self.header_lines + (1 if self.header_lines != 0 else 0)
        BuErrors.print_error(self.path, self.file_name, self.line, self.get_check_level(),
                             self.get_check_id(), self.message)

    def check_function_decl(self, visitor, func):
        if func.body.block_items is None:
            return 0
        if tc is None:
            return 0
        # TODO: recursive check
        for it in func.body.block_items:
            if not isinstance(it, For):
                continue
            self.curly_process(it)
        return 0

    def check_line(self, line, line_number):
        return 0

    def check_function_calls(self, func):
        return 0

    def check_variable_decl(self, var):
        return 0

    def check_visitor(self, visitor, lines):
        return 0

    def check_inner(self, file_content, file_contentf):
        global tc
        lines = file_contentf.split('\n')
        tc = lines
        return 0
