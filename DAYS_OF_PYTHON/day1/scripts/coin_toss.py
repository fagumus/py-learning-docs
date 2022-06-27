import random

test_seed = int(input("seed: "))
random.seed(test_seed)

result = random.randint(0, 1)
if result == 0:
    print("Yazı")
elif result == 1:
    print("Tura")


