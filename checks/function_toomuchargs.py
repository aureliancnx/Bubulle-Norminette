from checks._check import AbstractCheck


class FunctionTooMuchArgs(AbstractCheck):

    def __init__(self, file_name, path, header_lines):
        self.message = "Func '{0}' has too much args. ({1} > 4)"
        self.file_name = file_name
        self.path = path
        self.header_lines = header_lines

    def get_check_id(self):
        return "F5"

    def get_check_level(self):
        return 2

    def check_function_decl(self, visitor, func):
        if not func.decl.type.args:
            return 0
        params = len(func.decl.type.args.params)
        if params <= 4:
            return 0
        func_name = ''
        if func.decl.coord.line in visitor.function_defs:
            func_name = visitor.function_defs[func.decl.coord.line]
        self.fill_error((visitor.function_defs[func.decl.coord.line], params))
        return 1

    def check_line(self, line, line_number):
        return 0

    def check_function_calls(self, func):
        return 0

    def check_variable_decl(self, var):
        return 0

    def check_visitor(self, visitor, lines):
        return 0

    def check_inner(self, file_content, file_contentf):
        return 0