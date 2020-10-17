import re

from checks._check import AbstractCheck
from error_handling import BuErrors


class ColumnToomuch(AbstractCheck):

    def __init__(self, file_name, header_lines):
        self.message = "Too much chars in line ({0} > 80)"
        self.file_name = file_name
        self.header_lines = header_lines

    def get_check_id(self):
        return "F3"

    def get_check_level(self):
        return 2

    def check_line(self, line, line_number):
        length = len(line.replace("\t", "    "))

        if length < 80:
            return 0
        self.fill_error(length)
        return 1

    def check_function_calls(self, func):
        return 0

    def check_function_decl(self, visitor, func):
        return 0

    def check_variable_decl(self, var):
        return 0

    def check_visitor(self, visitor, lines):
        return 0
