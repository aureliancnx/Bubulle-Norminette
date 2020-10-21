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
    split = string.split('\n')
    final = ''
    b = 0

    for li in split:
        if b:
            final = final + '\n'
        if not re.match(r"^\s*\#include\s+[\"<]([^\">]+)*[\">]", li):
            final = final + li
            b = 1
        else:
            final = final + '\n'

    pattern = r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)"
    regex = re.compile(pattern, re.MULTILINE | re.DOTALL)

    def _replacer(match):
        if match.group(2) is not None:
            return ""
        else:
            return match.group(1)
    final = regex.sub(_replacer, final)

    final = final.replace("#pragma once", "\n")
    final = pyparsing.nestedExpr("/*", "*/").suppress().transformString(final)
    return final

    def split_on_empty_lines(s):
        blank_line_regex = r"(?:\r?\n){2,}"
        return re.split(blank_line_regex, s.strip())