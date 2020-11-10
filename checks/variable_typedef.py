from checks._check import AbstractCheck


class VariableTypedef(AbstractCheck):

    def __init__(self, file_name, path, header_lines):
        self.message = "Typedef '{0}' must ends with _t"
        self.file_name = file_name
        self.path = path
        self.header_lines = header_lines

    def get_check_id(self):
        return "V1"

    def get_check_level(self):
        return 2

    def check_variable_decl(self, var):
        return 'typedef' in var.storage and not var.name.endswith('_t')

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