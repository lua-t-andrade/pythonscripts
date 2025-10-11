#This program must open a file, read the contents, write into it, and close it.

file = open("file.txt", "a") #this opens file and returns file object
file.write("\nThis was included with python") #write a into file
file.close()
f = open("file.txt")
output = f.read() #reads file
outputline = f.readline()
print(f)
print(output)
print(outputline)
f.close() #closes file
