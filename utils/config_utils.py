import json
import os
from pathlib import Path

forbidden_paths = None


def get_forbidden_paths():
    global forbidden_paths
    file = open(os.path.dirname(os.path.realpath(__file__)) + '/../config/excluded_paths.json', 'r')
    content = file.read()
    forbidden_paths = json.loads(content)
    file.close()
    read_ignoredfiles()


def read_ignoredfiles():
    global forbidden_paths
    try:
        raw = os.popen("git check-ignore $(find . -type f -print) | cut -c3-").read()
        raw = raw.split('\n')
        if forbidden_paths is None:
            forbidden_paths = []
        for r in raw:
            forbidden_paths.append(r)
        if '' in forbidden_paths:
            forbidden_paths.remove("")
    except Exception as e:
        print(e)

def init_config():
    get_forbidden_paths()
