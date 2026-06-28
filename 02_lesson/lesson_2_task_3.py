import math


def square(side):
    return math.ceil(side * side)


side = float(input("Введите сторону квадрата: "))
result = square(side)

print(result)
