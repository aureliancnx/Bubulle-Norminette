import re

from checks._check import AbstractCheck


class ForbiddenGoto(AbstractCheck):

    def __init__(self, file_name, header_lines):
        self.message = "Forbidden keyword 'goto'"
        self.file_name = file_name
        self.header_lines = header_lines

    def get_check_id(self):
        return "-42?"

    def get_check_level(self):
        return 2

    def check_line(self, line, line_number):
        return re.match(r'/(^|[^0-9a-zA-Z_])(goto)[^0-9a-zA-Z]/', line)

    def check_function_calls(self, func):
        return 0

    def check_function_decl(self, visitor, func):
        return 0

    def check_variable_decl(self, var):
        return 0

    def check_visitor(self, visitor, lines):
        return 0

    def check_inner(self, file_content, file_contentf):
        return 0