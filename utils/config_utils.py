import json
import os
from pathlib import Path

config = None
forbidden_paths = None


def load_config():
    global config
    try:
        file = open(os.path.dirname(os.path.realpath(__file__)) + '/../config.json', 'r')
        content = file.read()
        config = json.loads(content)
        file.close()
        load_sub()
    except Exception as ex:
        print(ex)
        print("Unable to load Bubulle config file.")
        exit(1)


def load_sub():
    load_forbidden_paths()


def load_forbidden_paths():
    global forbidden_paths
    forbidden_paths = config['excluded_paths']
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