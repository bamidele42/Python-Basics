"""Challenge: Wax Poetic
In this challenge, you’ll write a program that generates poetry.
Create five lists for different word types:
• Nouns: ["fossil", "horse", "aardvark", "judge", "chef", "mango",
"extrovert", "gorilla"]
• Verbs: ["kicks", "jingles", "bounces", "slurps", "meows",
"explodes", "curdles"]
• Adjectives: ["furry", "balding", "incredulous", "fragrant",
"exuberant", "glistening"]
• Prepositions: ["against", "after", "into", "beneath", "upon",
"for", "in", "like", "over", "within"]
• Adverbs: ["curiously", "extravagantly", "tantalizingly",
"furiously", "sensuously"]

Randomly select the following number of elements from each list:
• 3 nouns
• 3 verbs
• 3 adjectives
• 2 prepositions
• 1 adverb

Using the randomly selected words, generate and display a poem with
the following structure inspired by Clifford Pickover:
{A/An} {adj1} {noun1}
{A/An} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}
{adverb1}, the {noun1} {verb2}
the {noun2} {verb3} {prep2} a {adj3} {noun3}
"""

import random
Nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
Verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
Adjectives = ["furry", "balding", "incredulous", "fragrant","exuberant", "glistening"]
Prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
Adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]
def wax_poetic():
    noun1 = random.choice(Nouns)
    noun2 = random.choice(Nouns)
    noun3 = random.choice(Nouns)
    verb1 = random.choice(Verbs)
    verb2 = random.choice(Verbs)
    verb3 = random.choice(Verbs)
    adj1 = random.choice(Adjectives)
    adj2 = random.choice(Adjectives)
    adj3 = random.choice(Adjectives)
    prep1 = random.choice(Prepositions)
    prep2 = random.choice(Prepositions)
    adv1 = random.choice(Adverbs)

    return f"""A/An {adj1} {noun1}
    A/An {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}
    {adv1}, the {noun1} {verb2}
    the {noun2} {verb3} {prep2} a {adj3} {noun3} """

wax_poetic()
