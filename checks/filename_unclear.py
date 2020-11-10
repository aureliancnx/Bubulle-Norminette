from checks._check import AbstractCheck

notclear_names = (
'string.c', 'str.c', 'my_string.c', 'my_str.c', 'algorithm.c', 'my_algorithm.c', 'algo.c', 'my_algo.c', 'program.c',
'main.c', 'my_program.c', 'test.c', 'prog.c', 'my_prog.c')

class FilenameUnclear(AbstractCheck):

    def __init__(self, file_name, path, header_lines):
        self.message = "File name not clear enough"
        self.file_name = file_name
        self.path = path
        self.header_lines = header_lines

    def get_check_id(self):
        return "O4"

    def get_check_level(self):
        return 2

    def check_filename(self):
        try:
            for name in notclear_names:
                if name == self.file_name:
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
