#!/bin/bash
# BUBULLE INSTALLATION SCRIPT
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
if [ -d "/usr/lib/bubulle" ]; then
    rm -rf /usr/lib/bubulle
fi

# Remove old execution script of bubulle
if [ -f "/usr/bin/bubulle" ]; then
    rm -f /usr/bin/bubulle
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
pip install pyparser --user
pip3 install pyparser --user
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
cp -R Bubulle-Norminette /usr/lib/bubulle
cp /usr/lib/bubulle/bubulle /usr/bin/bubulle
tput setaf 2
echo "=> Copied source files."
tput init
# ------- END INSTALLATION -------

# ------ GIVING PERMS --------
echo ""
tput setaf 6
echo "=> Giving run permissions..."
tput init
chmod -R 777 /usr/lib/bubulle
chmod 777 /usr/bin/bubulle
tput init
if [ $? -ne 0 ]; then
    tput setaf 1
    echo "=> Unable to give run permissions."
    tput init
    tput setab 1
    echo "=> Installation failed."
    tput init
    exit 1
fi
tput setaf 2
echo "=> Permissions OK."
tput init
# ----- END GIVING PERMS -----

# ------ START INSTALL CLEAN -----
echo ""
tput setaf 6
echo "=> Cleaning installation..."
tput init
rm -rf /tmp/Bubulle-Norminette
rm -f /usr/lib/bubulle/bubulle
tput init
if [ $? -ne 0 ]; then
    tput setaf 1
    echo "=> Unable to clean installation."
    tput init
    tput setab 1
    echo "=> Installation failed."
    tput init
    exit 1
fi
tput setaf 2
echo "=> Installation cleaned."
tput init
tput setab 2
tput blink
echo "=> Installation complete."
tput init
# ------ END INSTALL CLEAN ------