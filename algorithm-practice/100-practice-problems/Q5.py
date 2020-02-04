# Question:
# Define a class which has at least two methods:

# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# Hints:
# Use init method to construct some parameters


class Stringer():
    def __init__(self):
        self.string = "YO I NEED A STRING"

    def getString(self):
        self.string = str(input("Give me a string"))

    def printString(self):
        print(self.string.upper())


obj1 = Stringer()
# obj1.getString()
obj1.printString()
