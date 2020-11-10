from checks._check import AbstractCheck

check_end = {".o", ".gch", ".a", ".so", ".d", ".gdca", ".gcno", "~"}
check_presuffix = {"#"}


class FilenameUseless(AbstractCheck):

    def __init__(self, file_name, path, header_lines):
        self.message = "Useless file for compilation"
        self.file_name = file_name
        self.path = path
        self.header_lines = header_lines

    def get_check_id(self):
        return "O1"

    def get_check_level(self):
        return 2

    def check_filename(self):
        try:
            for c in check_end:
                if self.file_name.endswith((c)):
                    return 1
            for c in check_presuffix:
                if self.file_name.startswith((c)) and self.file_name.endswith((c)):
                    return 1
        except Exception as e:
            print(e)
        return 0

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
