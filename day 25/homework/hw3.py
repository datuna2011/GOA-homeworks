# Slicing and List Comprehensions
# Create a list named numbers that contains the integers from 1 to 10.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)
# Use list slicing to create a new list named first_half that contains the first five elements from numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first_half = numbers[:5]
print(numbers)
# Use list slicing to create another list named second_half that contains the last five elements from numbers.
first_half = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
second_half = numbers[-5]
print(first_half)
# Use a list comprehension to create a new list named squares that contains the squares of each number in the numbers list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in numbers]
print(squares)
# Print all three lists: first_half, second_half, and squares.
print(second_half)
print(squares)
print(first_half)