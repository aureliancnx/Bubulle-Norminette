import re

from checks._check import AbstractCheck


class IfCurlybrackets(AbstractCheck):

    def __init__(self, file_name, header_lines):
        self.message = "Misplaced curly brackets"
        self.file_name = file_name
        self.header_lines = header_lines

    def get_check_id(self):
        return "L4"

    def get_check_level(self):
        return 1

    def check_function_decl(self, visitor, func):
        return 0

    def check_line(self, line, line_number):
        return 0

    def check_function_calls(self, func):
        return 0

    def check_variable_decl(self, var):
        return 0

    def check_visitor(self, visitor, lines):
        return 0

    def check_inner(self, file_content, file_contentf):
        reg = re.compile('if\s*\(((?!\s*\{).+)\)\s*\{(.|\s)*?\}')
        statements = re.finditer(reg, file_contentf)
        for statement in statements:
            lineno = file_content.count('\n', 0, statement.start())
            self.line = lineno
            if not '){' in statement.group(0).replace(" ", ""):
                return 1
        return 0