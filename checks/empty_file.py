from checks._check import AbstractCheck


class EmptyFile(AbstractCheck):

    def __init__(self, file_name, header_lines):
        self.message = "Empty source file"
        self.file_name = file_name
        self.header_lines = header_lines

    def get_check_id(self):
        return "G1"

    def get_check_level(self):
        return 2

    def check_filename(self):
        return 0

    def check_line(self, line, line_number):
        return 0

    def check_inner(self, content, contentf):
        return len(contentf) < 1

    def check_function_calls(self, func):
        return 0

    def check_function_decl(self, visitor, func):
        return 0

    def check_variable_decl(self, var):
        return 0

    def check_visitor(self, visitor, lines):
        return 0
