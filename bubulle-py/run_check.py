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
import os
import traceback

from pycparser import c_parser, parse_file

from utils import file_utils, check_utils, string_utils, error_handling, c_utils
from utils.functions_reader import FunctionPrinter

run_err = "\033[31m{0}: Unable to run test: {1}. -verbose for more info.\033[0m"


class RunCheck:
    def __init__(self, file_name, full_path):
        self.file_name = file_name
        self.full_path = full_path.replace("\\\\", "\\").replace("//", "/")
        self.file_content = None

    def is_validsource(self):
        if self.file_name.endswith(".tmp"):
            self.delete_temp(already=True)
        return self.file_name.endswith(".c") or self.file_name.endswith(".h")

    def delete_temp(self, already=False):
        path = self.full_path
        if not already:
            path = f"{path}.tmp"

        if os.path.exists(path):
            os.remove(path)

    def read_content(self):
        try:
            self.file_content = file_utils.read_file(self.full_path)
            return 1
        except OSError:
            return 0

    def get_header_lines(self):
        header_lines = 0
        header_found_end = False
        lines_with_comments = self.file_content.split("\n")
        for line in lines_with_comments:
            header_lines += 1
            if line.startswith("*/"):
                header_found_end = True
                break

        if not header_found_end:
            return 0
        return header_lines

    # TODO: rewrite this crap
    def run(self):
        self.delete_temp()
        tmp = f"{self.full_path}.tmp"

        for clazz in check_utils.get_filenames():
            try:
                clazz = clazz(
                    file_name=self.file_name, path=self.full_path, header_lines=0
                )
                clazz.process_filename()
            except Exception as e:
                if error_handling.args.verbose:
                    traceback.print_exc()
                    print(e)
                print(run_err.format(self.full_path, clazz.__class__.__name__))

        if not self.is_validsource():
            return

        if not self.read_content():
            return

        header_lines = self.get_header_lines()
        lines_with_comments = self.file_content.split("\n")
        lines = ()
        parser = c_parser.CParser()

        file_contentf = string_utils.remove_comments(self.file_content)
        lines = file_contentf.split("\n")
        header_lines = len(lines_with_comments) - len(lines)
        header_lines = max(header_lines, 0)
        parsed = False
        try:
            with open(tmp, "a", encoding="utf-8") as file:
                file.write(file_contentf.replace("bool ", "_Bool "))
            ast = parse_file(tmp, use_cpp=True, cpp_args=c_utils.includes)
            self.delete_temp()
            parsed = True
        except c_parser.ParseError as e:
            line = str(e).split(":")
            self.delete_temp()
            if error_handling.args.verbose:
                print(e)

        self.delete_temp()
        if parsed:
            v = FunctionPrinter()
            v.reset_visit()
            v.visit(ast)

            for clazz in check_utils.get_ast():
                try:
                    clazz = clazz(
                        file_name=self.file_name,
                        path=self.full_path,
                        header_lines=header_lines,
                    )
                    clazz.process_ast(ast)
                except Exception as e:
                    if error_handling.args.verbose:
                        traceback.print_exc()
                        print(e)
                    print(run_err.format(self.full_path, clazz.__class__.__name__))

            for clazz in check_utils.get_pre_visitor():
                try:
                    clazz = clazz(
                        file_name=self.file_name,
                        path=self.full_path,
                        header_lines=header_lines,
                    )
                    clazz.process_visitor_check(v, lines)
                except Exception as e:
                    if error_handling.args.verbose:
                        traceback.print_exc()
                        print(e)
                    print(run_err.format(self.full_path, clazz.__class__.__name__))

        for line_index, line in enumerate(lines, start=1):
            for clazz in check_utils.get_line():
                try:
                    clazz = clazz(
                        file_name=self.file_name,
                        path=self.full_path,
                        header_lines=header_lines,
                    )
                    clazz.process_line(line, line_index)
                except Exception as e:
                    if error_handling.args.verbose:
                        traceback.print_exc()
                        print(e)
                    print(run_err.format(self.full_path, clazz.__class__.__name__))

        for clazz in check_utils.get_inner():
            try:
                clazz = clazz(
                    file_name=self.file_name,
                    path=self.full_path,
                    header_lines=header_lines,
                )
                clazz.process_inner(self.file_content, file_contentf)
            except Exception as e:
                if error_handling.args.verbose:
                    traceback.print_exc()
                    print(e)
                print(run_err.format(self.full_path, clazz.__class__.__name__))

        v = None
        if parsed:
            v = FunctionPrinter()
            v.reset_visit()
            v.visit(ast)

            for clazz in check_utils.get_visitor():
                try:
                    clazz = clazz(
                        file_name=self.file_name,
                        path=self.full_path,
                        header_lines=header_lines,
                    )
                    clazz.process_visitor_check(v, lines)
                except Exception as e:
                    if error_handling.args.verbose:
                        traceback.print_exc()
                        print(e)
                    print(run_err.format(self.full_path, clazz.__class__.__name__))

            for func in v.func:
                for clazz in check_utils.get_func_decl():
                    try:
                        clazz = clazz(
                            file_name=self.file_name,
                            path=self.full_path,
                            header_lines=header_lines,
                        )
                        clazz.process_function_decl(v, func)
                    except Exception as e:
                        if error_handling.args.verbose:
                            traceback.print_exc()
                            print(e)
                        print(run_err.format(self.full_path, clazz.__class__.__name__))
                if func.body.block_items is not None:
                    for var in func.body.block_items:
                        for clazz in check_utils.get_func_call():
                            try:
                                clazz = clazz(
                                    file_name=self.file_name,
                                    path=self.full_path,
                                    header_lines=header_lines,
                                )
                                clazz.process_function_call(var)
                            except Exception as e:
                                if error_handling.args.verbose:
                                    traceback.print_exc()
                                    print(e)
                                print(
                                    run_err.format(
                                        self.full_path, clazz.__class__.__name__
                                    )
                                )
                        for clazz in check_utils.get_var_decl():
                            try:
                                clazz = clazz(
                                    file_name=self.file_name,
                                    path=self.full_path,
                                    header_lines=header_lines,
                                )
                                clazz.process_variable_decl(var)
                            except Exception as e:
                                if error_handling.args.verbose:
                                    traceback.print_exc()
                                    print(e)
                                print(
                                    run_err.format(
                                        self.full_path, clazz.__class__.__name__
                                    )
                                )
