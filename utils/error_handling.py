import re

from utils.string_utils import colors

errors = []
args = None

class BuError():
    def __init__(self, file_name, errid, level, line, message):
        self.file_name = file_name
        self.errid = errid
        self.level = level
        self.line = line
        self.message = message

    def print_error(self):
        try:
            highlight = "\33[44m "
            if self.level == 1:
                highlight = "\33[0;30;43m "
            elif self.level == 2:
                highlight = "\x1b[0;30;41m "

            line_st = ""
            if not isinstance(self.file_name, str):
                self.file_name = self.file_name[0]
            if len(self.file_name) > 19:
                self.file_name = self.file_name[:15] + "..."
            level_st = ""
            err_spaces = 22 - len(self.file_name)
            shown_err = ""
            for i in range(1, err_spaces):
                shown_err = shown_err + " "
            shown_err = shown_err + str(self.errid)
            line_spaces = 9 - len(self.errid)
            if self.line != -1:
                line_st = line_st + highlight + str(self.line)
            level_spaces = 7 - len(str(self.line))
            for i in range(1, level_spaces):
                level_st = " " + level_st
            if self.line == -1:
                line_st = line_st + "   "

            if self.level == 0:
                level_st = level_st + "\33[44m INFO " + colors.ENDC
            elif self.level == 1:
                level_st = level_st + "\33[0;30;43m MINOR " + colors.ENDC
            else:
                level_st = level_st + "\x1b[0;30;41m MAJOR " + colors.ENDC
            for i in range(1, line_spaces):
                line_st = " " + line_st
            level_space = 8 if self.level == 0 else 7
            details_spaces = level_space - len(str(self.line))
            color = '\033[37m' if len(errors) % 2 == 1 else '\033[0m'
            message = color + self.message
            details_st = message
            for i in range(1, details_spaces):
                details_st = " " + details_st
            line_st = line_st + " \033[0m"
            print("{0}{1}{2}{3}{4}".format(color + self.file_name, color + shown_err, color + line_st, level_st, details_st))
        except Exception as e:
            print(e)

class BuErrors:

    def split_on_empty_lines(s):
        blank_line_regex = r"(?:\r?\n){2,}"
        return re.split(blank_line_regex, s.strip())

    def print_error(file_name, line, level, errid, message):
        error = BuError(file_name, errid, level, line, message)
        errors.append(error)
        error.print_error()
