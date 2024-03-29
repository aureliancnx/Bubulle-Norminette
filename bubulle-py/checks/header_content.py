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

from pycparser.c_ast import Decl, Struct

from checks._check import Check
from utils.error_handling import BuErrors


class HeaderContent(Check):
    def __init__(self, file_name, path, header_lines):
        self.message = self.get_config()["message"]
        self.file_name = file_name
        self.path = path
        self.header_lines = header_lines

    def is_header_file(self):
        return self.file_name.endswith(".h")

    def check_ast(self, ast):
        # Check for structures in source file
        if not self.is_header_file():
            for dcl in ast:
                if not isinstance(dcl, Decl) or not hasattr(dcl, "type"):
                    continue
                if not isinstance(dcl.type, Struct):
                    continue
                self.message = self.get_config()["source_struct"]
                BuErrors.print_error(
                    self.path,
                    self.file_name,
                    -1,
                    self.get_check_level(),
                    self.get_check_id(),
                    self.message,
                )
        return 0

    def check_line(self, line, line_number):
        # If a #define is present in the source file
        if not self.is_header_file() and re.match(
            self.get_config()["macro_regex"], line
        ):
            self.message = self.get_config()["source_define"]
            return 1

    def check_function_decl(self, visitor, func):
        # Check function declaration in header file
        if self.is_header_file():
            self.line = func.decl.coord.line + (1 if self.header_lines != 0 else 0)
            self.message = self.get_config()["header_func_dcl"]
            return 1
        return 0
