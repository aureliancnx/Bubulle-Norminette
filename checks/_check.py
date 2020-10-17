import re
from abc import ABC, abstractmethod, ABCMeta

from pycparser.c_ast import FuncCall, Decl, FuncDecl

from error_handling import BuErrors


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
        if not self.args:
            self.err("", -1, self.message)
            return 1
        self.err("", -1, self.message.format(self.args))
        return 1

    def process_function_decl(self, visitor, func):
        if not func.decl.type.args:
            return 0
        if type(func.decl.type) is not FuncDecl:
            return 0
        if not self.check_function_decl(visitor, func):
            return 0
        if not self.args:
            self.err("", -1, self.message)
            return 1
        self.err("", -1, self.message.format(*self.args))
        return 1

    def process_visitor_check(self, visitor, lines):
        if not self.check_visitor(visitor, lines):
            return 0
        self.err("", -1, self.message)
        return 1

    def process_variable_decl(self, var):
        if type(var) is not Decl:
            return 0
        if not hasattr(var, 'name'):
            return 0
        if not self.check_variable_decl(var):
            return 0
        if not self.args:
            self.err("", -1, self.message)
            return 1
        self.err("", -1, self.message.format(self.args))
        return 1

    def process_line(self, line, line_number):
        if not self.check_line(line, line_number):
            return 0
        if not self.args:
            self.err(line, line_number, self.message)
            return 1
        self.err(line, line_number, self.message.format(self.args))
        return 1

    def err(self, line, line_number, text):
        line_number += self.header_lines - 1 if line_number != -1 else 0
        BuErrors.print_error(self.file_name, line_number, self.get_check_level(), self.get_check_id(), text)

    def get_check_id(self):
        pass

    def get_check_level(self):
        pass