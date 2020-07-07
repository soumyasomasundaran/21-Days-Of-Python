#Finding numbers that are not divisible by a particular number
n=int(input("Enter the number"))
print('The numbers between 1-100 that are  divisible by %d are:'%n)
for i in range(1,100):
    if i%n!=0:
        continue
    else:
        print(i,end=" ")
