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
import os.path

from html_report.htmlparser_utils import fill_variable


class HtmlReportDetail:
    def __init__(self, report, path, file_name, info, minor, major, source, errors):
        self.report = report
        self.path = path
        self.file_name = file_name
        self.info = info
        self.minor = minor
        self.major = major
        self.source = source
        self.errors = errors
        self.generate()

    def escape_source(self):
        split = self.source.split("\n")
        fin = ""
        for line, split_fragment in enumerate(split, start=1):
            fin += split_fragment
            for error in self.errors:
                if error.get("line") != line and (line != 1 or error.get("line") != -1):
                    continue
                error["pos"] = len(split_fragment)
                fin += " /* {0}: {1} */".format(
                    error.get("errid"), error.get("message")
                )
            fin += "\n"
        self.source = fin
        self.source = self.source.replace("'", "\\'")
        self.source = self.source.replace("\n", "\\n")

    @staticmethod
    def get_init_content():
        with open(
            f"{os.path.dirname(os.path.realpath(__file__))}/../../assets/html/report-file.html",
            "r",
        ) as file:
            content = file.read()
        return content

    def save_details(self, content):
        with open(
            f"{self.report.folder}html/{self.path}.html", "w+", encoding="utf-8"
        ) as file_w:
            file_w.write(content)

    def highlight_errors(self, content):
        mistakes = ""
        with open(
            f"{os.path.dirname(os.path.realpath(__file__))}/../../assets/cards/mistake.js",
            "r",
            encoding="utf-8",
        ) as file:
            base = file.read()
        for error in self.errors:
            mistakes_temp = base
            type_ = "info"
            type_ = "minor" if error.get("level") == 1 else "major"
            if error.get("line") <= 0:
                mistakes_temp = fill_variable(mistakes_temp, "line", "0")
            else:
                mistakes_temp = fill_variable(
                    mistakes_temp, "line", str(error.get("line") - 1)
                )
            mistakes_temp = fill_variable(
                mistakes_temp, "line_end", str(error.get("pos"))
            )
            mistakes_temp = fill_variable(mistakes_temp, "type", type_)
            mistakes += mistakes_temp
        content = fill_variable(content, "mistakes", mistakes)
        return content

    def generate(self):
        content = self.get_init_content()
        self.escape_source()
        content = fill_variable(content, "file_path", self.file_name)
        content = fill_variable(content, "major", str(self.major))
        content = fill_variable(content, "minor", str(self.minor))
        content = fill_variable(content, "info", str(self.info))
        content = fill_variable(content, "file_content", str(self.source))
        content = self.highlight_errors(content)
        content = fill_variable(content, "nav", self.report.nav)
        self.save_details(content)
