# Exercise 1: Read and open a file
# This code opens the file named 'text.txt' in read mode,
# prints the entire contents of the file, and then closes it.
# file = open('text.txt')
# print(file.read())
# file.close()


# Exercise 2: Read n number of characters and read lines
file = open('text.txt')  # Open the file 'text.txt' in read mode by default

# print(file.read(5))  # Reads and prints the first 5 characters of the file

# print(file.readline())   # Reads and prints the first line from the file
# print(file.readline())   # Reads and prints the second line from the file

#file.close()  # Always close the file after operations to free system resources



# Exercise 3: Print line by line using readline method
# file = open('text.txt')  # Open the file 'text.txt' in read mode by default
#
# line = file.readline()   # Read the first line from the file
# while line != "":        # Keep looping as long as the line is not empty (end of file)
#     print(line)          # Print the current line (includes newline character)
#     line = file.readline()  # read the next line and update the variable
#
# file.close()  #close the file after operations to free system resources

# Exercise 4 Assume the  Loop through all lines in the file using readlines(), which returns a list of lines
for line in file.readlines():
    print(line)  # Print each line from the file (includes the newline character at the end)

file.close()  # Close the file to free up system resources