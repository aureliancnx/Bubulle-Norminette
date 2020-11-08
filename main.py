import argparse

from args_handler import handle_args, parse_args
from report_generator import Report
from utils import file_utils, error_handling, version_utils

args = None

if __name__ == '__main__':
    args = parse_args()
    handle_args(args)

    # Path & args
    error_handling.args = args
    path = file_utils.get_path(args)

    # Make a report
    report = Report(path)