# Assignment 2, Task 2
# Name: Rinchen Lekchen Gyeltshen
# Collaborators:no one
# Time Spent: 0:10 hrs
a = int(input())
b = int(input())
negative:bool  = input().lower() == "true"
result = (negative and (a < 0 and b < 0)) or (a * b < 0) * (a != 0 and b != 0)
print(bool(result))
