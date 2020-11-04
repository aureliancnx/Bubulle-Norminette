import re

from checks._check import AbstractCheck
from utils.error_handling import BuErrors


class FunctionTooLong(AbstractCheck):

    v = None

    def __init__(self, file_name, header_lines):
        self.message = "Func '{0}' too long ('{1}' > 20)"
        self.file_name = file_name
        self.header_lines = header_lines
        self.v = None

    def get_check_id(self):
        return "F4"

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
        global v
        self.v = visitor
        return 0

    def check_inner(self, file_content, file_contentf):
        global v
        last_func = ''
        i = 0
        index = 0
        line_start = -1
        lines = file_contentf.split('\n')

        for line in lines:
            i += 1
            if self.v is not None and self.v.function_defs is not None and line in self.v.function_defs:
                last_func = v.function_defs[line]

            started_newindent = 0
            if '{' in line:
                started_newindent = 1
                if index == 0:
                    line_start = i
                index += 1
                if i - 1 >= 0 and self.v is not None and i - 1 in self.v.function_defs:
                    last_func = self.v.function_defs[i - 1]
            elif re.match(r'[ \t]*}[ \t]*', line):
                started_newindent = 0
                index -= 1
                if index <= 0:
                    index = 0
                    if line_start > 0 and i - line_start - 2 > 20:
                        BuErrors.print_error(self.file_name, i + self.header_lines, 2, "F4",
                                             "Func '{0}' too long ({1} > 20)".format(last_func,
                                                                                     (i - line_start - 2)))
                    line_start = -1
                    last_func = ''
            else:
                started_newindent = 0