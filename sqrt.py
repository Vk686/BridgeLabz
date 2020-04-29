import math



def sqRt(c):
    t = c
    epsilon = float(1 * math.pow(10, -15))
    while abs(t - c / t) > epsilon * t:
        t = ((c / t) + t) / 2
    return t


value = int(input("Enter Value  :"))
val = sqRt(value)
print(val)