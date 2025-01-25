# Assignment 3, Task 1
# Name: Rinchne Lekchen Gyeltshen
# Collaborators: John Nonexistent
# Time Spent: 0:10 hrs
def my_min(p: float, q: float, r: float) -> float:
    mini = 0
    if p - q > 0:
        mini += q
        if q - r > 0:
            mini -= q
            mini += r
    elif q - r > 0:
        mini += r
        if r - p > 0:
            mini -= r
            mini += p
    elif r - p > 0:
        mini += p
        if p - q > 0:
            mini -= p
            mini += q
    return mini
