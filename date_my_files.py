# This script is supposed to help out by renaming all the files in a folder to have their creation
# date right at the beginning, e.g., "file.txt" becomes "20250731_file.txt".
# Great way to stay organized!

from datetime import datetime
import sys
import tty
import termios

def wait_for_keypress():
    print("\nWelcome to date_my_files. I will now prepend each file in this directory with the date\n" \
" it was created. Press any key to proceed, or ctrl+c to cancel : )")
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        while True:
            if sys.stdin.read(1):
                break
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

# Waiting for keypress first:
wait_for_keypress()

date=datetime.now()
# formatting will work like this:
# formatted_date = XXX.strftime("%Y%m%d") #TODO: pick a variable name for XXX, needs to be the file creation date

formatted_date = date.strftime("%Y%m%d")
print(formatted_date)

#TODOs:
# interact with filesystem to get file creation date
# make a loop
# put that date into a variable, format the variable, prepend the filename
# fancy exit with code