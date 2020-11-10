from utils import string_utils
from checks._check import AbstractCheck


class VariableSnakecase(AbstractCheck):

    def __init__(self, file_name, path, header_lines):
        self.message = "Variable '{0}' not in snake_case format."
        self.file_name = file_name
        self.path = path
        self.header_lines = header_lines

    def get_check_id(self):
        return "V1"

    def get_check_level(self):
        return 2

    def check_variable_decl(self, var):
        self.fill_error(var.name)
        return string_utils.tosnake(var.name) != var.name

    def check_line(self, line, line_number):
        return 0

    def check_function_calls(self, func):
        return 0

    def check_function_decl(self, visitor, func):
        return 0

    def check_visitor(self, visitor, lines):
        return 0

    def check_inner(self, file_content, file_contentf):
        return 0