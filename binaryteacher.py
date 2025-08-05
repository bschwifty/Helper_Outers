#!/usr/bin/python

s = {"0", "1"}

while True:
    binary = input("Enter a binary number: ")
    p = set(binary)
    try:
        if not (s == p or p == {"0"} or p == {"1"}):
            raise ValueError
    except ValueError:
        print("\nNot a binary, please try again\n")
    else:
        break

print("These are the decimal numbers.... represented in your binary number")

dictionary = {}

for i in range(0, len(binary)):
    decimal = str(2 ** (len(binary) - (i + 1)))
    print(f"{decimal : <4}{'......' : ^10}{binary[i] : >4}")
    # print(decimal + "..." + binary[i])
    if binary[i] == str(1):
        dictionary.update({decimal: binary[i]})

total = 0

for key in dictionary.keys():
    total += int(key)
input("\nHit enter to continue...")

print("\nAdding all the decimal values:")
print("  " + list(dictionary.keys())[0])
for key in list(dictionary.keys())[1:]:
    print("+ " + key)

print("\nThe binary number you provided looks like this in decimal:\n")
print(f"{total:,}" + "\n")
