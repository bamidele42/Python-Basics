# Challenge2
"""Write a script called translate.py that asks the user for some input
with the following prompt: Enter some text:. Then use the .replace()
method to convert the text entered by the user into “leetspeak” by making
the following changes to lower-case letters:
• The letter a becomes 4
• The letter b becomes 8
• The letter e becomes 3
• The letter l becomes 1
• The letter o becomes 0
• The letter s becomes 5
• The letter t becomes 7
"""
user_input = input("Enter some text: ")
change1 = user_input.replace("a", "4")
change2 = change1.replace("b", "8")
change3 = change2.replace("e", "3")
change4 = change3.replace("l", "1")
change5 = change4.replace("o", "0")
change6 = change5.replace("s", "5")
change7 = change6.replace("t", "7")
print(change7)

