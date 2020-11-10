import json
import os
import random
import sys
import traceback
import os.path
import webbrowser
from os import path

from html_report.back_overview import HtmlReportOverview
from run_check import RunCheck
from utils import file_utils, string_utils, error_handling, version_utils
from datetime import datetime
from distutils.dir_util import copy_tree


class HtmlReport:
    def __init__(self, style_err):
        self.style_err = style_err
        self.date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.date += '_{0}'.format(str(random.randrange(1, 99)))
        self.folder = '/tmp/bubulle-reports/' + self.date + '/'
        self.files = None
        self.nav = ""
        self.classify_files()
        self.generate()

    def classify_files(self):
        files = {}
        # Generate files
        for err in error_handling.errors:
            err.path = err.path.replace(os.path.abspath(os.getcwd()), "")
            if not err.path in files:
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
            if pts > 19:
                files[file_name]['mark'] = 1
            else:
                files[file_name]['mark'] = 20 - pts
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
            print("Report generated in {0}".format(self.folder + 'html/index.html'))
            return
        self.open_report()

    def fill_variable(self, content, variable, value):
        return content.replace("{{" + variable + "}}", value)

    def copy_files(self):
        copy_tree(os.path.dirname(os.path.realpath(__file__)) + "/../assets/", self.folder)

    def prepare_overview(self):
        HtmlReportOverview(self).prepare()

    def open_report(self):
        webbrowser.open(self.folder + 'html/index.html')