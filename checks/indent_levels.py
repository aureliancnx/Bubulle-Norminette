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
import json
import re

from pycparser.c_ast import For, If, Switch, While

from checks._check import AbstractCheck
from utils.error_handling import BuErrors

matches = ["if\s*\(((?!\s).+)\)", "while\s*\(((?!\s).+)\)", "for\s*\(((?!\s).+)\)"
           , "else\s"]

sub_stmt = [For, If, Switch, While]

t_mul = 4

class IndentLevels(AbstractCheck):

    tc = None
    flag_lines = []
    def __init__(self, file_name, path, header_lines):
        self.message = "Indentation must be {0} spaces but it's {1}"
        self.base_message = "Wrong indentation level"
        self.file_name = file_name
        self.path = path
        self.header_lines = header_lines

    def get_check_id(self):
        return "L2"

    def get_check_level(self):
        return 1

    def check_line(self, line, line_number):
        return 0

    def check_function_calls(self, func):
        return 0

    def stmt_parse(self, node, last, ilvl, last_expr):
        stmb = 0
        for st in sub_stmt:
            if isinstance(node, st):
                stmb = 1
        if not stmb:
            return 0
        stms = []
        stms_expr = []
        if hasattr(node, 'iftrue') and node.iftrue is not None:
            stms.append(node.iftrue)
            stms_expr.append('iftrue')
        if hasattr(node, 'iffalse') and node.iffalse is not None:
            stms.append(node.iffalse)
            stms_expr.append('iffalse')
        if hasattr(node, 'stmt') and node.stmt is not None:
            stms.append(node.stmt)
            stms_expr.append('stmt')
        node_cc = node.coord.line - 1
        nodel = tc[node_cc]
        node_s = len(nodel) - len(nodel.lstrip())
        #if node_s != (ilvl) * t_mul and node_cc + 1 not in flag_lines:
        #    flag_lines.append(node_cc + 1)
        #    BuErrors.print_error(self.path, self.file_name, node_cc + 1 + self.header_lines,
        #                         self.get_check_level(), self.get_check_id(),
        #                         'a' + self.message.format(str((ilvl) * t_mul), str(node_s)))
        pos = -1
        for stm1 in stms:
            pos += 1
            if self.stmt_parse(stm1, node, ilvl + 1, stms_expr[pos]):
                continue
            for stm in stm1:
                ilvl_n = ilvl
                if self.stmt_parse(stm, node, ilvl + 1, stms_expr[pos]):
                    continue
                li = stm.coord.line - 1
                l = tc[li]
                s = len(l) - len(l.lstrip())
                line = li + 1 + self.header_lines + (1 if self.header_lines > 0 else 0)
                # Handle conditional branches

                ilvl_t = ilvl
                if isinstance(node, If) and isinstance(last, If):
                    if last.iffalse and hasattr(last.iffalse, 'iftrue') and stm1 == last.iffalse.iftrue:
                        ilvl_t -= 1
                    elif last.iffalse and hasattr(last.iffalse, 'iffalse') and stm1 == last.iffalse.iffalse:
                        ilvl_t -= 1
                if s != ilvl_t * t_mul and line not in flag_lines:
                    flag_lines.append(line)
                    print("LAST:")
                    print(last.iffalse)
                    print("NODE:")
                    print(stm1)
                    BuErrors.print_error(self.path, self.file_name, line,
                                         self.get_check_level(), self.get_check_id(),
                                         self.message.format(str(ilvl_t * t_mul), str(s)) + ' [{0}]'.format(l))
        return 1

    def check_function_decl(self, visitor, func):
        if func.body.block_items is None:
            return 0
        if tc is None:
            return 0
        ilvl = 1
        for b in func.body.block_items:
            li = b.coord.line - 1
            l = tc[li]
            s = len(l) - len(l.lstrip())
            line = li + 1 + self.header_lines + 1 if self.header_lines > 1 else 0
            if s != ilvl * t_mul and line not in flag_lines:
                flag_lines.append(line)
                BuErrors.print_error(self.path, self.file_name, line,
                                     self.get_check_level(), self.get_check_id(),
                                     self.message.format(str(ilvl * t_mul), str(s)))
            self.stmt_parse(b, None, ilvl + 1, 'a')
        return 0

    def check_variable_decl(self, var):
        return 0

    def check_visitor(self, visitor, lines):
        return 0

    def check_inner(self, file_content, file_contentf):
        global tc
        global flag_lines
        flag_lines = []
        lines = file_contentf.split('\n')
        lc = 0
        tc = lines
        # TODO better check
        # workaround while we develop something better.

        for l in lines:
            lc += 1
            s = len(l) - len(l.lstrip())
            self.line = lc + self.header_lines
            self.line += 1 if self.header_lines > 0 else 0
            if s % 4 != 0:
                flag_lines.append(self.line)
                BuErrors.print_error(self.path, self.file_name, self.line, self.get_check_level(),
                                     self.get_check_id(), self.base_message)
        return 0