def reverse(n):
    reversed_num = 0

    while (n != 0):
        r = int(n % 10)
        reversed_num = reversed_num * 10 + r
        n = int(n / 10)

    return reversed_num


n = int(input('Enter a number : '))
reversed_num = reverse(n)
print("Reversed number is", reversed_num)
