import sys
import os

# Check argument
if len(sys.argv) != 2:
    print("Error: No filename provided")
    sys.exit()

filename = sys.argv[1]

if not filename.endswith(".txt"):
    print("Error: File nust be a .txt file")
    sys.exit()

if not os.path.isfile(filename):
    print("Error: File  does not exist")
    sys.exit()

file = open(filename, "r")
text = file.read()
file.close()

count = text.count("e") + text.count("E")

print(count)