from pyfiglet import Figlet

def figlet(phenny, input):
   f = Figlet()
   for l in f.renderText(input.group(2) or "").rsplit("\n"):
      phenny.say(l)
figlet.commands = [ 'figlet' ]
