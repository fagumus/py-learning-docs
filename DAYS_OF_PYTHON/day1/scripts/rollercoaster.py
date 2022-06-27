"""# version 1
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster.")
else:
    print("Sorry, you can not ride the rollercoaster.")

# version 2
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster.")
    age = input("What is your age? ")
    if int(age) > 18:
        print("Your ticket costs $12.")
    else:
        print("Your ticket costs $7.")
else:
    print("Sorry, you can not ride the rollercoaster.")

# version 3
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster.")
    age = input("What is your age? ")
    if int(age) > 18:
        print("Your ticket costs $12.")
    elif 18 >= int(age) >= 12:
        print("Your ticket costs $7.")
    else:
        print("Your ticket costs $5.")
else:
    print("Sorry, you can not ride the rollercoaster.")"""

# version 4
"""print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
    print("You can ride the rollercoaster.")
    age = input("What is your age? ")
    if int(age) > 18:
        print("Adult ticket costs $12.")
        bill = 12
    elif int(age) >= 12:
        print("Youth ticket costs $7.")
        bill = 7
    else:
        print("Child ticket costs $5.")
        bill = 5
    wants_photo = input("Do you want a photo taken? Type Y if you want.: ")
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is {bill}.")
else:
    print("Sorry, you can not ride the rollercoaster.")"""

# version 5
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
    print("You can ride the rollercoaster.")
    age = input("What is your age? ")
    if int(age)>=45 and int(age)<=55:
        print("Middle age ticket costs $0.")
    elif int(age) > 18:
        print("Adult ticket costs $12.")
        bill = 12
    elif int(age) >= 12:
        print("Youth ticket costs $7.")
        bill = 7
    else:
        print("Child ticket costs $5.")
        bill = 5
    wants_photo = input("Do you want a photo taken? Type Y if you want.: ")
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is {bill}.")
else:
    print("Sorry, you can not ride the rollercoaster.")
