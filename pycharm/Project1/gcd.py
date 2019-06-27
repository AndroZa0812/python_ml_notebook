def gcd(x, y):
    num1 = max(x, y)
    num2 = min(x, y)
    while num2 != 0:
        num1 %= num2
        if num1 < num2:
            num1, num2 = num2, num1

    return num1


print(gcd(1071, 462))
