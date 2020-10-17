import re

from checks._check import AbstractCheck
from error_handling import BuErrors


class LinesExtra(AbstractCheck):

    def __init__(self, file_name, header_lines):
        self.message = "Extra lines"
        self.file_name = file_name
        self.header_lines = header_lines
        self.last_empty_line = -100

    def get_check_id(self):
        return "L6"

    def get_check_level(self):
        return 1

    def check_line(self, line, line_number):
        if len(line.strip()) == 0:
            if self.last_empty_line == line_number - 1:
                self.last_empty_line = line_number
                return 1
            self.last_empty_line = line_number
            return 0
        self.last_empty_line = -100
        return 0

    def check_function_calls(self, func):
        return 0

    def check_variable_decl(self, var):
        return 0

    def check_function_decl(self, visitor, func):
        return 0

    def check_visitor(self, visitor, lines):
        return 0

    def check_inner(self, file_content, file_contentf):
        return 0