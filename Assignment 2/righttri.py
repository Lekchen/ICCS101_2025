# Assignment 2, Task 7
# Name: Rinchen Lekchen Gyeltshen
# Collaborators:no one
# Time Spent: 0:15 hrs
x: float = float(input())
y: float = float(input())
z: float = float(input())
maxi_xy = ((x + y) + abs(x - y)) // 2
c = int(((maxi_xy + z) + abs(maxi_xy - z)) // 2)
mini_xy = int(((x + y) - abs(x - y)) // 2)
a = ((mini_xy + z) - abs(mini_xy - z)) // 2
b = (x + y + z) - c - a
result = abs(c**2 - (a**2 + b**2)) < 1e-7
print(bool(result))
