# Challenge5
"""In this challenge, you will write a program called invest.py that tracks
the growing amount of an investment over time.
An initial deposit, called the principal amount, is made. Each year,
the amount increases by a fixed percentage, called the annual rate of
return.
For example, a principal amount of $100 with an annual rate of return
of 5% increases the first year by $5. The second year, the increase is
5% of the new amount $105, which is $5.25.
Write a function called invest with three parameters: the principal
amount, the annual rate of return, and the number of years to calculate.
The function signature might look something like this:
def invest(amount, rate, years):"""



amount = float(input("Enter the number of initial deposit: "))
rate = float(input("Enter an annual percentage rate: "))
years = int(input("Enter Number of years: "))

def invest(amount, rate, years):
    for i in range(1,years):
        print(f"year {i}: ${amount+(amount * rate * i)/100:.2f}") 

invest(amount, rate, years)
