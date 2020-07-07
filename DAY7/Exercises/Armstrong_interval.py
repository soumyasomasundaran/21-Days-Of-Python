def check_armstrong(num1,num2):
    for num in range(num1,num2+1):
        length = len(str(num))
        sum = 0
        temp = num
        while (temp != 0):
            sum = sum + ((temp % 10) ** length)
            temp = temp // 10

        if sum == num:
            print(num)



num1 = int(input("Enter the starting number: "))
num2 = int(input("Enter the ending number: "))


check_armstrong(num1,num2)