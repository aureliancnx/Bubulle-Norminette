import re

from pycparser.c_ast import FuncCall

from checks._check import AbstractCheck
from error_handling import BuErrors
from string_utils import StringUtils


class FunctionSnakecase(AbstractCheck):

    def __init__(self, file_name, header_lines):
        self.message = "Func '{0}' not in snake_case"
        self.file_name = file_name
        self.header_lines = header_lines

    def get_check_id(self):
        return "F2"

    def get_check_level(self):
        return 2

    def check_function_decl(self, visitor, func):
        return 0

    def check_line(self, line, line_number):
        return 0

    def check_function_calls(self, func):
        return 0

    def check_variable_decl(self, var):
        return 0

    def check_visitor(self, visitor, lines):
        for function_line in visitor.function_defs:
            if StringUtils.tosnake(visitor.function_defs[function_line]) != visitor.function_defs[function_line]:
                self.fill_error(visitor.function_defs[function_line])
                return 1
        return 0
