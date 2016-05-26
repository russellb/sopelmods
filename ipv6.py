import re
import urllib


def ipv6(phenny, input):
    try:
        s = re.search('<h1>(.*)', urllib.urlopen('http://ipv6excuses.com').read()).group(1)
        urls = re.findall(r'href=[\'"]?([^\'" >]+)', s)
        quote = re.sub('<.*?>', '', s)

        if urls:
            quote = quote + " (" + ', '.join(urls) + ")"

        phenny.say(quote)
    except Exception:
        pass
ipv6.commands = ['ipv6', 'ipv6excuse']

