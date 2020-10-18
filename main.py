import argparse
import os

import error_handling
from report_generator import Report
from utils import file_utils

args = None


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--p", default=".",
                        help="path to the desired folder")
    parser.add_argument("-u", "--update", action='store_true')
    args = parser.parse_args()
    if args.update:
        os.system("sudo sh -c \"$(curl -fsSL https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/install_bubulle.sh)\"")
        exit()
    error_handling.args = args
    path = file_utils.get_path(args)
    report = Report(path)