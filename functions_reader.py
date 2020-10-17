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

    def visit_FuncDef(self, node):
        self.func.append(node)
        self.function_lines.append(node.decl.coord.line)
        self.function_count = self.function_count + 1
        self.function_content[node.decl.name] = node.body
        self.function_defs[node.decl.coord.line] = node.decl.name
