# -*- coding: utf-8 -*-

import itertools

flip_table = {
    '1': 'Ɩ',
    '2': 'ᄅ',
    '3': 'Ɛ',
    '4': 'ㄣ',
    '5': 'ϛ',
    '6': '9',
    '7': 'ㄥ',
    '8': '8',
    '9': '6',
    '0': '0',
    'a': 'ɐ',
    'b': 'q',
    'c': 'ɔ',
    'd': 'p',
    'e': 'ǝ',
    'f': 'ɟ',
    'g': 'ƃ',
    'h': 'ɥ',
    'i': 'ı',
    'j': 'ɾ',
    'k': 'ʞ',
    'l': 'ן',
    'm': 'ɯ',
    'n': 'u',
    'o': 'o',
    'p': 'd',
    'q': 'b',
    'r': 'ɹ',
    's': 's',
    't': 'ʇ',
    'u': 'n',
    'v': 'ʌ',
    'w': 'ʍ',
    'x': 'x',
    'y': 'ʎ',
    'z': 'z',
    '.': '',
    '[': ']',
    '(': ')',
    '{': '}',
    '?': '¿',
    '!': '¡',
    "'": ',',
    '<': '>',
    '_': '‾',
    '"': '„',
    ';': '؛'
}


def _reverse(text):
    return text[::-1]


def _map_by_table(table, text):
    return "".join(table.get(w, w) for w in text)


def caps(phenny, input):
    phenny.say(input.upper())
caps.commands = ['caps']


def reverse(phenny, input):
     phenny.say(input[::-1])
reverse.commands = ['reverse']


def flip(phenny, input):
    flip_reverse(phenny, input[::-1])
flip.commands = ['flip']


def flip_reverse(phenny, input):
    phenny.say(_map_by_table(flip_table, input.lower()))
flip_reverse.commands = ['flip_reverse']
