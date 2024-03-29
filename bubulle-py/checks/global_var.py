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
from pycparser.c_ast import TypeDecl, Decl, PtrDecl

from checks._check import Check
from utils.error_handling import BuErrors

allw = [PtrDecl, TypeDecl]


class GlobalVariable(Check):
    def __init__(self, file_name, path, header_lines):
        self.message = self.get_config()["message"]
        self.file_name = file_name
        self.path = path
        self.header_lines = header_lines

    def check_variable_decl(self, var):
        return 0

    def check_ast(self, ast):
        for p in ast:
            if not isinstance(p, Decl) or not hasattr(p, "quals"):
                continue
            if not hasattr(p, "type") or "const" in p.quals:
                continue
            btype = any(isinstance(p.type, altype) for altype in allw)
            if not btype:
                continue
            if not hasattr(p, "coord"):
                continue
            line = p.coord.line + self.header_lines
            line += 1 if self.header_lines > 0 else 0
            BuErrors.print_error(
                self.path,
                self.file_name,
                line,
                self.get_check_level(),
                self.get_check_id(),
                self.message,
            )
        return 0
