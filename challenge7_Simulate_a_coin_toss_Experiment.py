""" Suppose you flip a fair coin repeatedly until it lands on both heads
and tails at least once each. In other words, after the first flip, you
continue to flip the coin until it lands on something different.
Doing this generates a sequence of heads and tails. For example, the
first time you do this experiment, the sequence might be heads, heads,
then tails.
On average, how many flips are needed for the sequence to contain
both heads and tails?
Write a simulation that runs 10,000 trials of the experiment and
prints the average number of flips per trial.
"""


"""Let's start by writing a function called coin_flip() that randomly returns the string 'head' or string 'tails'"""
import random

def coin_flip():
    """ Randomly return 'heads' or 'tails'. """
    if random.randint(0, 1) == 0:
        return "heads" or "tails"
    else:
        return "tails" or "heads"

"""Now we can write a for loop that flips the coin 10,000 times and updates a heads or tails tally accordingly"""
# First initialize the tallies to 0

heads_tally = 0
tails_tally = 0

for trial in range(10_000):
    if coin_flip() == "heads" and "tails":
        heads_tally = heads_tally + 1
    else:
        tails_tally = tails_tally + 1

"""Finally, we can print the average of heads and tails:"""
average = heads_tally + tails_tally / 2
print(f"The averages of heads to tails is {average}")
