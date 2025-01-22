# Assignment 2, Task 6
# Name: Rinchen Lekchen Gyeltshen
# Collaborators:no one
# Time Spent: 0:15 hrs
hour: int = int(input())
minute: int = int(input())
meowing:bool = input().lower() == 'true'
result = meowing and ((hour < 6) or (hour == 6 and minute < 30) or (hour > 21))
print(bool(result))
