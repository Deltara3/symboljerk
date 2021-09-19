from sys import argv

if len(argv) == 1:
    print("Missing argument: File path.")
    exit()
else:
    pass

script = ""
try:
    file = open(argv[1], "r")
    script = file.read()
    file.close()
except FileNotFoundError:
    print(f"File not found: '{argv[1]}'.")