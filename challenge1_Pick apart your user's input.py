# challenge: Pick apart your user's input
"""Write a script named first_letter.py that first prompts the user for
input by using the string "Tell me your password:" The script should
then determine the first letter of the user’s input, convert that letter
to upper-case, and display it back.
For example, if the user input is "no" then the program should respond
like this:
The first letter you entered was: N"""

user_input = input("Tell me your password:" )
password = user_input[0].upper()
print(password, "This is the first thing you entered")



    
