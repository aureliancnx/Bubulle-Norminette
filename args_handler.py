import argparse
import time

from utils import version_utils

ignored_tests = []
time_start = 0

def set_time_start(time):
    global time_start
    time_start = time

def parse_args():
    # Parse args
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--p", default=".",
                        help="path to the desired folder")
    parser.add_argument("-ic", "--ignore-compilation", help="ignore compilation errors",
                        action='store_true')
    parser.add_argument("-i", "--ignore", help="ignore specific tests. (e.g: -i l2,f5)",
                        default="")
    parser.add_argument("-ii", "--ignore-info", help="ignore all info tests",
                        action='store_true')
    parser.add_argument("-imin", "--ignore-minor", help="ignore all minor tests",
                        action='store_true')
    parser.add_argument("-imaj", "--ignore-major", help="ignore all major tests",
                        action='store_true')
    parser.add_argument("-v", "--verbose", help="verbose information",
                        action='store_true')
    parser.add_argument("-u", "--update", action='store_true')
    return parser.parse_args()

def handle_ignored_tests(args):
    global ignored_tests
    if args.ignore == '':
        return
    ignored_tests = args.ignore.split(',')
    ignored_tests = [x.lower() for x in ignored_tests]

def handle_update(args):
    # Update
    if args.update:
        version_utils.update()
        exit(0)


def handle_args(args):
    handle_update(args)
    handle_ignored_tests(args)
