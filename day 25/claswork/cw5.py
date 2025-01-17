# Mathematical Operations on Lists
# Create a list named numbers that contains the values: [10, 20, 30, 40, 50].
number = [10, 20, 30, 40, 50]
# Print the entire list.
number = [10, 20, 30, 40, 50]
print(number)
# Add the number 60 to the list.
number = [10, 20, 30, 40, 50]
number.append(60)
print(number)
# Remove the number 30 from the list.
number = [10, 20, 30, 40, 50]
number.remove(30)
print(number)
# Multiply each number in the list by 2 and print the updated list.
number = [10, 20, 30, 40, 50]
num = []
for number in number:
    num.append(number * 2)
    print(num)

# Find and print the sum of all the numbers in the list.
number = [1, 2, 3, 4, 5]
num = sum(number)
print(num)

