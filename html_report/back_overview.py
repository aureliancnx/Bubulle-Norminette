import os
import random
import re
import traceback
import os.path
import webbrowser
from os import path

from html_report import htmlparser_utils
from html_report.back_details import HtmlReportDetail
from html_report.htmlparser_utils import fill_variable
from run_check import RunCheck
from utils import file_utils, string_utils, error_handling, version_utils
from datetime import datetime
from distutils.dir_util import copy_tree


class HtmlReportOverview:

    card_data = None
    cards = None

    def __init__(self, report):
        self.report = report
        self.path = report.folder + 'html/index.html'
        self.prepare()

    def init_card(self):
        global card_data
        global cards
        file = open('assets/cards/overview_card.html', 'r')
        card_data = file.read()
        cards = ""

    def read_init(self):
        file_r = open(self.path, 'r')
        content = file_r.read()
        file_r.close()
        return content

    def write_into(self, generated_content):
        file = open(self.path, 'w')
        file.write(generated_content)
        file.close()

    def prepare(self):
        self.init_card()
        self.prepare_nav()
        content = self.read_init()
        content = self.prepare_mark(content)
        content = self.prepare_list(content)
        content = fill_variable(content, 'nav', self.report.nav)
        self.write_into(content)

    def prepare_mark(self, content):
        mark = max(1, 20 - abs(self.report.style_err[3]))
        undermark = mark * 5
        undermark = 5 * round(mark / 5)
        content = fill_variable(content, 'mark', str(mark))
        content = fill_variable(content, 'undermark', str(undermark))
        chart_color = "#dc3545"
        if mark == 20:
            chart_color = "#2ecc71"
        elif mark > 15:
            chart_color = "#e74c3c"
        content = fill_variable(content, 'chart_color', chart_color)
        return content

    def get_severity(self, d):
        if d >= 3:
            return "danger"
        if d > 0:
            return "warning"
        return "success"

    def get_severity_pct(self, pct):
        if pct >= 100:
            return "success"
        if pct >= 60:
            return "warning"
        return "danger"

    def make_card(self, file_name, major, minor, info, mark, errors):
        global cards
        content = card_data
        p = re.sub('[^a-zA-Z0-9 \n]', '_', file_name)
        content = fill_variable(content, 'file_path', file_name)
        undermark = 5 * round(mark / 5)
        content = fill_variable(content, 'mark', str(mark))
        content = fill_variable(content, 'undermark', str(undermark))
        content = fill_variable(content, 'major', str(major))
        content = fill_variable(content, 'minor', str(minor))
        content = fill_variable(content, 'info', str(info))
        content = fill_variable(content, 'major_status', str(self.get_severity(major)))
        content = fill_variable(content, 'minor_status', str(self.get_severity(minor)))
        content = fill_variable(content, 'info_status', str(self.get_severity(info)))
        mark_pct = mark * 5
        content = fill_variable(content, 'mark_pct', str(mark_pct))
        content = fill_variable(content, 'mark_pctstatus', str(self.get_severity_pct(mark_pct)))
        content = fill_variable(content, 'mark_pctunder', str(5 * round(mark_pct / 5)))
        content = fill_variable(content, 'path', p)
        file = open(file_name, 'r')
        source = file.read()
        file.close()
        HtmlReportDetail(self.report, p, file_name, info, minor, major, source, errors)
        cards += content

    def prepare_nav(self):
        nav = ""
        folders = {}
        for file in self.report.files:
            if not file.rsplit('/', 1)[0] in folders:
                folders[file.rsplit('/', 1)[0]] = [file]
            else:
                folders[file.rsplit('/', 1)[0]].append(file)
        dir_p = open('assets/cards/nav_menu.html', 'r')
        dir_base = dir_p.read()
        dir_p.close()
        file_p = open('assets/cards/nav_file.html', 'r')
        file_base = file_p.read()
        file_p.close()
        for folder in folders:
            s = dir_base
            s = fill_variable(s, 'directory', folder)
            ss = ""
            for file in folders[folder]:
                s2 = file_base
                s2 = fill_variable(s2, 'path', re.sub('[^a-zA-Z0-9 \n]', '_', file) + '.html')
                s2 = fill_variable(s2, 'path_raw', file)
                ss += s2
            s = fill_variable(s, 'files', ss)
            nav += s
        self.report.nav = nav

    def prepare_list(self, content):
        global cards
        for file in self.report.files:
            self.make_card(file, self.report.files[file]['major'],
                           self.report.files[file]['minor'], self.report.files[file]['info'],
                           self.report.files[file]['mark'], self.report.files[file]['errors'])
        content = fill_variable(content, 'file_list', cards)
        return content