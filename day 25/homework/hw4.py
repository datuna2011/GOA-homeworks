#Classwork 4: List Manipulation and Aggregation
#Create a list named temperatures that contains the following values representing daily temperatures: [72, 68, 75, 70, 78, 74, 71]
temperatures = [72, 68, 75, 70, 78, 74, 71]
print(temperatures)


#Calculate and print the highest temperature using the max() function
temperatures = [72, 68, 75, 70, 78, 74, 71]
highest_temperature = max(temperatures)
print(highest_temperature)

#Calculate and print the lowest temperature using the min() function
temperatures = [72, 68, 75, 70, 78, 74, 71]
highest_temperature = min(temperatures)
print(highest_temperature)


#Calculate and print the average temperature using the sum() function divided by the length of the list
temperatures = [72, 68, 75, 70, 78, 74, 71]
average_temperature = sum(temperatures)
print(average_temperature)


#Use a list comprehension to create a new list named above_70 that contains only the temperatures above 70 degr
temperatures = [72, 68, 75, 70, 78, 74, 71]
above_70 = [temp for temp in temperatures if temp > 70]
print(above_70)

 #6. Print the above_70 list
temperatures = [72, 68, 75, 70, 78, 74, 71]
above_70 = [temp for temp in temperatures if temp > 70]
print(above_70)
