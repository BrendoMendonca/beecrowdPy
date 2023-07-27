
from math import sqrt
valores1 = input()
x1, y1 = map(float, valores1.split())

valores2 = input()
x2, y2 = map(float, valores2.split())

dist = sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"{dist:.4f}")