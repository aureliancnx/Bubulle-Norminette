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
from checks._check import AbstractCheck

disallowed_functions = ('printf', 'dprintf', 'fprintf', 'vprintf', 'sprintf', 'snprintf', 'vprintf',
                                'vfprintf', 'vsprintf', 'vsnprintf', 'asprintf', 'scanf', 'memcpy', 'memset',
                                'memmove', 'strcat', 'strchar', 'strcpy', 'atoi', 'strlen', 'strstr', 'strncpy',
                                'strcasestr', 'strncastestr', 'strcmp', 'strncmp', 'strtok', 'strnlen', 'strdup',
                                'realloc')


class ForbiddenFunctions(AbstractCheck):

    def __init__(self, file_name, path, header_lines):
        self.message = "Forbidden function '{0}'?"
        self.file_name = file_name
        self.path = path
        self.header_lines = header_lines

    def get_check_id(self):
        return "-42?"

    def get_check_level(self):
        return 2

    def check_function_decl(self, visitor, func):
        return 0

    def check_line(self, line, line_number):
        return 0

    def check_function_calls(self, func):
        if func.name.name in disallowed_functions:
            self.line = func.coord.line + (1 if self.header_lines != 0 else 0)
            self.fill_error(func.name.name)
            return 1
        return 0

    def check_variable_decl(self, var):
        return 0

    def check_visitor(self, visitor, lines):
        return 0

    def check_inner(self, file_content, file_contentf):
        return 0