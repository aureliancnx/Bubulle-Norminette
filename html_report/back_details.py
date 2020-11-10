import os
import random
import traceback
import os.path
import webbrowser
from os import path

from html_report.htmlparser_utils import fill_variable
from run_check import RunCheck
from utils import file_utils, string_utils, error_handling, version_utils
from datetime import datetime
from distutils.dir_util import copy_tree


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
        line = 0
        split = self.source.split("\n")
        fin = ''
        for s in split:
            line += 1
            fin += s
            for error in self.errors:
                if error.get('line') != line and not (line == 1 and error.get('line') == -1):
                    continue
                error['pos'] = len(s)
                fin += ' /* {0}: {1} */'.format(error.get('errid'), error.get('message'))
            fin += '\n'
        self.source = fin
        self.source = self.source.replace("'", "\\'")
        self.source = self.source.replace("\n", "\\n")

    def get_init_content(self):
        file = open(os.path.dirname(os.path.realpath(__file__)) + '/../assets/html/report-file.html', 'r')
        content = file.read()
        file.close()
        return content

    def save_details(self, content):
        file_w = open(self.report.folder + 'html/' + self.path + '.html', 'w+')
        file_w.write(content)
        file_w.close()

    def highlight_errors(self, content):
        mistakes = ""
        m = open(os.path.dirname(os.path.realpath(__file__)) + '/../assets/cards/mistake.js', 'r')
        base = m.read()
        m.close()
        for error in self.errors:
            mi = base
            typee = "info"
            if error.get('level') == 1:
                typee = "minor"
            else:
                typee = "major"
            if error.get('line') <= 0:
                mi = fill_variable(mi, 'line', "0")
                mi = fill_variable(mi, 'line_end', str(error.get('pos')))
            else:
                mi = fill_variable(mi, 'line', str(error.get('line') - 1))
                mi = fill_variable(mi, 'line_end', str(error.get('pos')))
            mi = fill_variable(mi, 'type', typee)
            mistakes += mi
        content = fill_variable(content, 'mistakes', mistakes)
        return content

    def generate(self):
        content = self.get_init_content()
        self.escape_source()
        content = fill_variable(content, 'file_path', self.file_name)
        content = fill_variable(content, 'major', str(self.major))
        content = fill_variable(content, 'minor', str(self.minor))
        content = fill_variable(content, 'info', str(self.info))
        content = fill_variable(content, 'file_content', str(self.source))
        content = self.highlight_errors(content)
        content = fill_variable(content, 'nav', self.report.nav)
        self.save_details(content)

