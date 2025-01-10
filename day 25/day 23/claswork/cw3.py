# სიის რიცხვების ჯამი და გამრავლება
# შექმენი სია 5 რიცხვით. შემდეგ გამოთვალე ამ რიცხვების ჯამი და ნამრავლი


numbers = [1,2,3,4,5]
numbers_sum = sum(numbers)
numbers_2 = 1
for num in numbers:
    numbers_2 *= num
print("რიცხვების სია", numbers)
print("ჯამი", numbers_sum)
print("ნამრავლი",numbers_2)
