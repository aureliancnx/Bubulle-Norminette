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
import ast

from pycparser import c_ast


def extract_funcDef(node, defList):
    if node is None:
        return

    for item in [item[1] for item in node.children()]:
        if isinstance(item, ast.FuncDef):
            defList.append(item)
        else:
            extract_funcDef(item, defList)


# Print functions
class FunctionPrinter(c_ast.NodeVisitor):
    function_count = 0
    function_lines = []
    function_defs = {}
    function_content = {}
    func = []

    def reset_visit(self):
        self.func = []
        self.function_content = {}
        self.function_defs = {}
        self.function_lines = []
        self.function_count = 0

    def visit_FuncDef(self, node):
        self.func.append(node)
        self.function_lines.append(node.decl.coord.line)
        self.function_count = self.function_count + 1
        self.function_content[node.decl.name] = node.body
        self.function_defs[node.decl.coord.line] = node.decl.name