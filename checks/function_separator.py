import re

from utils import string_utils
from checks._check import AbstractCheck
from utils.error_handling import BuErrors


class FunctionSeparator(AbstractCheck):

    def __init__(self, file_name, header_lines):
        self.message = "One empty line between func"
        self.file_name = file_name
        self.header_lines = header_lines

    def get_check_id(self):
        return "G2"

    def get_check_level(self):
        return 1

    def check_function_decl(self, visitor, func):
        return 0

    def check_line(self, line, line_number):
        return 0

    def check_function_calls(self, func):
        return 0

    def check_variable_decl(self, var):
        return 0

    def check_visitor(self, visitor, lines):
        for function_line in visitor.function_lines:
            if lines[function_line] == '{':
                if len(lines) - (function_line - 1) < 0 or (function_line > 2 and lines[function_line - 2] != ''):
                    return 1
            elif len(lines) - (function_line - 2) < 0:
                return 1
        return 0

    def check_inner(self, file_content, file_contentf):
        return 0