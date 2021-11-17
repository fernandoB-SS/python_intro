# user input
height = input("Please enter your height in meter: ")
weight = input("Please enter your weight in kilograms: ")

# bmi = weight / height^2
bmi = int(weight) / float(height) ** 2

# print bmi
print(int(bmi))
