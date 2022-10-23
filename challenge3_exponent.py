# Challenge3
"""Write a script called exponent.py that receives two numbers from the
user and displays the first number raised to the power of the second
number.
A sample run of the program should look like this (with example input
that has been provided by the user included below):
Enter a base: 1.2
Enter an exponent: 3
1.2 to the power of 3 = 1.7279999999999998"""

num1 = float(input("Enter a base: "))
num2 = float(input("Enter an exponent: "))
power = num1 ** num2
print(f"{num1} to the power of {num2} = {power}")

#num = float(input("enter a number here: "))
#round_num = round(num, 2)
#print(f"{num}  rounded to 2 decimal places is {round_num}")

#num1 = float(input("Enter first number here: "))
#num2 = float(input("Enter second number here: "))
#diff = num1 - num2
#print(f"The difference between {num1} and {num2} is an integer? {diff.is_integer()}!")
