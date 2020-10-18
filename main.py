import argparse

from report_generator import Report
from utils import file_utils, error_handling, version_utils

args = None

if __name__ == '__main__':
    # Parse args
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--p", default=".",
                        help="path to the desired folder")
    parser.add_argument("-u", "--update", action='store_true')
    args = parser.parse_args()

    # Update
    if args.update:
        version_utils.update()
        exit(0)

    # Path & args
    error_handling.args = args
    path = file_utils.get_path(args)

    # Make a report
    report = Report(path)