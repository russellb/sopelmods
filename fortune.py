import commands

def fortune(phenny, input):
   fortune = commands.getoutput('fortune')
   for line in fortune.rsplit("\n"):
      phenny.say(line)
fortune.commands = ['fortune']
