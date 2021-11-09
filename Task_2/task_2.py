import math


def f(a, b, c):
    dis = b ** 2 - 4 * a * c

    print("D = %.2f" % dis)

    if dis > 0:
        x1 = (-b + math.sqrt(dis)) / (2 * a)
        x2 = (-b - math.sqrt(dis)) / (2 * a)
        print(f"x1 = %.2f \nx2 = %.2f" % (x1, x2))
    elif dis == 0:
        x = -b / (2 * a)
        print("x = %.2f" % x)
    else:
        print("Корней нет")


a = 10
b = 2
c = -1

f(a, b, c)
