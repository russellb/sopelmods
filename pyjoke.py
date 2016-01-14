import pyjokes


def pyjoke(phenny, input):
    phenny.say(pyjokes.get_joke(category='all'))
pyjoke.commands = ['pyjoke', 'devjoke']
