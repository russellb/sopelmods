import random
import pyjokes
from sopel import module

@module.commands('pyjoke')
def pyjoke(bot, trigger):
    j1 = pyjokes.get_jokes(category='neutral')
    j2 = pyjokes.get_jokes(category='adult')
    bot.say(random.choice(j1 + j2))
