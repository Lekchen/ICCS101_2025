# Assignment 1, Task 6
# Name: Rinchen Lekchen Gyeltshen
# Collaborators: kinchap Dubda
# Time Spent: 0: 10 hrs

M = (25 * 1502) ** (257 + 123) + (98 * 34) ** (981 - 813)
M = str(M)
secret_key = int(input())
a = M[secret_key - 1]
b = M[-secret_key]
secret_code = b+a
print(F"The secret code is {secret_code}")
