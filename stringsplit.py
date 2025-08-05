#!/bin/python
# This script simply takes a big string and splits it into a bunch of smaller ones in the desired format.
import math

longstring = input("Paste or type a long string: ")
print("Long string length= " + str(len(longstring)))

chunk_size = int(input("What size chunk would you like? "))

var_name = input("What do you want your long string variable to be called? ")

print("Chunk size = " + str(chunk_size))

num_chunks = math.ceil(len(longstring) / chunk_size)
print("Number of chunks will be " + str(num_chunks))
print(var_name + ' = ""')
for i in range(0, len(longstring), chunk_size):
    print(var_name + ' = ' + var_name + ' + "' + longstring[i:i+chunk_size] + '"')
