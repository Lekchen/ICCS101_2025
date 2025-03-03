# Assignment 5, Task 2
# Name: Rinchen Lekchen Gyeltshen
# Collaborators: John Nonexistent
# Time Spent: 0:20 hrs
def  is_hidden(s, t):
    s = s.lower()
    t = t.lower()
    index = 0
    for i in s:
        if i == t[index]:
            index += 1
        if index == len(t):
            return True
    return False
