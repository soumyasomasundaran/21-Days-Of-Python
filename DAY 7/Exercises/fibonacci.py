def fibonacci(num):
    # initializing first two elements of the fibonacci series
    first = 0
    second = 1

    print("\nfibonacci series is:")
    print(first, ",", second, end=", ")

    for i in range(2, num):
        next = first + second
        print(next, end=", ")

        first = second
        second = next


num = int(input("Enter the length of the fibonacci series you want(minimum length = 2)"))
fibonacci(num)
