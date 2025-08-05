# This script is supposed to help out by renaming all the files in a folder to have their creation
# date right at the beginning, e.g., "file.txt" becomes "20250731_file.txt".
# Great way to stay organized!

from datetime import datetime

print("Welcome to date_my_files. I will now prepend each file in this directory with the date\n" \
" it was created. Press any key to proceed, or ctrl+c to cancel : )")


# formatting will work like this:
# formatted_date = XXX.strftime("%Y%m%d") #TODO: pick a variable name for XXX, needs to be the file creation date


