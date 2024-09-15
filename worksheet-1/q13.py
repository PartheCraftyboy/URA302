principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (as a percentage): ")) / 100
times_compounded = int(input("Enter the number of times interest is compounded per year: "))
time = float(input("Enter the time the money is invested for (in years): "))


amount = principal * (1 + rate / times_compounded) ** (times_compounded * time)
compound_interest = amount - principal

print(f"Compound Interest: ${compound_interest}")
print(f"Total Amount after {time} years: ${amount:.2f}")