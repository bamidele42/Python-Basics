"""Challenge: Find the Factors of a
Number
A factor of a positive integer n is any positive integer less than or equal
to n that divides n with no remainder.
For example, 3 is a factor of 12 because 12 divided by 3 is 4, with no
remainder. However, 5 is not a factor of 12 because 5 goes into 12 twice
with a remainder of 2.
Write a script factors.py that asks the user to input a positive integer
and then prints out the factors of that number.
"""



word = int(input("Enter a positive number: "))

#for i in range(1, word):
#    if word % i  == 0:
#        print(f"{i} is a factor of {word}")
    #else:
        #print(f"{i} is not a factor of {word}")

n = 1
while n <= word:
    if word % n == 0:
        print(f"{n} is a factor of {word}")
    n += 1
