import re
import urllib


def ipv6(phenny, input):
    try:
        s = re.search('<h1>(.*)', urllib.urlopen('http://ipv6excuses.com').read()).group(1)
        phenny.say(re.sub('<.*?>', '', s))
    except Exception:
        pass
ipv6.commands = ['ipv6', 'ipv6excuse']

