import re

from checks._check import AbstractCheck
from utils import string_utils
from utils.error_handling import BuErrors

class VariableUnclear(AbstractCheck):

    def __init__(self, file_name, header_lines):
        self.message = "Unclear variable name: '{0}'"
        self.file_name = file_name
        self.header_lines = header_lines

    def get_check_id(self):
        return "T010"

    def get_check_level(self):
        return 0

    def check_line(self, line, line_number):
        return 0

    def check_function_calls(self, func):
        return 0

    def check_function_decl(self, visitor, func):
        return 0

    def check_variable_decl(self, var):
        self.fill_error(var.name)
        return var.name == 'l' or var.name == 'o'

    def check_visitor(self, visitor, lines):
        return 0

    def check_inner(self, file_content, file_contentf):
        return 0