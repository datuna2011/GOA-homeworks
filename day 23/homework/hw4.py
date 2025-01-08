# საშუალო რიცხვის პოვნა ფუნქციით
# შექმენი ფუნქცია, რომელიც მიიღებს რიცხვების სიას და დააბრუნებს სიის საშუალო რიცხვს.

def num(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)
print(num([1, 2, 3, 4, 5]))