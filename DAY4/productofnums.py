#Finding the product of numbers upto a limit
n=int(input("Enter the limit"))
product=1
for i in range(1,n+1):
    product=product*i
print("Product of numbers is:",product)