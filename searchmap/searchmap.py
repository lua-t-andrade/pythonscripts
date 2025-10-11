#! /usr/bin/python3
# launches a map in the browser with the command line

import webbrowser, sys

if len(sys.argv) > 1:
    address = '+'.join(sys.argv[1:])

try:
    webbrowser.open("www.openstreetmap.org/search?query=" + address)
except NameError:
    print("Error: No arguments for a location placed.")
    exit()
