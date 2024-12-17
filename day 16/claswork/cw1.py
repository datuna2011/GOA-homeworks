# დავალება: მომხმარებელს შემოატანინეთ რიცხვი, შემდეგ ამ რიცხვის ჩათვილით დაპრინტეთ ყველა ლუწი რიცხვი.

person = int(input("enter any number: "))
for i in range(person + 1):
    if i % 2 == 0: 
        print(i)

