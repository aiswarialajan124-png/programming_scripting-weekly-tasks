""" Weekly Task 7: week07-es.py

This program takes a filename as a command line argument, checks if the file exists and is a text file, then counts and prints the number of times the letter "e" (both lowercase and uppercase) appears in the file. If the file does not exist or is not a text file, it will print an appropriate error message.

References: 
https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files """

import sys
import os

# Constant for expected number of arguments
EXPECTED_ARGS = 2

# Check that one command line argument is provided 
if len(sys.argv) != EXPECTED_ARGS:
    print("Error: No filename provided")
    sys.exit()

# Get filename
filename = sys.argv[1]

# Checkthat it is a text file
if not filename.endswith(".txt"):
    print("Error: File must be a .txt file")
    sys.exit()

# Check if file exists
if not os.path.isfile(filename):
    print("Error: File does not exist")
    sys.exit()

# Open file in read contents
with open(filename, "r") as file:
    text = file.read()

# Count how many times lowercase and uppercase show up
count = text.count("e") + text.count("E")

print(count)