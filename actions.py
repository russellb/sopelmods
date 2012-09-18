# -*- coding: utf-8 -*-

from random import choice


def table(phenny, input):
    phenny.say('(╯°□°）╯︵ ┻━┻')
table.commands = ['table', 'rage']


def untable(phenny, input):
    phenny.say('┬┬ ノ(゜-゜ノ)')
untable.commands = ['untable', 'putitback', 'unrage']


def joyful(phenny, input):
    joyful_emotes = ['🙌', '😀', '😁', '😂', '😃', '😄', '😅']
    phenny.say(choice(joyful_emotes))
joyful.commands = ['huzzuh', 'awesome', 'happy', 'smile']
