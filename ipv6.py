import re
import urllib
from sopel import module


def ipv6(bot, input):
    try:
        s = re.search('<h1>(.*)', urllib.urlopen('http://ipv6excuses.com').read()).group(1)
        urls = re.findall(r'href=[\'"]?([^\'" >]+)', s)
        quote = re.sub('<.*?>', '', s)

        if urls:
            quote = quote + " (" + ', '.join(urls) + ")"

        bot.say(quote)
    except Exception:
        pass
ipv6.commands = ['ipv6', 'ipv6excuse']

