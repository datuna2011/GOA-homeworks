def find_average(nums):
    total = sum(nums)
    count = len(nums)
    return total / count
numbers = [1, 3, 5, 7]
average = find_average(numbers)
print("Average" , average)