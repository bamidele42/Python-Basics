""" With some help from the random module and a little condition logic,
you can simulate an election between two candidates.
Suppose two candidates, Candidate A and Candidate B, are running
for mayor in a city with three voting regions. The most recent polls
show that Candidate A has the following chances for winning in each
region:
• Region 1: 87% chance of winning
• Region 2: 65% chance of winning
• Region 3: 17% chance of winning
Write a program that simulates the election 10,000 times and prints
the percentage of where Candidate A wins.
To keep things simple, assume that a candidate wins the election is
they win in at least two of the three regions.

"""


"""Using the random.random to write probability for an unfair coin toss that will help stimulate election between two candidate"""

import random

def Election_result(probability_of_tails):
    if random.random() < probability_of_tails:
        return "canditate_B"
    else:
        return "canditate_A"

"""Let's re-write the fair coin flip experiment from earlier using unfair_coin_flip() to run each trial with an unfair coin"""

region_1 = 0
region_2 = 0
region_3 = 0

for trial in range(10_000):
    if Election_result(.87) == "canditate_A":
        region_1 = region_1 + 1
    elif Election_result(.65) == "canditate_A":
        region_2 = region_2 + 1
    elif Election_result(.17) == "canditate_A":
        region_3 = region_3 + 1
    else:
        region_1 = region_1 + 1
        region_2 = region_2 + 1
        region_3 = region_3 + 1

total = region_1 + region_2 + region_3
percentage = ((region_1 + region_2 )/ total) * 100
print(f"The chances of candidate A winning is {percentage:.2f}%")
