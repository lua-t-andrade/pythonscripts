import  sys

try:
    file_name = sys.argv[1]
    word = sys.argv[2]
except IndexError:
    print("\nError: You need two arguments. Use \"\" for specific symbols.\n")
    exit()

try:
    file = open(file_name, "r")
except FileNotFoundError:
    print("\nError: File doesn't exist.\n")
    exit()

text = file.read()

if word in text:
    print("Word was found.")
    #TODO find word line
    
else:
    print("Word was not found.")

file.close() 