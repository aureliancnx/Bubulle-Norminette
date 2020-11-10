from checks._check import AbstractCheck

disallowed_functions = ('printf', 'dprintf', 'fprintf', 'vprintf', 'sprintf', 'snprintf', 'vprintf',
                                'vfprintf', 'vsprintf', 'vsnprintf', 'asprintf', 'scanf', 'memcpy', 'memset',
                                'memmove', 'strcat', 'strchar', 'strcpy', 'atoi', 'strlen', 'strstr', 'strncpy',
                                'strcasestr', 'strncastestr', 'strcmp', 'strncmp', 'strtok', 'strnlen', 'strdup',
                                'realloc')


class ForbiddenFunctions(AbstractCheck):

    def __init__(self, file_name, path, header_lines):
        self.message = "Forbidden function '{0}'?"
        self.file_name = file_name
        self.path = path
        self.header_lines = header_lines

    def get_check_id(self):
        return "-42?"

    def get_check_level(self):
        return 2

    def check_function_decl(self, visitor, func):
        return 0

    def check_line(self, line, line_number):
        return 0

    def check_function_calls(self, func):
        if func.name.name in disallowed_functions:
            self.fill_error(func.name.name)
            return 1
        return 0

    def check_variable_decl(self, var):
        return 0

    def check_visitor(self, visitor, lines):
        return 0

    def check_inner(self, file_content, file_contentf):
        return 0