# Assignment 2, Task 1
# Name: Rinchen Lekchen Gyeltshen
# Collaborators:no one
# Time Spent: 0:20 hrs
s = input()
t = input()
s = s.lower()
t = t.upper()
s = s.replace("s", "m").replace("l", "m").replace("a", "m")
t = t.replace("P", "T").replace("O", "T").replace("I", "T").replace("N", "T")
first_s = s[0]
first_t = t[0]
remain_s = s[1:]
remain_t = t[1:]
s = first_t + remain_s
t = first_s + remain_t
one_third_s = int(len(s) / 3)
one_third_t = int(len(t) / 3)
remaining_s = s[:-one_third_s]
middle_part = t[one_third_t: (one_third_t * 2)]
s = remaining_s + middle_part
z = s + t
print(z)
