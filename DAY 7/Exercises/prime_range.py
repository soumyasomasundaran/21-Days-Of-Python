def prime_range(lower,upper):
    for num in range(lower, upper + 1):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)


lower = int(input("Enter the lower limit"))
upper = int(input("Enter the upper limit"))
print("Prime numbers between", lower, "and", upper, "are:")
prime_range(lower,upper)

