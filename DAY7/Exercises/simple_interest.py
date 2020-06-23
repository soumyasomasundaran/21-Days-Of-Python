princ_amount = float(input(" Enter the Principal Amount : "))
rate_of_int = float(input("  Enter the Rate Of Interest   : "))
time_period = float(input("  Enter Time period in Years   : "))

simple_interest = (princ_amount * rate_of_int * time_period) / 100

print("Simple Interest is",simple_interest)