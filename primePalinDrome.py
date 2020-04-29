class PrimeAndPalindrome:

    def palindrome(number):
        tempNumber = 0
        variable = number
        while number != 0:
            temp = number % 10
            tempNumber = 10 * tempNumber + temp
            number = number // 10
        return variable == tempNumber

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
        if palindrome(number) and prime(number):
            print(number, end=" ")
