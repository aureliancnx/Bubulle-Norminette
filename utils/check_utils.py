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


def get_filenames():
    return [FilenameUnclear, FilenameUseless, FilenameSnakecase]


def get_inner():
    return [HeaderMissing, EmptyFile, IfCurlybrackets, ForCurlybrackets, WhileCurlybrackets]


def get_func_decl():
    return [FunctionTooMuchArgs]


def get_func_call():
    return [ForbiddenFunctions]


def get_var_decl():
    return [VariableSnakecase, VariableTypedef]


def get_visitor():
    return [FunctionSnakecase, FunctionCurlybrackets, FunctionToomuch]


def get_line():
    return [MacroConstant, ForbiddenGoto, MisplacedSpace, MissingSpace, MultipleAssignements,
            DeclarationSpaces, ExtraSpaces, ColumnToomuch, MisplacedPointers, IndentTabs,
            LinesExtra]
