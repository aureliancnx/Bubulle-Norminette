import re

from utils import string_utils
from checks._check import AbstractCheck
from utils.error_handling import BuErrors

cache_visitor = None

class FunctionNested(AbstractCheck):

    def __init__(self, file_name, header_lines):
        self.message = "Nested function '{0}'"
        self.file_name = file_name
        self.header_lines = header_lines

    def get_check_id(self):
        return "F7"

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
        global cache_visitor
        cache_visitor = visitor
        return 0

    def check_inner(self, file_content, file_contentf):
        lines = file_contentf.split('\n')
        last_func = ''
        i = 0
        index = 0
        line_start = -1

        for line in lines:
            i += 1
            if line in cache_visitor.function_defs:
                last_func = cache_visitor.function_defs[line]
            for function_line in cache_visitor.function_lines:
                if i != function_line:
                    break
                if index > 0:
                    self.fill_error(cache_visitor.function_defs[function_line])
                    return 1
            if '{' in line:
                index += 1
            elif re.match(r'[ \t]*}[ \t]*', line):
                index -= 1
                if index <= 0:
                    index = 0
        return 0
