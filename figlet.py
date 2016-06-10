from pyfiglet import Figlet
from sopel import module

def figlet(bot, input):
   f = Figlet()
   for l in f.renderText(input.group(2) or "").rsplit("\n"):
      bot.say(l)
figlet.commands = [ 'figlet' ]
