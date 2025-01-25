# Assignment 3, Task 2
# Name: Rinchne Lekchen Gyeltshen
# Collaborators: John Nonexistent
# Time Spent: 0:10 hrs
def price(vol: int) -> float:
    vol_per_price = vol * 18
    total_price = 0
    if vol < 20:
        total_price += vol_per_price + 250
    elif 20 <= vol <= 100:
        total_price += vol_per_price + (10 * vol)
    elif vol > 100:
        total_price += vol_per_price - (0.01 * vol_per_price)
