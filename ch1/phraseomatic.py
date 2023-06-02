import random

verbs = ['Leverage','Sync','Target','Gamify','Offline','Crowd-sourced', '24/7','Lean-in','30.000 foot']

adjetives = ['A/B Tested','Freemium','Hyperlocal','Siloed','B-to-B','Oriented','Coud-based','API-based']

nouns = ['Early adopter','Low-hanging fruit','Pipeline','Splash Page','Prouctivity','Process','Tipping point','Paradigm']

verb = random.choice(verbs)

adjetive = random.choice(adjetives)

noun = random.choice(nouns)

phrase = verb + ' ' + adjetive + ' ' + noun

print(phrase) 
