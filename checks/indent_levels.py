import re

from checks._check import AbstractCheck
from utils.error_handling import BuErrors

matches = ["if\s*\(((?!\s).+)\)", "while\s*\(((?!\s).+)\)", "for\s*\(((?!\s).+)\)"]

class IndentLevels(AbstractCheck):

    def __init__(self, file_name, header_lines):
        self.message = "Wrong indentation level"
        self.file_name = file_name
        self.header_lines = header_lines

    def get_check_id(self):
        return "L2"

    def get_check_level(self):
        return 1

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
        lines = file_contentf.split('\n')
        i = 0
        index = 0
        new_ind = 0
        last_dc = 0

        for line in lines:
            i += 1
            new_ind = 0
            dc = 0

            if '{' in line:
                index += 1
                new_ind = 1
            elif re.match(r'[ \t]*}[ \t]*', line):
                index -= 1
                if index <= 0:
                    index = 0

            if index > 0 and not len(line) <= 0:
                spaces_diff = len(line) - len(line.lstrip())
                self.line = i + self.header_lines
                if not new_ind:
                    for match in matches:
                        if len(re.findall(match, line)) > 0:
                            last_dc = 2
                if last_dc <= 1:
                    ind_t = index
                    if last_dc == 1:
                        ind_t += 1
                    tmp_indx = 4 * (ind_t - new_ind)
                    if spaces_diff != tmp_indx:
                        BuErrors.print_error(self.file_name, self.line, self.get_check_level(),
                                             self.get_check_id(), self.message)
                    if index >= 4:
                        BuErrors.print_error(self.file_name, self.line, 1,
                                             "C1", "3 or more conditionnal blocks.")

            if last_dc > 0:
                last_dc -= 1
        return 0