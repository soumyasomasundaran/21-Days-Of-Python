def palindrome(n):
    reversed_num = 0
    original = n
    while (n != 0):
        r = int(n % 10)
        reversed_num = reversed_num * 10 + r
        n = int(n / 10)

    if reversed_num == original:
        print("Palindrome")
    else:
        print("Not a Palindrome")


n = int(input('Enter a number : '))
palindrome(n)
