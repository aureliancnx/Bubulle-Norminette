import re

from pycparser.c_ast import FuncCall

from checks._check import AbstractCheck
from error_handling import BuErrors


class FunctionCurlybrackets(AbstractCheck):

    def __init__(self, file_name, header_lines):
        self.message = "Misplaced curly brackets"
        self.file_name = file_name
        self.header_lines = header_lines

    def get_check_id(self):
        return "L4"

    def get_check_level(self):
        return 1

    def check_function_decl(self, visitor, func):
        params = len(func.decl.type.args.params)
        if params <= 4:
            return 0
        func_name = ''
        if func.decl.coord.line in visitor.function_defs:
            func_name = visitor.function_defs[func.decl.coord.line]
        return 1

    def check_line(self, line, line_number):
        return 0

    def check_function_calls(self, func):
        return 0

    def check_variable_decl(self, var):
        return 0

    def check_visitor(self, visitor, lines):
        for function_line in visitor.function_lines:
            if lines[function_line] != '{' and not lines[function_line - 1].endswith(';'):
                self.line = function_line
                return 1
        return 0

    def check_inner(self, file_content, file_contentf):
        return 0