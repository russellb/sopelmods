import urllib
from xml.dom.minidom import parseString


def devexcuse(phenny, input):
    phenny.say(parseString(
        urllib.urlopen('http://developerexcuses.com').read().replace('&', '')).
        getElementsByTagName('body')[0].getElementsByTagName('div')[0].
        getElementsByTagName('center')[0].getElementsByTagName('a')[0].
        childNodes[0].nodeValue)
devexcuse.commands = ['devexcuse']
