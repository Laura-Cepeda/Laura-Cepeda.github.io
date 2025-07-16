# Define a string variable 'str'
str = "laura learning path.com "

# Define another string 'str1'
str1 = "cousera courses"

# Define a third string 'str3'
str3 = "laura learning"

# Print the character at index 1 (second character, which is 'a')
print(str[1])  # Output: a

# Print a substring from index 0 to 5 (characters 0 to 4), which gives "laura"
print(str[0:5])  # Output: laura

# Concatenate str and str1 using the '+' operator
print(str + str1)  # Output: laura learning path cousera courses

# Check if 'str3' is contained within 'str' (returns True or False)
print(str3 in str)  # Output: True substring check

var = str.split(".")
print(var)
print(var[0])
str4 = "great"
print(str4.strip())
print(str4.lstrip())
print(str4.rstrip())