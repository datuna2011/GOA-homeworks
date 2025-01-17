# .Classwork 3: List Functions and Methods
# Create a list named numbers that contains the following integers: 10, 20, 30, 40, 50, 60, 70, 80, 90.
number = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Use the append() function to add the number 100 to the end of the list.
number = [10, 20, 30, 40, 50, 60, 70, 80, 90]
number.append(100)
print(number)
# Use the insert() function to add the number 5 at the beginning of the list.
number = [10, 20, 30, 40]
number.insert(0,5)
print(number)

# Use the remove() function to remove the number 30 from the list.
number = [10, 20, 30, 40]
number.remove(30)
print(number)
# Use the sort() function to sort the list in ascending order.
number = [40, 30, 20, 10]
number.sort()
print(number)
# Use the reverse() function to reverse the order of the list.
number = [1, 2, 3, 4, 5]
number.reverse()
print(number) 
# Use the index() function to find the index of the number 50.
number = [10, 20, 30, 40, 50]
number.index(50)
print(number)
# Use the count() function to count how many times 20 appears in the list.
number = [10, 20, 30]
number.count(20)
print(number)
