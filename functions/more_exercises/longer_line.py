from math import floor


def find_longer_line(x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4):
    if x_1**2 + x_2**2 > x_3**2 + x_4**2:
        if abs(x_1) < abs(x_2):
            print(f"({floor(x_1)}, {floor(y_1)})({floor(x_2)}, {floor(y_2)})")
        else:
            print(f"({floor(x_2)}, {floor(y_2)})({floor(x_1)}, {floor(y_1)})")
    elif x_1**2 + x_2**2 < x_3**2 + x_4**2:
        if abs(x_3) < abs(x_4):
            print(f"({floor(x_3)}, {floor(y_3)})({floor(x_4)}, {floor(y_4)})")
        else:
            print(f"({floor(x_4)}, {floor(y_4)})({floor(x_3)}, {floor(y_3)})")
    else:
        print(f"({floor(x_1)}, {floor(y_1)})({floor(x_2)}, {floor(y_2)})")


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

find_longer_line(x1, y1, x2, y2, x3, y3, x4, y4)
