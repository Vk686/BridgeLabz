d = int(input("Enter Date"))
m = int(input("Enter Month"))
y = int(input("Enter Year"))

y0 = float(y - (14 - m) / 12)
x = float(y0 + y0 / 4 - y0 / 100 + y0 / 400)
m0 = float(m + 12 * ((14 - m) / 12) - 2)
d0 = float((d + x + 31 * m0 / 12) % 7)
n = int(d0)

if n == 0:
    print("sunday")
elif n == 1:
    print("Monday")
elif n == 2:
    print("Tuesday")
elif n == 3:
    print("Wednesday")
elif n == 4:
    print("Thursday")
elif n == 5:
    print("Friday")
elif n == 6:
    print("Saturday")