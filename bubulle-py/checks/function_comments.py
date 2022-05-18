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

cache_visitor = None


class FunctionComments(AbstractCheck):
    def __init__(self, file_name, path, header_lines):
        self.message = self.get_config()["message"]
        self.file_name = file_name
        self.path = path
        self.header_lines = header_lines

    def check_ast(self, ast):
        return 0

    def check_function_decl(self, visitor, func):
        return 0

    def check_line(self, line, line_number):
        return 0

    def check_function_calls(self, func):
        return 0

    def check_variable_decl(self, var):
        return 0

    def check_visitor(self, visitor, lines):
        global cache_visitor
        cache_visitor = visitor
        return 0

    def check_inner(self, file_content, file_contentf):
        lines_with_comments = file_content.split("\n")
        index = 0
        for i, line in enumerate(lines_with_comments, start=1):
            base_line = line.replace("\t", "").lstrip()
            if index > 0 and (base_line.startswith("//") or base_line.startswith("/*")):
                self.fill_error(last_func)
                BuErrors.print_error(
                    self.path,
                    self.file_name,
                    i,
                    self.get_check_level(),
                    self.get_check_id(),
                    self.get_config()["message"].format(last_func),
                )

            if re.match(r"{[ \t]*", line):
                index += 1
                if (
                    i >= 1
                    and cache_visitor is not None
                    and i - self.header_lines - 1 in cache_visitor.function_defs
                ):
                    last_func = cache_visitor.function_defs[i - self.header_lines - 1]
            elif re.match(r"[ \t]*}[ \t]*", line):
                index -= 1
                if index <= 0:
                    index = 0
                    last_func = ""
        return 0
