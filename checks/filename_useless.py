import re

from checks._check import AbstractCheck
from error_handling import BuErrors

check = {".o", ".gch", ".a", ".so", ".d"}


class FilenameUseless(AbstractCheck):

    def __init__(self, file_name, header_lines):
        self.message = "Useless file for compilation"
        self.file_name = file_name
        self.header_lines = header_lines

    def get_check_id(self):
        return "O1"

    def get_check_level(self):
        return 2

    def check_filename(self):
        try:
            for c in check:
                if self.file_name.endswith((c)):
                    return 1
        except Exception as e:
            print(e)
        return 0

    def check_line(self, line, line_number):
        return 0

    def check_function_calls(self, func):
        return 0

    def check_function_decl(self, visitor, func):
        return 0

    def check_variable_decl(self, var):
        return 0

    def check_visitor(self, visitor, lines):
        return 0
