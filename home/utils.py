import string
import random
from random import randint


""""Generates unique ids"""""
def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def generate_description():
    names=["You","I","They","He","She","Ken","We"]
    verbs=["am","was", "is", "are", "were"]
    nouns=["playing football.", "watching television.", "singing.", "swimming.", "riding."]
    description = names[randint(0,len(names)-1)]+" "+verbs[randint(0,len(verbs)-1)]+" "+nouns[randint(0,len(nouns)-1)]
    return description