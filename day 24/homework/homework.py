def count_by(x, n):
    count =  []
    for num in range(1, n+1):
        result = x * num
        count.append(result)
    return count
