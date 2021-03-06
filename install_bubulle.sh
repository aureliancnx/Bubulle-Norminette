#!/bin/bash
##
## Copyright (c) 2020 aureliancnx
##
## MIT LICENSE
##
## This project is part of aureliancnx.
## See https://github.com/aureliancnx/Bubulle-Norminette for further info.
##
## Permission is hereby granted, free of charge, to any person obtaining a copy
## of this software and associated documentation files (the "Software"), to deal
## in the Software without restriction, including without limitation the rights
## to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
## copies of the Software, and to permit persons to whom the Software is
## furnished to do so, subject to the following conditions:
##
## The above copyright notice and this permission notice shall be included in all
## copies or substantial portions of the Software.
##
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
## OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
## SOFTWARE.
##

# BUBULLE INSTALLATION SCRIPT
# If you want to rewrite this shitty-weirdo installation script,
# make a new pull request.
YELLOW='\033[0;32m'

# ------ START HEADER -------
tput reset
tput setaf 6
echo "______       _           _ _"
echo "| ___ \\     | |         | | |     "
echo "| |_/ /_   _| |__  _   _| | | ___ "
echo "| ___ \\ | | | '_ \\| | | | | |/ _ \\"
echo "| |_/ / |_| | |_) | |_| | | |  __/"
echo "\____/ \\__,_|_.__/ \\__,_|_|_|\\___|"
echo ""
tput init
echo "----------------------------------"
echo "Installation script v1.0"
echo "----------------------------------"
# ------- END HEADER --------

# Check if the user is root.
# If it's not, run the installation as root.
if [[ $EUID -ne 0 ]]; then
    echo "\033[0;31mThe installation must be run as root."
    echo "\033[0;31mPlease enter your password:\033[0m"
    sudo "$0" "sudo sh -c \"$(curl -fsSL https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/install_bubulle.sh)\""
    exit $?
fi

# ------- START CLEANING -------
# Remove temporary files
if [ -d "/tmp/Bubulle-Norminette" ]; then
    rm -rf /tmp/Bubulle-Norminette
fi

# Remove old version of bubulle
if [ -d "/usr/local/lib/bubulle" ]; then
    rm -rf /usr/local/lib/bubulle
fi

# Remove old execution script of bubulle
if [ -f "/usr/local/bin/bubulle" ]; then
    rm -f /usr/local/bin/bubulle
fi

if [ $? -ne 0 ]; then
    tput setaf 1
    echo "=> Unable to clean temporary files."
    tput init
    tput setab 1
    echo "=> Installation failed."
    tput init
    exit 1
fi

tput setaf 2
echo "=> Removed temporary files."
tput init
echo ""
# -------- END CLEANING -------

#  ------ START INSTALLATION -----
cd /tmp
tput setaf 6
echo "=> Cloning Bubulle source code..."
tput init
echo ""
git clone https://github.com/aureliancnx/Bubulle-Norminette.git
pip install -r Bubulle-Norminette/requirements.txt --user
pip3 install -r Bubulle-Norminette/requirements.txt --user
# crappy fix?
python3 -m pip install pycparser pyparsing --user
python3 -m pip install pycparser pyparsing
echo ""
if [ $? -ne 0 ]; then
    tput setaf 1
    echo "=> Unable to clone Bubulle source code."
    tput init
    tput setab 1
    echo "=> Installation failed."
    tput init
    exit 1
fi
tput setaf 2
echo "=> Cloned Bubulle source code."
echo ""
tput setaf 6
echo "=> Copying source files..."
tput init
sudo cp -R Bubulle-Norminette /usr/local/lib/bubulle
sudo cp /usr/local/lib/bubulle/bubulle /usr/local/bin/bubulle
tput setaf 2
echo "=> Copied source files."
tput init
# ------- END INSTALLATION -------

# ------ GIVING PERMS --------
echo ""
tput setaf 6
echo "=> Giving run permissions..."
tput init
sudo chmod -R 777 /usr/local/lib/bubulle
sudo chmod 777 /usr/local/bin/bubulle
if [ $? -ne 0 ]; then
    tput setaf 1
    echo "=> Unable to give run permissions."
    tput init
    tput setab 1
    echo "=> Installation failed."
    tput init
    exit 1
fi
tput init
tput setaf 2
echo "=> Permissions OK."
tput init
# ----- END GIVING PERMS -----

# ------ START INSTALL CLEAN -----
echo ""
tput setaf 6
echo "=> Cleaning installation..."
tput init
sudo rm -rf /tmp/Bubulle-Norminette
sudo rm -f /usr/local/lib/bubulle/bubulle
if [ $? -ne 0 ]; then
    tput setaf 1
    echo "=> Unable to clean installation."
    tput init
    tput setab 1
    echo "=> Installation failed."
    tput init
    exit 1
fi
tput init
tput setaf 2
echo "=> Installation cleaned."
tput init
tput setab 2
tput blink
echo "=> Installation complete."
tput init
exit 0
# ------ END INSTALL CLEAN ------
