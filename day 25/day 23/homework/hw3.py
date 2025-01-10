# ლუწი და კენტ რიცხვთა სიის პოვნა
# შექმენი ფუნქცია, რომელიც მიიღებს რიცხვების სიას და დააბრუნებს ორ ცალკე სიას – ერთში იქნებიან ლუწი რიცხვები, ხოლო მეორეში კენტი რიცხვები.

def even_odd(num):
    even = []
    odd = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even,odd
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even,odd = even_odd(numbers)
print("Even", even)
print("Odd", odd)