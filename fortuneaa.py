import commands

def fortuneaa(phenny, input):
   #fortune = commands.getoutput('fortune ascii-art mario.arteascii')
   fortune = commands.getoutput('fortune ascii-art')
   for line in fortune.rsplit('\n')
      phenny.say(line)
fortuneaa.commands = ['fortuneaa']
