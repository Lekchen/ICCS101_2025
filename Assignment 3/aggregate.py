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

def my_mean(p: float, q: float, r: float) -> float:
    total = p + q + r
    mean = total / 3
    return float(mean)

def my_med(p: float, q: float, r: float) -> float:
    total = p + q + r
    maxi_pq = ((p + q) + abs(p - q)) // 2
    maxi = ((maxi_pq + r) + abs(maxi_pq - r)) // 2
    mini_pq = ((p + q) - abs(p - q)) // 2
    mini = ((mini_pq + r) - abs(mini_pq - r)) // 2
    med = total - maxi - mini
    return float(med)
