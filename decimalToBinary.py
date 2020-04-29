decimal = int(input("Enter Decimal Number"))


def toBinary(dec):
    if dec > 1:
        toBinary(dec // 2)
    print(dec % 2, end=" ")


toBinary(decimal)