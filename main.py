import argparse
import ast
import glob
import os
import sys
import re
import pyparsing

from pycparser import c_parser, c_ast, parse_file
from pycparser.c_ast import FuncCall
from pycparser.plyparser import Coord

import error_handling
from checks.column_toomuch import ColumnToomuch
from checks.declaration_spaces import DeclarationSpaces
from checks.extra_spaces import ExtraSpaces
from checks.filename_unclear import FilenameUnclear
from checks.filename_useless import FilenameUseless
from checks.forbidden_functions import ForbiddenFunctions
from checks.forbidden_goto import ForbiddenGoto
from checks.function_curlybrackets import FunctionCurlybrackets
from checks.function_snakecase import FunctionSnakecase
from checks.function_toomuchargs import FunctionTooMuchArgs
from checks.indent_tabs import IndentTabs
from checks.macro_constants import MacroConstant
from checks.misplaced_pointers import MisplacedPointers
from checks.misplaced_spaces import MisplacedSpace
from checks.missing_spaces import MissingSpace
from checks.multiple_assignements import MultipleAssignements
from checks.variable_snakecase import VariableSnakecase
from checks.variable_typedef import VariableTypedef
from error_handling import BuErrors
from functions_reader import FunctionPrinter
from string_utils import StringUtils

args = None

def get_severity_col(n):
    if n > 5:
        return "\033[31m" + str(n) + "\033[0m"
    if n >= 3:
        return "\033[33m" + str(n) + "\033[0m"
    if n > 1:
        return "\033[93m" + str(n) + "\033[0m"
    return "\033[32m" + str(n) + "\033[0m"

def get_path():
    path = args.p

    if path == '.':
        path = os.getcwd()

    print("\033[0m-------------------------------------------------------------------------------")
    print("\033[1;34;40m                           \033[93mBubulle Code Norme Report")
    print("\033[0mDirectory: \033[93m{0}".format(path))
    print("\033[0m-------------------------------------------------------------------------------")
    print("\033[1;34;40mFile                 Error   Line    Severity   Details")

    print("\033[0m-------------------------------------------------------------------------------\033[1;34;00m")
    checked_paths = []
    for pw, subdirs, files in os.walk(path):
        for name in files:
            check_norme_dir(subdirs)
            complete_path = pw + '/' + name
            if complete_path in checked_paths:
                continue
            checked_paths.append(complete_path)
            if is_tempfile(complete_path):
                continue
            try:
                check_norme(name, complete_path)
            except:
                continue

    info = 0
    majors = 0
    minors = 0
    note = 0
    for error in error_handling.errors:
        if error.level == 1:
            minors += 1
            note -= 1
        if error.level == 2:
            majors += 1
            note -= 3
        if error.level == 0:
            info += 1
    majors = get_severity_col(majors)
    minors = get_severity_col(minors)
    info = get_severity_col(info)
    print("\033[0m-------------------------------------------------------------------------------")
    print("\033[1;34;40mTOTAL\033[0m          Major: {0}       Minor: {1}       Info: {2}      Note: {3}".format(majors, minors, info, note))
    print("\033[0m-------------------------------------------------------------------------------")

def is_tempfile(path):
    if path.endswith(".tmp"):
        try:
            os.remove(path)
        except:
            pass
        return 1
    return 0

def check_norme_dir(subdir):
    for sub in subdir:
        if StringUtils.tosnake(sub) != sub:
            BuErrors.print_error(subdir, -1, 2, "O4", "File name not in snake_case")
            return 0


def read_file(name):
    f = open(name, 'r')
    return f.read()

def check_norme(file_name, path):
    #L02
    c_file = True
    file_content = read_file(path)
    header_lines = 0
    header_found_end = False
    lines_with_comments = file_content.split('\n')
    for line in lines_with_comments:
        header_lines += 1
        if line.startswith("*/"):
            header_found_end = True
            break

    if not header_found_end:
        header_lines = 0

    filename_unclear = FilenameUnclear(file_name, header_lines)
    filename_unclear.process_filename()
    filename_useless = FilenameUseless(file_name, header_lines)
    filename_useless.process_filename()

    if not file_name.endswith('.c') and not file_name.endswith('.h'):
        c_file = False
        if 'return' in file_content or 'main(' in file_content:
            BuErrors.print_error(file_name, -1, 1, "O2", "File not ending by .c/.h")

    lines = ()

    if c_file:
        parser = c_parser.CParser()
        tmp = path + ".tmp"
        try:
            os.remove(tmp)
        except:
            pass

        try:
            file_contentf = StringUtils.removeComments(file_content)
            f = open(tmp, "a")
            f.write(file_contentf)
            f.close()

            ast = parse_file(tmp)
            os.remove(tmp)
        except c_parser.ParseError:
            e = sys.exc_info()[1]
            return "Parse error:" + str(e)
        try:
            os.remove(tmp)
        except:
            pass
        v = FunctionPrinter()
        v.visit(ast)

        if v.function_count > 5:
            for i in range(0, v.function_count - 5):
                BuErrors.print_error(file_name, -1, 2, "O3", "Too many functions ({0} > 5)".format(v.function_count))

        if StringUtils.tosnake(file_name) != file_name:
            BuErrors.print_error(file_name, -1, 2, "O4", "File name not in snake_case")


        if not file_content.startswith("/*"):
            BuErrors.print_error(file_name, -1, 2, "G1", "EPITECH header missing")
        elif not file_content.split("\n")[1].startswith("** EPITECH PROJECT,"):
            BuErrors.print_error(file_name, -1, 2, "G1", "EPITECH header missing")
        elif not file_content.split("\n")[3].startswith("** File description:"):
            BuErrors.print_error(file_name, -1, 2, "G1", "EPITECH header missing")

        if len(file_contentf) < 1:
            BuErrors.print_error(file_name, -1, 2, "G1", "Empty C source file")
            return

        lines = file_contentf.split('\n')
        for function_line in v.function_lines:
            if lines[function_line] == '{':
                if len(lines) - (function_line - 1) < 0 or lines[function_line - 2] != '':
                    BuErrors.print_error(file_name, function_line + header_lines - 1, 1, "G2", "One empty line between func")
            elif len(lines) - (function_line - 2) < 0:
                    BuErrors.print_error(file_name, function_line + header_lines - 1, 1, "G2", "One empty line between func")

        last_func = ''
        i = 0
        index = 0
        line_start = -1

        for line in lines_with_comments:
            i += 1
            base_line = line.replace("\t", "").lstrip()
            if index > 0:
                if base_line.startswith("//") or base_line.startswith("/*"):
                    BuErrors.print_error(file_name, i, 1, "F6", "Comments inside a func ('{0}')".format(last_func))
            if re.match(r'{[ \t]*', line):
                index += 1
                if i - 1 >= 0 and i - 1 in v.function_defs:
                    last_func = v.function_defs[i - 1]
            elif re.match(r'[ \t]*}[ \t]*', line):
                index -= 1
                if index <= 0:
                    index = 0
                    last_func = ''

        last_func = ''
        i = 0
        index = 0
        line_start = -1

        for line in lines:
            i += 1
            if line in v.function_defs:
                last_func = v.function_defs[line]
            for function_line in v.function_lines:
                if i != function_line:
                    break
                if index > 0:
                    BuErrors.print_error(file_name, i + header_lines - 1, 2, "F7", "Nested function '{0}'".format(v.function_defs[function_line]))

            started_newindent = 0
            if re.match(r'{[ \t]*', line):
                started_newindent = 1
                if index == 0:
                    line_start = i
                index += 1
                if i - 1 >= 0 and i - 1 in v.function_defs:
                    last_func = v.function_defs[i - 1]
            elif re.match(r'[ \t]*}[ \t]*', line):
                started_newindent = 0
                index -= 1
                if index <= 0:
                    index = 0
                    if line_start > 0 and i - line_start - 2 > 20:
                        BuErrors.print_error(file_name, i + header_lines - 1, 2, "F4", "Func '{0}' too long ({1} > 20)".format(last_func, (i - line_start - 2)))
                    line_start = -1
                    last_func = ''
            else:
                started_newindent = 0

            #if index > 0 and not len(line) <= 0:
            #    spaces_diff = len(line) - len(line.lstrip())
            #    if spaces_diff != 4 * index:
            #        BuErrors.print_error(file_name, i + header_lines - 1, 1, "L2", "Error in indent levels {0} != {1}".format(index * 4, spaces_diff))
            #
                #elif (index - 1) * 4 != spaces_diff and started_newindent:
                #    print(line)
                #    print("[{0}:{1}] L2 - Misusage of indentation level. {2} != {3}".format(file_name,
                #                                                                            i + header_lines - 1,
                #                                                                            index * 4, spaces_diff))

        # CHECK visitor
        function_snakecase = FunctionSnakecase(file_name, header_lines)
        function_snakecase.process_visitor_check(v, lines)
        function_curlybrackets = FunctionCurlybrackets(file_name, header_lines)
        function_curlybrackets.process_visitor_check(v, lines)

        # CHECK functions & vars
        forbidden_functions = ForbiddenFunctions(file_name, header_lines)
        variable_typedef = VariableTypedef(file_name, header_lines)
        variable_snakecase = VariableSnakecase(file_name, header_lines)
        function_toomuchargs = FunctionTooMuchArgs(file_name, header_lines)

        for func in v.func:
            function_toomuchargs.process_function_decl(v, func)
            for var in func.body.block_items:
                forbidden_functions.process_function_call(var)
                variable_snakecase.process_variable_decl(var)
                variable_typedef.process_variable_decl(var)

        macro_constants = MacroConstant(file_name, header_lines)
        forbidden_goto = ForbiddenGoto(file_name, header_lines)
        misplaced_spaces = MisplacedSpace(file_name, header_lines)
        missing_spaces = MissingSpace(file_name, header_lines)
        multiple_assignements = MultipleAssignements(file_name, header_lines)
        declaration_spaces = DeclarationSpaces(file_name, header_lines)
        extra_spaces = ExtraSpaces(file_name, header_lines)
        column_toomuch = ColumnToomuch(file_name, header_lines)
        misplaced_spaces = MisplacedPointers(file_name, header_lines)
        indent_tabs = IndentTabs(file_name, header_lines)

        line_index = 0
        for line in lines:
            line_index += 1
            macro_constants.process_line(line, line_index)
            forbidden_goto.process_line(line, line_index)
            misplaced_spaces.process_line(line, line_index)
            missing_spaces.process_line(line, line_index)
            multiple_assignements.process_line(line, line_index)
            extra_spaces.process_line(line, line_index)
            column_toomuch.process_line(line, line_index)
            misplaced_spaces.process_line(line, line_index)
            indent_tabs.process_line(line, line_index)


        #print(func.body)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--p", default=".",
                        help="path to the desired folder")
    args = parser.parse_args()
    error_handling.args = args
    get_path()