import random

import pyjokes


def pyjoke(phenny, input):
    j1 = pyjokes.get_jokes(category='neutral')
    j2 = pyjokes.get_jokes(category='adult')
    phenny.say(random.choice(j1 + j2))
pyjoke.commands = ['pyjoke', 'pyjokes']
