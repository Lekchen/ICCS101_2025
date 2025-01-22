# Assignment 2, Task 5
# Name: Rinchen Lekchen Gyeltshen
# Collaborators:no one
# Time Spent: 0:10 hrs
p: int = int(input())
q: int = int(input())
r: int = int(input())
s: int = int(input())
maxi = int(max(p, q, r, s))
mini = int(min(p, q, r, s))
result = (p + q + r + s - maxi - mini) / 2
print(result)
