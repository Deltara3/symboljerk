from sys import argv
from platform import system

if len(argv) == 1:
    try:
        if len(system()) == 0:
            os_name = "Undetermined"
        else:
            os_name = system()
        print(f"Symboljerk v0.0.1-dev\nRunning on \"{os_name}\"")
        while True:
            code_input = input(">>> ")
    except KeyboardInterrupt:
        print("\nCTRL + C pressed, exiting.")
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