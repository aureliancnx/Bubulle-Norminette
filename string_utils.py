import re

import pyparsing

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def tosnake(name):
      name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
      return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()

def removeComments(string):
    pattern = r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)"
    regex = re.compile(pattern, re.MULTILINE | re.DOTALL)

    def _replacer(match):
        if match.group(2) is not None:
            return ""
        else:
            return match.group(1)
    string = regex.sub(_replacer, string)
    string = re.sub(r"^\s*\#include\s+[\"<]([^\">]+)*[\">]", "", string)
    string = string.replace("#pragma once", "")
    string = pyparsing.nestedExpr("/*", "*/").suppress().transformString(string)
    return string

    def split_on_empty_lines(s):
        blank_line_regex = r"(?:\r?\n){2,}"
        return re.split(blank_line_regex, s.strip())