from utils import string_utils
from checks._check import AbstractCheck


class FunctionSnakecase(AbstractCheck):

    def __init__(self, file_name, path, header_lines):
        self.message = "Func '{0}' not in snake_case"
        self.file_name = file_name
        self.path = path
        self.header_lines = header_lines

    def get_check_id(self):
        return "F2"

    def get_check_level(self):
        return 2

    def check_function_decl(self, visitor, func):
        return 0

    def check_line(self, line, line_number):
        return 0

    def check_function_calls(self, func):
        return 0

    def check_variable_decl(self, var):
        return 0

    def check_visitor(self, visitor, lines):
        for function_line in visitor.function_defs:
            if string_utils.tosnake(visitor.function_defs[function_line]) != visitor.function_defs[function_line]:
                self.fill_error(visitor.function_defs[function_line])
                return 1
        return 0

    def check_inner(self, file_content, file_contentf):
        return 0