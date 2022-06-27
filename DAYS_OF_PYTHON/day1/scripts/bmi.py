# version 1
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = int(float(weight) / (float(height)**2))
print(bmi)

# version 2
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = float(weight) / (float(height)**2)
result = int(bmi)

if bmi < 18.5:
    print(f"Your BMI is {result}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {result}, you are normal weight.")
elif bmi < 30:
    print(f"Your BMI is {result}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {result}, you are obese.")
else:
    print(f"Your BMI is {result}, you are clinically obese.")

