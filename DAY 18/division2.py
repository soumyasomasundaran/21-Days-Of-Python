try:
    a = int(input())
    b = int(input())
    c = a/b
except ZeroDivisionError:
    print("division by zero")
except ValueError:
    print("Enter valid input")
else:
    print(c)