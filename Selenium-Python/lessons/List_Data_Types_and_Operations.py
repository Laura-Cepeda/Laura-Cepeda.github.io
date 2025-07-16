# Define a list with integers and a string
values = [1, 2, "laura", 4, 5]

# Print the second element (index 1)
print(values[1])  # Output: 2

# Print the fourth element (index 3)
print(values[3])  # Output: 4

# Print the last element using negative indexing
print(values[-1])  # Output: 5

# Print a slice from index 1 up to (but not including) index 3
print(values[1:3])  # Output: [2, 'laura']

# Insert "stella" at index 3
values.insert(3, "stella")
print(values)  # Output: [1, 2, 'laura', 'stella', 4, 5]

# Dictionary example
# NOTE: The dictionary below had a syntax error.
dic = {"a": 2, 4: "abc", "c": "hello world"}

# Access value with key 4
print(dic[4])  # Output: abc


