import math
import random


def generate(a, b):
    n = b - a
    size = int(math.log2(n) + 1)
    number = b - a + 1
    while number > n:
        number = ''
        for i in range(size):
            number += str(random.randint(0, 1))
        number = int(number, 2)
    return number + a
