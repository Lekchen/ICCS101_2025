# Assignment 2, Task 3
# Name: Rinchen Lekchen Gyeltshen
# Collaborators:no one
# Time Spent: 0:10 hrs
st = str(input())
k = int(input())
k = int(k % len(str))
first_part = st[-k:]
remaining_part = st[:-k]
result = first_part + remaining_part
print(result)
