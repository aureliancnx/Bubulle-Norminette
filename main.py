import argparse
import ast
import glob
import os
import sys
import re
import traceback
import unittest

import pyparsing

from pycparser import c_parser, c_ast, parse_file
from pycparser.c_ast import FuncCall
from pycparser.plyparser import Coord

import error_handling
import string_utils
from checks.column_toomuch import ColumnToomuch
from checks.declaration_spaces import DeclarationSpaces
from checks.empty_file import EmptyFile
from checks.extra_spaces import ExtraSpaces
from checks.filename_snakecase import FilenameSnakecase
from checks.filename_unclear import FilenameUnclear
from checks.filename_useless import FilenameUseless
from checks.for_curlybrackets import ForCurlybrackets
from checks.forbidden_functions import ForbiddenFunctions
from checks.forbidden_goto import ForbiddenGoto
from checks.function_curlybrackets import FunctionCurlybrackets
from checks.function_snakecase import FunctionSnakecase
from checks.function_toomuch import FunctionToomuch
from checks.function_toomuchargs import FunctionTooMuchArgs
from checks.header_missing import HeaderMissing
from checks.if_curlybrackets import IfCurlybrackets
from checks.indent_tabs import IndentTabs
from checks.lines_extra import LinesExtra
from checks.macro_constants import MacroConstant
from checks.misplaced_pointers import MisplacedPointers
from checks.misplaced_spaces import MisplacedSpace
from checks.missing_spaces import MissingSpace
from checks.multiple_assignements import MultipleAssignements
from checks.variable_snakecase import VariableSnakecase
from checks.variable_typedef import VariableTypedef
from checks.while_curlybrackets import WhileCurlybrackets
from error_handling import BuErrors
from functions_reader import FunctionPrinter
from run_check import RunCheck
from utils import file_utils

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
    print("\033[1;34;40m                          \033[93mBubulle Code Norme Report v1.1")
    print("\033[0mDirectory: \033[93m{0}".format(path))
    print("\033[0m-------------------------------------------------------------------------------")
    print("\033[1;34;40mFile                 Error   Line    Severity   Details")

    print("\033[0m-------------------------------------------------------------------------------\033[1;34;00m")
    checked_paths = []
    for pw, subdirs, files in os.walk(path):
        for name in files:
            check_norme_dir(subdirs)
            complete_path = pw + '/' + name
            if is_tempfile(complete_path):
                continue
            if complete_path in checked_paths:
                continue
            checked_paths.append(complete_path)
            try:
                runcheck = RunCheck(name, complete_path)
                runcheck.run()
            except Exception as e:
                traceback.print_exc()
                print(e)
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
        if string_utils.tosnake(sub) != sub:
            BuErrors.print_error(subdir, -1, 2, "O4", "File name not in snake_case")
            return 0

        #print(func.body)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--p", default=".",
                        help="path to the desired folder")
    parser.add_argument("-u", "--update", action='store_true')
    args = parser.parse_args()
    if args.update:
        os.system("sudo sh -c \"$(curl -fsSL https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/install_bubulle.sh)\"")
        exit()
    error_handling.args = args
    get_path()