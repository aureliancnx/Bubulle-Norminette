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

from checks._check import Check

cache_visitor = None


class FunctionNested(Check):
    def __init__(self, file_name, path, header_lines):
        self.message = self.get_config()["message"]
        self.file_name = file_name
        self.path = path
        self.header_lines = header_lines

    def check_visitor(self, visitor, lines):
        global cache_visitor
        cache_visitor = visitor
        return 0

    def check_inner(self, file_content, file_contentf):
        if cache_visitor is None:
            return 0
        lines = file_contentf.split("\n")
        index = 0
        line_start = -1

        last_func = ""
        for i, line in enumerate(lines, start=1):
            if line in cache_visitor.function_defs:
                last_func = cache_visitor.function_defs[line]
            for function_line in cache_visitor.function_lines:
                if i != function_line:
                    break
                if index > 0:
                    self.fill_error(cache_visitor.function_defs[function_line])
                    return 1
            if "{" in line:
                index += 1
            elif re.match(r"[ \t]*}[ \t]*", line):
                index -= 1
                index = max(index, 0)
        return 0
