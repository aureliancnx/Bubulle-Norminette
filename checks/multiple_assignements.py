import re

from checks._check import AbstractCheck
from error_handling import BuErrors


class MultipleAssignements(AbstractCheck):

    def __init__(self, file_name, header_lines):
        self.message = "Multiple assignements on same line"
        self.file_name = file_name
        self.header_lines = header_lines

    def get_check_id(self):
        return "L1"

    def get_check_level(self):
        return 1

    def check_line(self, line, line_number):
        return line.count(';') > 1 and not ('for (' in line or 'for(' in line)

    def check_function_calls(self, func):
        return 0

    def check_function_decl(self, visitor, func):
        return 0

    def check_variable_decl(self, var):
        return 0

    def check_visitor(self, visitor, lines):
        return 0

