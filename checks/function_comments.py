import re

from utils import string_utils
from checks._check import AbstractCheck
from utils.error_handling import BuErrors

cache_visitor = None

class FunctionComments(AbstractCheck):

    def __init__(self, file_name, path, header_lines):
        self.message = "Comments inside a func ('{0}')"
        self.file_name = file_name
        self.path = path
        self.header_lines = header_lines

    def get_check_id(self):
        return "F6"

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
        global cache_visitor
        cache_visitor = visitor
        return 0

    def check_inner(self, file_content, file_contentf):
        lines_with_comments = file_content.split('\n')
        i = 0
        index = 0
        for line in lines_with_comments:
            i += 1
            base_line = line.replace("\t", "").lstrip()
            if index > 0:
                if base_line.startswith("//") or base_line.startswith("/*"):
                    self.fill_error(last_func)
                    BuErrors.print_error(self.path, self.file_name, i, 1, "F6", "Comments inside a func ('{0}')".format(last_func))
            if re.match(r'{[ \t]*', line):
                index += 1
                if i - 1 >= 0 and cache_visitor is not None and i - self.header_lines - 1 in cache_visitor.function_defs:
                    last_func = cache_visitor.function_defs[i - self.header_lines - 1]
            elif re.match(r'[ \t]*}[ \t]*', line):
                index -= 1
                if index <= 0:
                    index = 0
                    last_func = ''

        return 0