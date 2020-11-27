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

from pycparser.c_ast import For, If, Switch, While

from checks._check import AbstractCheck
from utils.error_handling import BuErrors

sub_stmt = [For, If, Switch, While]


class IndentBranches(AbstractCheck):

    tc = None
    flag_lines = []

    def __init__(self, file_name, path, header_lines):
        self.message = self.get_config()['message']
        self.file_name = file_name
        self.path = path
        self.header_lines = header_lines

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
        pos = -1
        for stm1 in stms:
            pos += 1
            if self.stmt_parse(stm1, node, ilvl + 1, stms_expr[pos]):
                continue
            try:
                for stm in stm1:
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
                    if ilvl_t > self.get_config()['max_branches']:
                        BuErrors.print_error(self.path, self.file_name, line,
                                             self.get_check_level(), self.get_check_id(),
                                             self.message)
            except:
                pass
        return 1

    def check_function_decl(self, visitor, func):
        if func.body.block_items is None:
            return 0
        if tc is None:
            return 0
        ilvl = 0
        for b in func.body.block_items:
            self.stmt_parse(b, None, ilvl + 1, 'a')
        return 0

    def check_variable_decl(self, var):
        return 0

    def check_visitor(self, visitor, lines):
        return 0

    def check_inner(self, file_content, file_contentf):
        global tc
        lines = file_contentf.split('\n')
        tc = lines
        return 0