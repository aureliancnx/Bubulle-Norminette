from checks._check import AbstractCheck


class HeaderMissing(AbstractCheck):

    def __init__(self, file_name, path, header_lines):
        self.message = "EPITECH header misplaced/missing"
        self.file_name = file_name
        self.path = path
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
        if not content.startswith("/*"):
            return 1
        if not content.split("\n")[1].startswith("** EPITECH PROJECT,"):
            return 1
        if not content.split("\n")[3].startswith("** File description:"):
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