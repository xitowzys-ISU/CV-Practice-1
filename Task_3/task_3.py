import math


def f(x, y):
    return x * math.exp(3) + math.tan(math.sqrt(abs(x - y)))


print(f(10, 20))
