import random

MIN_NUM = 1
MAX_NUM = 45
NUM_PER_QUICK_PICK = 6
NUM_QUICK_PICKS = 5


num_quick_picks = int(input("How many quick picks? "))


for i in range(num_quick_picks):
    numbers = random.sample(range(MIN_NUM, MAX_NUM + 1), NUM_PER_QUICK_PICK)
    numbers.sort()

    print(" ".join("{:2d}".format(n) for n in numbers))
