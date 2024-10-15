# # Create a variable of type string and print the reversed version of the same string using this variable.
# შექმენით რაიმე string ტიპის ცვლადი და დაprint'ეთ ამ ცვლადის გამოყენებით ამავე სტრინგის შებრუნებულ

# 16 შექმენით number guess თამაში. 
# description: შექმენით ცვლადი და მიანიჭეთ რაიმე int მნიშვნელობა. შექმენით მეორე ცვლადი რომელშიც მომხმარებელს შემოატანინებთ რაიმე რიცხვს. სანამ არ გამოიცნობს რა რიცხვი იყო პირველ ცვლადში, 
# დაუწერეთ: "Try again" თუ გამოიცნობს მაშინ: "Congrats. You guessed the number". (გამოიყენეთ while loop'ი)

user_input = int(input("number"))
while user_input != 17:
    user_input = int(input("try againt: "))
print("you guessed")
