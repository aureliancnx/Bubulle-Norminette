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
from abc import ABC, abstractmethod, ABCMeta

from pycparser.c_ast import FuncCall, Decl, FuncDecl

from utils.error_handling import BuErrors


class AbstractCheck(ABC):
    __metaclass__ = ABCMeta
    pass

    @abstractmethod
    def check_line(self, line, line_number):
        pass

    @abstractmethod
    def check_function_calls(self, function):
        pass

    @abstractmethod
    def check_variable_decl(self, function):
        pass

    @abstractmethod
    def check_function_decl(self, visitor, func):
        pass

    @abstractmethod
    def check_visitor(self, visitor, lines):
        pass

    @abstractmethod
    def check_inner(self, content, contentf):
        pass

    def fill_error(self, args):
        self.args = args

    def process_filename(self):
        if not self.check_filename():
            return 0
        self.err("", -1, self.message)

    def process_function_call(self, func):
        if type(func) is not FuncCall:
            return 0
        if not hasattr(func, 'name'):
            return 0
        if not self.check_function_calls(func):
            return 0
        if not hasattr(self, 'args'):
            self.err("", -1, self.message)
            return 1
        self.err("", -1, self.message.format(self.args))
        return 1

    def process_function_decl(self, visitor, func):
        if type(func.decl.type) is not FuncDecl:
            return 0
        if not self.check_function_decl(visitor, func):
            return 0
        line = self.line if hasattr(self, 'line') else -1
        if not hasattr(self, 'args'):
            self.err("", line, self.message)
            return 1
        self.err("", line, self.message.format(self.args))
        return 1

    def process_visitor_check(self, visitor, lines):
        if not self.check_visitor(visitor, lines):
            return 0
        line = self.line if hasattr(self, 'line') else -1
        if not hasattr(self, 'args'):
            self.err("", line, self.message)
            return 1
        self.err("", line, self.message.format(self.args))
        return 1

    def process_variable_decl(self, var):
        if type(var) is not Decl:
            return 0
        if not hasattr(var, 'name'):
            return 0
        if not self.check_variable_decl(var):
            return 0
        if not hasattr(self, 'args'):
            self.err("", -1, self.message)
            return 1
        self.err("", -1, self.message.format(self.args))
        return 1

    def process_line(self, line, line_number):
        if not self.check_line(line, line_number):
            return 0
        if not hasattr(self, 'args'):
            self.err(line, line_number, self.message)
            return 1
        self.err(line, line_number, self.message.format(self.args))
        return 1

    def process_inner(self, content, contentf):
        if not self.check_inner(content, contentf):
            return 0
        line_n = -1
        if hasattr(self, 'line'):
            line_n = self.line
        if not hasattr(self, 'args'):
            self.err("", line_n, self.message)
            return 1
        self.err("", line_n, self.message.format(self.args))
        return 1

    def err(self, line, line_number, text):
        if line_number != -1:
            line_number += self.header_lines
        BuErrors.print_error(self.path, self.file_name, line_number, self.get_check_level(),
                             self.get_check_id(), text)

    def get_check_id(self):
        pass

    def get_check_level(self):
        pass