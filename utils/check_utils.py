#
# Copyright (c) 2020 aureliancnx
#
# MIT LICENSE
#
# This project is part of aureliancnx.
# See https://github.com/aureliancnx/Bubulle-Norminette for further info.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.#
from checks.column_toomuch import ColumnToomuch
from checks.declaration_spaces import DeclarationSpaces
from checks.empty_file import EmptyFile
from checks.extra_spaces import ExtraSpaces
from checks.filename_snakecase import FilenameSnakecase
from checks.filename_toolong import FilenameTooLong
from checks.filename_unclear import FilenameUnclear
from checks.filename_useless import FilenameUseless
from checks.filename_weirdstart import FilenameWeirdStart
from checks.for_curlybrackets import ForCurlybrackets
from checks.forbidden_functions import ForbiddenFunctions
from checks.forbidden_goto import ForbiddenGoto
from checks.function_comments import FunctionComments
from checks.function_curlybrackets import FunctionCurlybrackets
from checks.function_nested import FunctionNested
from checks.function_separator import FunctionSeparator
from checks.function_snakecase import FunctionSnakecase
from checks.function_toolong import FunctionTooLong
from checks.function_toomuch import FunctionToomuch
from checks.function_toomuchargs import FunctionTooMuchArgs
from checks.function_voidmissing import FunctionVoidMissing
from checks.header_missing import HeaderMissing
from checks.if_curlybrackets import IfCurlybrackets
from checks.indent_levels import IndentLevels
from checks.indent_tabs import IndentTabs
from checks.lines_extra import LinesExtra
from checks.macro_constants import MacroConstant
from checks.misplaced_pointers import MisplacedPointers
from checks.misplaced_spaces import MisplacedSpace
from checks.missing_spaces import MissingSpace
from checks.multiple_assignements import MultipleAssignements
from checks.variable_snakecase import VariableSnakecase
from checks.variable_typedef import VariableTypedef
from checks.variable_unclear import VariableUnclear
from checks.while_curlybrackets import WhileCurlybrackets


def get_filenames():
    return [FilenameUnclear, FilenameUseless, FilenameSnakecase, FilenameTooLong,
            FilenameWeirdStart]


def get_inner():
    return [HeaderMissing, EmptyFile, IfCurlybrackets, ForCurlybrackets, WhileCurlybrackets,
            IndentLevels, FunctionComments, FunctionNested, FunctionTooLong, LinesExtra]


def get_func_decl():
    return [FunctionTooMuchArgs, FunctionVoidMissing, IndentLevels, ForCurlybrackets]


def get_func_call():
    return [ForbiddenFunctions]


def get_var_decl():
    return [VariableSnakecase, VariableTypedef, VariableUnclear]


def get_visitor():
    return [FunctionSnakecase, FunctionCurlybrackets, FunctionToomuch, FunctionSeparator,
            FunctionComments, FunctionTooLong, ForCurlybrackets] # FunctionNestedfix?

def get_pre_visitor():
    return [FunctionTooLong]


def get_line():
    return [MacroConstant, ForbiddenGoto, MisplacedSpace, MissingSpace, MultipleAssignements,
            DeclarationSpaces, ExtraSpaces, ColumnToomuch, MisplacedPointers, IndentTabs]
