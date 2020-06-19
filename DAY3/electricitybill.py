units=int(input("Enter the units consumed in a month"))
if(units<=50):
    amount=units*.50
elif(units<=150):
    amount = 25 + ((units-50) * 0.75)
elif(units<=250):
    amount = 100 + ((units-150) * 1.20)
else:
    amount = 220 + ((units - 250) * 1.50)
sur_charge = amount * 0.20
total_amt  = amount + sur_charge

print("\nBill is " ,total_amt)