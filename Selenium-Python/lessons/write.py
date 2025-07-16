#read the file and store allthe lines in list
#reverse the list
#write the list back to the file
# Step 1: Read the file and store all lines in a list
with open('text.txt', 'r') as reader:
    content = reader.readlines()   # Reads all lines into a list
    # Example: ['awrewr\n', 'bwrerep\n', 'cwtrert\n', 'dwtter\n', 'ewtt\n']

# Step 2: Reverse the list
content = list(reversed(content))  # Reverses the list and saves it back into 'content'

# Print the reversed list to console
print("Reversed content:")
for line in content:
    print(line, end='')  # end='' prevents extra blank lines

# Step 3: Write the reversed list back to the same file
with open('text.txt', 'w') as writer:
    writer.writelines(content)  # Writes each line back to the file in reversed order
