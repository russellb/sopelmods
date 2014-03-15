import json
import re
import urllib


def format_defn(defn, num, max):
    lines = []
    pieces = re.split(r'\n+', defn['definition'])
    lines.append('%s: definition %i of %i' % (defn['word'], num, max))
    lines.extend(pieces)
    lines.append('Example: %s' % defn['example'].split('\n')[0])
    return lines


def urban(phenny, input):
    baseurl = 'http://api.urbandictionary.com/v0/define?term='

    if not input.group(2):
        phenny.say('Usage: .urban <word> [definition number]')
        return

    input = input.group(2).strip()
    words = input.split()
    try:
        num = int(words[-1])
        input = ' '.join(words[:-1])
    except ValueError:
        num = 1

    try:
        result = json.loads(urllib.urlopen(baseurl + input).read())
    except:
        return

    if not result or "result_type" not in result:
        return

    idx = num - 1
    max = len(result['list'])
    try:
        defn = result['list'][idx]
    except IndexError:
        phenny.say('No definition %i of %i for %s' % (idx, max, input))
        return

    lines = format_defn(defn, num, max)
    for line in lines:
        phenny.say(line)
urban.commands = ['urban']


if __name__ == '__main__':
    import sys

    class Phenny(object):
        def say(self, msg):
            print msg

    urban(Phenny(), re.match('()(.*)', sys.argv[1]))
