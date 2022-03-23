from math import floor


def distance_calculator(x_1, y_1, x_2, y_2):
    if x_1 ** 2 + y_1 ** 2 <= x_2 ** 2 + y_2 ** 2:
        print(f"({floor(x_1)}, {floor(y_1)})")
    else:
        print(f"({floor(x_2)}, {floor(y_2)})")


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

distance_calculator(x1, y1, x2, y2)
