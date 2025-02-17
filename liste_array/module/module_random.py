import random
from pprint import pprint # pprint afficher le result a une liste 

r = random.randint(0, 1) # random number generator 0 au 1 : randint:  1
print("randint: ", r)

u = random.uniform(0, 1) # random number generator decimals : uniform:  0.17912819397213464
print("uniform: ", u)

rand = random.randrange(99) # random number generator : randrange : 701 - Ex:(0, 101, 10) par pas
print("randrange :", rand)

# pprint(dir(random)) # random help
# help(random.randint)
