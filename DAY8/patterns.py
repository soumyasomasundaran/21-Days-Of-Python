

def pattern_one(n):
    myList = []
    for i in range(1, n + 1):
        myList.append(" *" * i)
    print("\n".join(myList))


def pattern_two(n):
    k = 2 * n - 2

    for i in range(0, n):

        for j in range(0, k):
            print(end=" ")

        k = k - 1

        for j in range(0, i + 1):
            print("* ", end="")

        print("\r")


def pattern_three(n):
    num = 1

    for i in range(0, n):

        num = 1

        for j in range(0, i + 1):
            print(num, end=" ")

            num = num + 1

        print("\r")


# Driver Code
n = int(input("Enter the number of lines"))
print("\nPattern One")

pattern_one(n)
print("\nPattern Two")
pattern_two(n)
print("\nPattern Three")
pattern_three(n)
