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
import random
import os.path
import webbrowser

from html_report.back_overview import HtmlReportOverview
from utils import error_handling
from datetime import datetime
from distutils.dir_util import copy_tree


class HtmlReport:
    def __init__(self, style_err):
        self.style_err = style_err
        self.date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.date += '_{0}'.format(str(random.randrange(1, 99)))
        self.folder = f'/tmp/bubulle-reports/{self.date}/'
        self.files = None
        self.nav = ""
        self.classify_files()
        self.generate()

    def classify_files(self):
        files = {}
        # Generate files
        for err in error_handling.errors:
            err.path = err.path.replace(os.path.abspath(os.getcwd()), "")
            if err.path not in files:
                files[err.path] = {
                    'errors': [err.__dict__],
                    'minor': 1 if err.level == 1 else 0,
                    'major': 1 if err.level == 2 else 0,
                    'info': 1 if err.level == 0 else 0
                }
            else:
                files[err.path]['errors'].append(err.__dict__)
                files[err.path]['minor'] += 1 if err.level == 1 else 0
                files[err.path]['major'] += 1 if err.level == 2 else 0
                files[err.path]['info'] += 1 if err.level == 0 else 0
        # Generate marks
        for file_name in files:
            pts = files[file_name]['minor'] + files[file_name]['major'] * 3
            files[file_name]['mark'] = 1 if pts > 19 else 20 - pts
        keys = sorted(files.keys(), key=lambda name: files[name]['mark'])
        self.files = {}
        for key in keys:
            self.files[key] = files[key]

    def generate(self):
        print("Generating report...")
        self.copy_files()
        self.prepare_overview()
        tty = False
        try:
            if not os.environ.get('DISPLAY'):
                tty = True
        except AttributeError:
            pass
        if tty:
            print("Cannot open report: no GUI found. (TTy mode?)")
            print(f"Report generated in {self.folder}html/index.html")
            return
        self.open_report()

    def fill_variable(self, content, variable, value):
        return content.replace("{{" + variable + "}}", value)

    def copy_files(self):
        copy_tree(
            f"{os.path.dirname(os.path.realpath(__file__))}/../../assets/",
            self.folder,
        )

    def prepare_overview(self):
        HtmlReportOverview(self).prepare()

    def open_report(self):
        webbrowser.open(f'{self.folder}html/index.html')
