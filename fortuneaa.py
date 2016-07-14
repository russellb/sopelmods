import commands
from sopel import module

def fortuneaa(bot, input):
   #fortune = commands.getoutput('fortune ascii-art mario.arteascii')
   fortune = commands.getoutput('fortune ascii-art')
   for line in fortune.rsplit('\n'):
      bot.say(line)
fortuneaa.commands = ['fortuneaa']
