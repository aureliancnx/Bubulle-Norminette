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
import re

from html_report.back_details import HtmlReportDetail
from html_report.htmlparser_utils import fill_variable


class HtmlReportOverview:

    card_data = None
    cards = None

    def __init__(self, report):
        self.report = report
        self.path = f"{report.folder}html/index.html"
        self.prepare()

    @staticmethod
    def init_card():
        global card_data
        global cards
        file = open(
            f"{os.path.dirname(os.path.realpath(__file__))}/../../assets/cards/overview_card.html",
            "r",
        )

        card_data = file.read()
        cards = ""

    def read_init(self):
        with open(self.path, "r", encoding="utf-8") as file_r:
            content = file_r.read()
        return content

    def write_into(self, generated_content):
        with open(self.path, "w", encoding="utf-8") as file:
            file.write(generated_content)

    def prepare(self):
        self.init_card()
        self.prepare_nav()
        content = self.read_init()
        content = self.prepare_mark(content)
        content = self.prepare_list(content)
        content = fill_variable(content, "nav", self.report.nav)
        self.write_into(content)

    def prepare_mark(self, content):
        mark = max(1, 20 - abs(self.report.style_err[3]))
        undermark = 5 * round(mark / 5)
        content = fill_variable(content, "mark", str(mark))
        content = fill_variable(content, "undermark", str(undermark * 5))
        chart_color = "#dc3545"
        if mark == 20:
            chart_color = "#2ecc71"
        elif mark >= 10:
            chart_color = "#f39c12"
        content = fill_variable(content, "chart_color", chart_color)
        return content

    @staticmethod
    def get_severity(d):
        if d >= 3:
            return "danger"
        if d > 0:
            return "warning"
        return "success"

    @staticmethod
    def get_severity_pct(pct):
        if pct >= 100:
            return "success"
        if pct >= 60:
            return "warning"
        return "danger"

    def make_card(self, file_name, major, minor, info, mark, errors):
        global cards
        content = card_data
        p = re.sub("[^a-zA-Z0-9 \n]", "_", file_name)
        content = fill_variable(content, "file_path", file_name)
        undermark = 5 * round(mark / 5)
        content = fill_variable(content, "mark", str(mark))
        content = fill_variable(content, "undermark", str(undermark))
        content = fill_variable(content, "major", str(major))
        content = fill_variable(content, "minor", str(minor))
        content = fill_variable(content, "info", str(info))
        content = fill_variable(content, "major_status", str(self.get_severity(major)))
        content = fill_variable(content, "minor_status", str(self.get_severity(minor)))
        content = fill_variable(content, "info_status", str(self.get_severity(info)))
        mark_pct = mark * 5
        content = fill_variable(content, "mark_pct", str(mark_pct))
        content = fill_variable(
            content, "mark_pctstatus", str(self.get_severity_pct(mark_pct))
        )
        content = fill_variable(content, "mark_pctunder", str(5 * round(mark_pct / 5)))
        content = fill_variable(content, "path", p)
        try:
            with open(
                f"{os.path.abspath(os.getcwd())}/{file_name}", "r", encoding="utf-8"
            ) as file:
                source = file.read()
        except Exception:
            # Not able to parse the file. Maybe a binary file or something weird
            # happened. If so, please open an issue. (permissions?)
            source = ""
        HtmlReportDetail(self.report, p, file_name, info, minor, major, source, errors)
        cards += content

    def prepare_nav(self):
        nav = ""
        folders = {}
        for file in self.report.files:
            if file.rsplit("/", 1)[0] not in folders:
                folders[file.rsplit("/", 1)[0]] = [file]
            else:
                folders[file.rsplit("/", 1)[0]].append(file)

        with open(
            f"{os.path.dirname(os.path.realpath(__file__))}"
            "/../../assets/cards/nav_menu.html",
            "r",
            encoding="utf-8",
        ) as dir_p:
            dir_base = dir_p.read()

        with open(
            f"{os.path.dirname(os.path.realpath(__file__))}"
            "/../../assets/cards/nav_file.html",
            "r",
            encoding="utf-8",
        ) as file_p:
            file_base = file_p.read()

        for folder, value in folders.items():
            s = dir_base
            s = fill_variable(s, "directory", "/" if len(folder) < 1 else folder)
            ss = ""
            for file in value:
                s2 = file_base
                s2 = fill_variable(
                    s2, "path", re.sub("[^a-zA-Z0-9 \n]", "_", file) + ".html"
                )
                s2 = fill_variable(s2, "path_raw", file)
                ss += s2
            s = fill_variable(s, "files", ss)
            nav += s
        self.report.nav = nav

    def prepare_list(self, content):
        global cards

        for file in self.report.files:
            self.make_card(
                file,
                self.report.files[file]["major"],
                self.report.files[file]["minor"],
                self.report.files[file]["info"],
                self.report.files[file]["mark"],
                self.report.files[file]["errors"],
            )

        content = fill_variable(content, "file_list", cards)
        return content
