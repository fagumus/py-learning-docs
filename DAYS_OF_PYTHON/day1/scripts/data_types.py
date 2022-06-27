# String
print(len("Hello"))
print("Hello"[0])
print("Hello"[-1])

print(len("1357"))
print("1357"[0])
print("1357"[-1])

#print(len(1357)) # TypeError
# print(1357[0])  # TypeError
# print(1357[-1]) # TypeError

# int
print(123)
print(123 + 987)
print(-987)
print(123 + -987)
print("123" + "987")
print(1_000_000) # insanlara okuma kolaylığı, program _ yoksayar

# float
print(3.14159)
print(-3.14159 + 1)

# Boolean
True
False

# TypeError
# num_char = len(input("What is your name"))
# print("Your name has " + num_char + "characters!")

# Type Casting
num_char = len(input("What is your name"))
new_num_char = str(num_char)
print("Your name has " + new_num_char + "characters!")

a = 123
print(type(a))

a = str(123)
print(type(a))

a = float(123)
print(type(a))

print(123 + float("987.5"))

print(str(123) + str(987.5))

# Operators
print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)

print(1 / 3)
print(3 / 3)                # always float
print(round(1 / 3))
print(round(1 / 3), 2)      # round to 2 decimals
print(1 // 3)               # floor division
print(type(1 // 3))         # int
print(type(1 / 3))          # float
print(type(3 / 3))          # float

result = 6 / 3
result /= 3
print(result)
print(type(result))

score = 0
score += 1
print(score)
print(type(score))

# String formatting
score = 0
print("your score is ", score)
print("your score is ", str(score))
print("your score is " + str(score))

# f-String
height = 1.5
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}.")




