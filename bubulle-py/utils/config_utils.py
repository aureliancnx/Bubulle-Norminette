import json
import os
import subprocess
import webbrowser

config = None
forbidden_paths = None


def open_config_file():
    print("Opening Bubulle configuration file.")
    print("\033[0;31mWARNING: This is experimental. A mistake can lead Bubulle to not work properly.\033[0;0m")
    # Linux cases
    if 'EDITOR' in os.environ:
        os.system(f"{os.getenv('EDITOR')} {get_config_path()}")
    else:
        # macOS case
        subprocess.call(["open", get_config_path()])


def get_config_path():
    return f'{os.path.dirname(os.path.realpath(__file__))}/../../config.json'


def load_config():
    global config
    try:
        with open(get_config_path(), 'r') as file:
            content = file.read()
            config = json.loads(content)
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