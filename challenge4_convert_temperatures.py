# Challenge4
"""Write a script called temperature.py that defines two functions:
1. convert_cel_to_far() which takes one float parameter representing
degrees Celsius and returns a float representing the same temperature
in degrees Fahrenheit using the following formula:
F = C * 9/5 + 32
2. convert_far_to_cel() which take one float parameter representing
degrees Fahrenheit and returns a float representing the same temperature
in degrees Celsius using the following formula:
C = (F - 32) * 5/9
The script should first prompt the user to enter a temperature in degrees
Fahrenheit and then display the temperature converted to Celsius.
Then prompt the user to enter a temperature in degrees Celsius and
display the temperature converted to Fahrenheit.
All converted temperatures should be rounded to 2 decimal places."""




temp1 = float(input("Enter a temperature in degrees F: "))

def convert_cel_to_far(x):
    """This function converts temperature in degree Fahrenheit to degree Celsius"""
    F = x * 9/5 + 3
    return f"{x} degrees F = {F:.2f} degrees C"

convert_cel_to_far(temp1)

temp2 = float(input("Enter a temperature in degrees C: "))

def convert_far_to_cel(x):
    """This function converts temperature in degree Celsius to degree Fahrenhneit"""
    C = (x - 32) * 5/9
    return f"{x} degrees C = {C:.2f} degrees F"
convert_far_to_cel(temp2)
