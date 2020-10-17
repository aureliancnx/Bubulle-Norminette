import re

from checks._check import AbstractCheck
from error_handling import BuErrors

misplaced_pointers = ('int*', 'double*', 'float*', 'long*', 'char*', 'string*', 'bool*', 'short*', 'linked_list_t*')


class MisplacedPointers(AbstractCheck):

    def __init__(self, file_name, header_lines):
        self.message = "Pointer misplaced: '{0}'"
        self.file_name = file_name
        self.header_lines = header_lines

    def get_check_id(self):
        return "V3"

    def get_check_level(self):
        return 1

    def check_line(self, line, line_number):
        for pointer in misplaced_pointers:
            if pointer in line:
                return 1
        return 0

    def check_function_calls(self, func):
        return 0

    def check_function_decl(self, visitor, func):
        return 0

    def check_variable_decl(self, var):
        return 0

    def check_visitor(self, visitor, lines):
        return 0
