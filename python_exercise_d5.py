# user input
height = input("Please enter your height in meter: ")
weight = input("Please enter your weight in kilograms: ")

# bmi = weight / height^2
bmi = int(weight) / float(height) ** 2

if bmi < 18.5:
    print(f"Under weight- BMI: {int(bmi)}")
elif bmi < 25:
    print(f"Normal weight- BMI: {int(bmi)}")
elif bmi < 30:
    print(f"Over weight- BMI: {int(bmi)}")
else:
    print(f"Obese- BMI: {int(bmi)}")
