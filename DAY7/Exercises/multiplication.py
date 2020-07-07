def multiplication_table(n):
    """prints multiplication table up to 10"""
    for i in range(1, 11):
        print(i, '*', n, '=', (i * n))


n = int(input("Enter the number"))
print("The multiplication Table of %d is"%n)
multiplication_table(n)
