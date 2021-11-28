'''Program to divide two numbers'''

while True:
    try:
        a = int(input())
        b = int(input())
        c = a/b
    except:
        print("Enter valid input only!")
    else:
        print(c)
        break
