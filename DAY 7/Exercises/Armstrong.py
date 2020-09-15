def check_armstrong(num):
    length = len(str(num))
    sum = 0
    temp = num

    while (temp != 0):
        sum = sum + ((temp % 10) ** length)
        temp = temp // 10

    if sum == num:
        print("Armstrong number")
    else:
        print("Not Armstrong number")


num = int(input("Enter a number: "))
check_armstrong(num)