from utils import string_utils
from checks._check import AbstractCheck


class FilenameSnakecase(AbstractCheck):

    def __init__(self, file_name, header_lines):
        self.message = "File name not in snake_case"
        self.file_name = file_name
        self.header_lines = header_lines

    def get_check_id(self):
        return "O4"

    def get_check_level(self):
        return 2

    def check_filename(self):
        if self.file_name == "Makefile":
            return 0
        return string_utils.tosnake(self.file_name) != self.file_name

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

    def check_inner(self, file_content, file_contentf):
        return 0
