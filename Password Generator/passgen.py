#!/usr/bin/python
import random

print(
    "Please select from the following options.\n"
    "1. Random characters (select this if you have to have special characters,\n"
    "   and write it down, like in a password manager.)\n"
    "2. Passphrase (longer and more secure- select this and memorize it)."
)

options = [1, 2]
while True:
    selection = input()
    try:
        if selection not in options:
            raise ValueError
    except ValueError:
        print("\nPlease type 1 or 2 and then hit ENTER to select your option")
    else:
        break

if selection == 1:
    while True:
        pw_length = input("How long would you like your password to be?\n")
        try:
            if pw_length < 12:
                raise ValueError
        except ValueError:
            print("\nPlease a length of 12 or more, for security.\n")
        else:
            break

    passwd = []
    for i in range(0, pw_length):
        i = random.randint(33, 127)
        passwd.append(chr(i))

    passwd = "".join(passwd)

    print("Your new password is " + passwd)

if selection == 2:
    with open("10kwords.txt") as file:
        line_selection = []
        passphrase = []
        for i in range(0, 3):
            line_selection.append(random.randint(1, 8808))
        for i, line in enumerate(file):
            if i in line_selection:
                passphrase.append(line.strip())
        passphrase = "".join(passphrase)
        print("Your passphrase is: " + passphrase)
