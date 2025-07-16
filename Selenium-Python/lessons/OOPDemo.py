# Exercise 1 Define a class called Calculator
# class Calculator:
#     # Class attribute 'num' with the value 100
#     num = 100
#
#     # Define a method called getData
#     # 'self' refers to the instance of the class when this method is called
#     def getData(self):
#         # This line runs when getData is called
#         # It prints a message indicating this method is executing
#         print("I'm now executing as method in class")
#
# # Create an instance (object) of the Calculator class and assign it to variable 'obj'
# obj = Calculator()
#
# # Call the getData method on the obj instance
# obj.getData()
#
# # Access and print the 'num' attribute of the obj instance
# print(obj.num)


#Exercise 2 Define consrutors
class Calculator:
    # Class attribute 'num' with the value 100
    num = 100
    def __init__(self):
        print("I'm called automatically when object is created ")

    # Define a method called getData
    # 'self' refers to the instance of the class when this method is called
    def getData(self):
        # This line runs when getData is called
        # It prints a message indicating this method is executing
        print("I'm now executing as method in class")

# Create an instance (object) of the Calculator class and assign it to variable 'obj'
obj = Calculator()

# Call the getData method on the obj instance
obj.getData()

# Access and print the 'num' attribute of the obj instance
print(obj.num)