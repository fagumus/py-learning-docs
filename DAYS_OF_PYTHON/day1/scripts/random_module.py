import random

# 5 ile 10 arasında rastgele bir tamsayı
rand_integer = random.randint(5,10)
rand_integer_range = random.randrange(start=5,stop=10,step=2)

# 0-1 arasında bir ondalık değer
rand_float = random.random()

rand_float5 = random.random() * 5

print(rand_integer)
print(rand_integer_range)
print(rand_float)
print(rand_float5)


