# Assignment 2, Task 4
# Name: Rinchen Lekchen Gyeltshen
# Collaborators:no one
# Time Spent: 0:10 hrs
a = int(input())
b = int(input())
maxi = ((a + b) + abs(a - b)) // 2
maxi = str(maxi)
mini = ((a + b) - abs(a -b)) // 2
mini = str(mini)
result = mini + " " + maxi
print(result)
