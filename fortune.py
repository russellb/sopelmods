import commands
from sopel import module

def fortune(bot, input):
   fortune = commands.getoutput('fortune')
   for line in fortune.rsplit("\n"):
      bot.say(line)
fortune.commands = ['fortune']
