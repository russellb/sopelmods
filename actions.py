# -*- coding: utf-8 -*-

from random import choice
import time


def table(phenny, input):
    rage = [
        '(╯°□°）╯︵ ┻━┻',
        '┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻',
        '（╯°□°）╯︵(\ .o.)\\',
        '(╯°□°)╯︵ ┻━┻ ︵ ╯(°□° ╯)',
        '(ノಠ益ಠ)ノ彡┻━┻',
    ]
    phenny.say(choice(rage))
table.commands = ['table', 'rage']


def untable(phenny, input):
    phenny.say('┬┬ ノ(゜-゜ノ)')
untable.commands = ['untable', 'putitback', 'unrage']


def raaage(phenny, input):
    rage = [
        '┬──┬ ノ( ゜-゜ノ)',
        '┬──┬◡ﾉ(° -°ﾉ)',
        '(╯°□°）╯︵ ┻━┻',
        '┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻',
        '（╯°□°）╯︵(\ .o.)\\',
        '(/ﾟДﾟ)/',
    ]
    for r in rage:
        phenny.say(r)
        time.sleep(0.5)
raaage.commands = ['raaage', 'RAAAGE', 'ultrarage']


def dapper(phenny, input):
    phenny.say('┌─┐')
    phenny.say('┴─┴')
    phenny.say('ಠ_ರೃ')
dapper.commands = ['dapper']

def smile(phenny, input):
    joyful_emotes = ['🙌', '😀', '😁', '😂', '😃', '😄', '😅', '\(סּںסּَ`)/ۜ', '【ツ】']
    phenny.say(choice(joyful_emotes))
smile.commands = ['huzzuh', 'awesome', 'happy', 'smile']


def finger(phenny, input):
    fingers = ['┌∩┐(◣_◢)┌∩┐', '凸(¬‿¬)凸']
    phenny.say(choice(fingers))
finger.commands = ['finger']


def umadbro(phenny, input):
    phenny.say('¯\_(ツ)_/¯')
umadbro.commands = ['umadbro', 'shrug', 'idunno', 'notsure']


def troll(phenny, input):
    phenny.say('░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░')
    phenny.say('░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░')
    phenny.say('░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░')
    phenny.say('░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░')
    phenny.say('░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░')
    phenny.say('█░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█')
    phenny.say('█░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█')
    phenny.say('░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░')
    phenny.say('░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░')
    phenny.say('░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░')
    phenny.say('░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░')
    phenny.say('░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░')
    phenny.say('░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░')
    phenny.say('░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░')
    phenny.say('░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░')
troll.commands = ['troll','trollface']

def trololo(phenny, input):
    phenny.say('http://trololololololololololo.com/')
trololo.commands = ['trolo', 'trololo', 'trolololo']

def notbad(phenny, input):
    phenny.say('░░░░░░░░░▄██████████▄▄░░░░░░░░')
    phenny.say('░░░░░░▄█████████████████▄░░░░░')
    phenny.say('░░░░░██▀▀▀░▀▀▀▀▀▀▀████████░░░░')
    phenny.say('░░░░██░░░░░░░░░░░░░░███████░░░')
    phenny.say('░░░██░░░░░░░░░░░░░░░████████░░')
    phenny.say('░░░█▀░░░░░░░░░░░░░░░▀███████░░')
    phenny.say('░░░█▄▄██▄░░░▀█████▄░░▀██████░░')
    phenny.say('░░░█▀███▄▀░░░▄██▄▄█▀░░░█████▄░')
    phenny.say('░░░█░░▀▀█░░░░░▀▀░░░▀░░░██░░▀▄█')
    phenny.say('░░░█░░░█░░░▄░░░░░░░░░░░░░██░██')
    phenny.say('░░░█░░█▄▄▄▄█▄▀▄░░░░░░░░░▄▄█▄█░')
    phenny.say('░░░█░░█▄▄▄▄▄▄░▀▄░░░░░░░░▄░▀█░░')
    phenny.say('░░░█░█▄████▀██▄▀░░░░░░░█░▀▀░░░')
    phenny.say('░░░░██▀░▄▄▄▄░░░▄▀░░░░▄▀█░░░░░░')
    phenny.say('░░░░░█▄▀░░░░▀█▀█▀░▄▄▀░▄▀░░░░░░')
    phenny.say('░░░░░▀▄░░░░░░░░▄▄▀░░░░█░░░░░░░')
    phenny.say('░░░░░▄██▀▀▀▀▀▀▀░░░░░░░█▄░░░░░░')
    phenny.say('░░▄▄▀░█░▀▄░░░░░░░░░░▄▀░▀▀▄░░░░')
    phenny.say('▄▀▀░░░███▄█▄░░░░░░▄▀░░░░░░█▄░░')
    phenny.say('█░░░░░███▄█▄░░░░░░▄▀░░░░░░░▀█▄')
notbad.commands = ['notbad']

def dealwithit(phenny, input):
    phenny.say('(•_•)')
    phenny.say('( •_•)>⌐■-■')
    phenny.say('(⌐■_■)')
dealwithit.commands = ['dealwithit']


def pirate(phenny, input):
    phenny.say('(•_•)')
    phenny.say('( •_•)>⌐■')
    phenny.say('(⌐■_•)')
pirate.commands = ['pirate', 'pirateup']


def glare(phenny, input):
    phenny.say('ಠ_ಠ')
glare.commands = ['glare', 'eyes', 'disapprove']


def facepalm(phenny, input):
    phenny.say('(>ლ)')
facepalm.commands = ['facepalm']


def tothemoon(phenny, input):
   phenny.say('┗(°0°)┛')
tothemoon.commands = ['tothemoon']


def postal(phenny, input):
    choices = [
        "' ̿'\̵͇̿̿\з=(◕_◕)=ε/̵͇̿̿/'̿'̿ ̿'",
        "¯¯̿̿¯̿̿'̿̿̿̿̿̿̿'̿̿'̿̿̿̿̿'̿̿̿)͇̿̿)̿̿̿̿ '̿̿̿̿̿̿\̵͇̿̿\=(•̪̀●́)=o/̵͇̿̿/'̿̿ ̿ ̿̿",
    ]
    phenny.say(choice(choices))
postal.commands = ['postal']


def ping(phenny, input):
    phenny.say('( •_•)O*¯`·.   |')
ping.commands = ['ping']


def pong(phenny, input):
    phenny.say('               |   .·´¯`°Q(•_• )')
pong.commands = ['pong']


def hi(phenny, input):
    choices = ['o/', '\o']
    phenny.say(choice(choices))
hi.commands = ['hi', 'ohai', 'hello', 'greetings', 'hola', 'bonjour']


def fail(phenny, input):
    phenny.say('http://www.youtube.com/watch?v=WtNHuqHWefU')
fail.commands = ['fail', 'dummy', 'dumber', 'stupid']


def boggle(phenny, input):
    phenny.say('           .--.')
    phenny.say('         .\'    \'.')
    phenny.say('        /  ~~~~  \\')
    phenny.say('       ( __    __ )')
    phenny.say('      /|<o->  <o->|\\')
    phenny.say('     ( |    ^^    | )')
    phenny.say('    _ ) \   __   / /')
    phenny.say('   /##\  \_(__)_/ /')
    phenny.say('  /####) )#\__// (')
    phenny.say(' /####( |##| |#\  \\')
    phenny.say('(#####| |##(_/##\_/\\')
    phenny.say(' \####(_)###########\\')
    phenny.say('   \#################)')
    phenny.say('    \/##############/')
boggle.commands = ['boggle', 'thescream']


def yay(phenny, input):
    phenny.say('\o/')
yay.commands = ['yay', 'woot', 'w00t']


def shithitsfan(phenny, input):
    phenny.say('https://www.youtube.com/watch?v=aZdp46Jen_w')
shithitsfan.commands = ['shithitsfan']


def fishslap(phenny, input):
    phenny.say('https://www.youtube.com/watch?v=IhJQp-q1Y1s')
fishslap.commands = ['fishslap']


def makeitrain(phenny, input):
    phenny.say('[̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅]')
    phenny.say('')
    phenny.say('[̲̅$̲̅(̲̅5̲̅)̲̅$̲̅]')
    phenny.say('')
    phenny.say('[̲̅$̲̅(̲̅1̲̅)̲̅$̲̅]')
makeitrain.commands = ['makeitrain']


def failboat(phenny, input):
    phenny.say('    __4_____')
    phenny.say(' _  \F\A\I\L\\')
    phenny.say('<\'\ /_/_/_/_/')
    phenny.say(' ((____!_____/)')
    phenny.say(' \\0\\0\\0\\0\\0\/')
    phenny.say(' ~~~~~~~~~~~~~~~')
failboat.commands = ['failboat']


def beerme(phenny, input):
    phenny.say('     ,-"-.__,-"-.__,-"-..')
    phenny.say('    ( C>  )( C>  )( C>  ))')
    phenny.say('   /.`-_-\'||`-_-\'||`-_-\'/')
    phenny.say('  /-"-.--,-"-.--,-"-.--/|')
    phenny.say(' ( C>  )( C>  )( C>  )/ |')
    phenny.say('(|`-_-\',.`-_-\',.`-_-\'/  |')
    phenny.say(' `-----++-----++----\'|  |')
    phenny.say(' |     ||     ||     |-\'')
    phenny.say(' |     ||     ||     |')
    phenny.say(' |     ||     ||     |')
    phenny.say('  `-_-\'  `-_-\'  `-_-\'')
beerme.commands = ['beerme']
