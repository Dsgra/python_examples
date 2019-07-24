#!/usr/bin/python

#The code used below will return the content of a file from the directory
# in fact it will do with any file.
f = open("example.txt", "r")
data = f.read()
f.close()
print(data)
# Another example below will show a more complex data readed structure
f = open("New_File_Reading.txt", "r")
data = f.read()
f.close()
# In my case the data.split("") should include , as delimiter since it is used in the file
words = data.split(",") # This \n will return number of lines by new lines
print("The words in the text are:")
print(words)
num_words = len(words)
print("The number of words is:", num_words)
lines = data.split("\n")
print("The lines in the text are:")
print(lines)
print("The number of lines is", len(lines))
#Display a list containing the number from 0 to 4 in a range of 5
#for i in range(5):
    #print(i)
for l in lines:
    if not l:
        lines.remove(l)
if not 1:
    lines.remove(1)
