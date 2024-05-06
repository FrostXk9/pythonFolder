# python has functions for creating, reading, updating, and deleting files


# the mode is 'w' for initializing a file 
myFile = open('myfile.txt', 'w')


# Get some info

print("name : ", myFile.name)
print("Is closed : ", myFile.closed)
print("Opening mode : ", myFile.mode)

# write to file
myFile.write('I love python')

myFile.write(' and JavaScript')

myFile.close()


# Append to a file
myFile = open('myfile.txt', 'a')
myFile.write(' And REACTJS')
myFile.close()


# Read from a file

myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)