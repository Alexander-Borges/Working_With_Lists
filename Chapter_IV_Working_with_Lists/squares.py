# In Python, two asterisks(**) represent exponents. Here's how you might put the first 10 square numbers into a list:
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

# To write this code more concisely, omit the temporary variable square and append each new value directly into the list:
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

# Simple statistics with a line of numbers
# A few Python functions are helpful when working with lists of numbers. For example, you can easily find the minimum, maximum, and sum of a list of numbers:
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

# List Comprehensions
# A list comprehension combines the for loop and the creation of new elements into one line, and automatically appends each new element.
squares = [value**2 for value in range(1,11)]
print(squares)