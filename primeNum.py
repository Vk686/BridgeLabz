def prime(num):
    count = 1
    for i in range(1, num):
        if num % i == 0:
            count += 1
        if count > 2:
            break

    if count == 2:
        return True
    return False


for number in range(1001):
    if prime(number):
     print(number,end=" ")