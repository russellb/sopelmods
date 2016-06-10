# -*- coding: utf-8 -*-

from random import choice
import time
from sopel import module

def table(bot, input):
    rage = [
        '(╯°□°）╯︵ ┻━┻',
        '┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻',
        '（╯°□°）╯︵(\ .o.)\\',
        '(╯°□°)╯︵ ┻━┻ ︵ ╯(°□° ╯)',
        '(ノಠ益ಠ)ノ彡┻━┻',
    ]
    bot.say(choice(rage))
table.commands = ['table', 'rage']


def untable(bot, input):
    bot.say('┬┬ ノ(゜-゜ノ)')
untable.commands = ['untable', 'putitback', 'unrage']


def raaage(bot, input):
    rage = [
        '┬──┬ ノ( ゜-゜ノ)',
        '┬──┬◡ﾉ(° -°ﾉ)',
        '(╯°□°）╯︵ ┻━┻',
        '┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻',
        '（╯°□°）╯︵(\ .o.)\\',
        '(/ﾟДﾟ)/',
    ]
    for r in rage:
        bot.say(r)
        time.sleep(0.5)
raaage.commands = ['raaage', 'RAAAGE', 'ultrarage']


def dapper(bot, input):
    bot.say('┌─┐')
    bot.say('┴─┴')
    bot.say('ಠ_ರೃ')
dapper.commands = ['dapper']

def smile(bot, input):
    joyful_emotes = ['🙌', '😀', '😁', '😂', '😃', '😄', '😅', '\(סּںסּَ`)/ۜ', '【ツ】']
    bot.say(choice(joyful_emotes))
smile.commands = ['huzzuh', 'awesome', 'happy', 'smile']


def finger(bot, input):
    fingers = ['┌∩┐(◣_◢)┌∩┐', '凸(¬‿¬)凸']
    bot.say(choice(fingers))
finger.commands = ['finger']


def umadbro(bot, input):
    bot.say('¯\_(ツ)_/¯')
umadbro.commands = ['umadbro', 'shrug', 'idunno', 'notsure']


def troll(bot, input):
    bot.say('░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░')
    bot.say('░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░')
    bot.say('░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░')
    bot.say('░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░')
    bot.say('░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░')
    bot.say('█░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█')
    bot.say('█░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█')
    bot.say('░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░')
    bot.say('░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░')
    bot.say('░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░')
    bot.say('░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░')
    bot.say('░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░')
    bot.say('░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░')
    bot.say('░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░')
    bot.say('░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░')
troll.commands = ['troll','trollface']

def trololo(bot, input):
    bot.say('http://trololololololololololo.com/')
trololo.commands = ['trolo', 'trololo', 'trolololo']

def notbad(bot, input):
    bot.say('░░░░░░░░░▄██████████▄▄░░░░░░░░')
    bot.say('░░░░░░▄█████████████████▄░░░░░')
    bot.say('░░░░░██▀▀▀░▀▀▀▀▀▀▀████████░░░░')
    bot.say('░░░░██░░░░░░░░░░░░░░███████░░░')
    bot.say('░░░██░░░░░░░░░░░░░░░████████░░')
    bot.say('░░░█▀░░░░░░░░░░░░░░░▀███████░░')
    bot.say('░░░█▄▄██▄░░░▀█████▄░░▀██████░░')
    bot.say('░░░█▀███▄▀░░░▄██▄▄█▀░░░█████▄░')
    bot.say('░░░█░░▀▀█░░░░░▀▀░░░▀░░░██░░▀▄█')
    bot.say('░░░█░░░█░░░▄░░░░░░░░░░░░░██░██')
    bot.say('░░░█░░█▄▄▄▄█▄▀▄░░░░░░░░░▄▄█▄█░')
    bot.say('░░░█░░█▄▄▄▄▄▄░▀▄░░░░░░░░▄░▀█░░')
    bot.say('░░░█░█▄████▀██▄▀░░░░░░░█░▀▀░░░')
    bot.say('░░░░██▀░▄▄▄▄░░░▄▀░░░░▄▀█░░░░░░')
    bot.say('░░░░░█▄▀░░░░▀█▀█▀░▄▄▀░▄▀░░░░░░')
    bot.say('░░░░░▀▄░░░░░░░░▄▄▀░░░░█░░░░░░░')
    bot.say('░░░░░▄██▀▀▀▀▀▀▀░░░░░░░█▄░░░░░░')
    bot.say('░░▄▄▀░█░▀▄░░░░░░░░░░▄▀░▀▀▄░░░░')
    bot.say('▄▀▀░░░███▄█▄░░░░░░▄▀░░░░░░█▄░░')
    bot.say('█░░░░░███▄█▄░░░░░░▄▀░░░░░░░▀█▄')
notbad.commands = ['notbad']


def dealwithit(bot, input):
    bot.say('(•_•)')
    bot.say('( •_•)>⌐■-■')
    bot.say('(⌐■_■)')
dealwithit.commands = ['dealwithit']


def pirate(bot, input):
    bot.say('(•_•)')
    bot.say('( •_•)>⌐■')
    bot.say('(⌐■_•)')
pirate.commands = ['pirate', 'pirateup']


def glare(bot, input):
    bot.say('ಠ_ಠ')
glare.commands = ['glare', 'eyes', 'disapprove']


def facepalm(bot, input):
    bot.say('(>ლ)')
facepalm.commands = ['facepalm']


def tothemoon(bot, input):
   bot.say('┗(°0°)┛')
tothemoon.commands = ['tothemoon']


def postal(bot, input):
    choices = [
        "' ̿'\̵͇̿̿\з=(◕_◕)=ε/̵͇̿̿/'̿'̿ ̿'",
        "¯¯̿̿¯̿̿'̿̿̿̿̿̿̿'̿̿'̿̿̿̿̿'̿̿̿)͇̿̿)̿̿̿̿ '̿̿̿̿̿̿\̵͇̿̿\=(•̪̀●́)=o/̵͇̿̿/'̿̿ ̿ ̿̿",
    ]
    bot.say(choice(choices))
postal.commands = ['postal']


def ping(bot, input):
    bot.say('( •_•)O*¯`·.   |')
ping.commands = ['ping']


def pong(bot, input):
    bot.say('               |   .·´¯`°Q(•_• )')
pong.commands = ['pong']


def hi(bot, input):
    choices = ['o/', '\o']
    bot.say(choice(choices))
hi.commands = ['hi', 'ohai', 'hello', 'greetings', 'hola', 'bonjour']


def fail(bot, input):
    bot.say('http://www.youtube.com/watch?v=WtNHuqHWefU')
fail.commands = ['fail', 'dummy', 'dumber', 'stupid']


def boggle(bot, input):
    bot.say('           .--.')
    bot.say('         .\'    \'.')
    bot.say('        /  ~~~~  \\')
    bot.say('       ( __    __ )')
    bot.say('      /|<o->  <o->|\\')
    bot.say('     ( |    ^^    | )')
    bot.say('    _ ) \   __   / /')
    bot.say('   /##\  \_(__)_/ /')
    bot.say('  /####) )#\__// (')
    bot.say(' /####( |##| |#\  \\')
    bot.say('(#####| |##(_/##\_/\\')
    bot.say(' \####(_)###########\\')
    bot.say('   \#################)')
    bot.say('    \/##############/')
boggle.commands = ['boggle', 'thescream']


def yay(bot, input):
    bot.say('\o/')
yay.commands = ['yay', 'woot', 'w00t', 'friday']


def shithitsfan(bot, input):
    bot.say('https://www.youtube.com/watch?v=aZdp46Jen_w')
shithitsfan.commands = ['shithitsfan']


def fishslap(bot, input):
    bot.say('https://www.youtube.com/watch?v=IhJQp-q1Y1s')
fishslap.commands = ['fishslap']


def makeitrain(bot, input):
    bot.say('[̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅]')
    bot.say('')
    bot.say('[̲̅$̲̅(̲̅5̲̅)̲̅$̲̅]')
    bot.say('')
    bot.say('[̲̅$̲̅(̲̅1̲̅)̲̅$̲̅]')
makeitrain.commands = ['makeitrain']


def failboat(bot, input):
    bot.say('    __4_____')
    bot.say(' _  \F\A\I\L\\')
    bot.say('<\'\ /_/_/_/_/')
    bot.say(' ((____!_____/)')
    bot.say(' \\0\\0\\0\\0\\0\/')
    bot.say(' ~~~~~~~~~~~~~~~')
failboat.commands = ['failboat']


def beerme(bot, input):
    bot.say('     ,-"-.__,-"-.__,-"-..')
    bot.say('    ( C>  )( C>  )( C>  ))')
    bot.say('   /.`-_-\'||`-_-\'||`-_-\'/')
    bot.say('  /-"-.--,-"-.--,-"-.--/|')
    bot.say(' ( C>  )( C>  )( C>  )/ |')
    bot.say('(|`-_-\',.`-_-\',.`-_-\'/  |')
    bot.say(' `-----++-----++----\'|  |')
    bot.say(' |     ||     ||     |-\'')
    bot.say(' |     ||     ||     |')
    bot.say(' |     ||     ||     |')
    bot.say('  `-_-\'  `-_-\'  `-_-\'')
beerme.commands = ['beerme']


def halibut(bot, input):
    bot.say('><}}}}}*>')
halibut.commands = ['halibut']


def pabelanger(bot, input):
    bot.say('http://media.giphy.com/media/R4mn3MfNRmlCU/200.gif')
pabelanger.commands = ['pabelanger', 'paul', 'woahdance']


def dundundun(bot, input):
    bot.say('https://www.youtube.com/watch?v=cphNpqKpKc4')
dundundun.commands = ['dundundun']


def meditate(bot, input):
    bot.say('https://vimeo.com/132790897')
meditate.commands = ['meditate']


def roflcopter(bot, input):
    bot.say('        ROFL:ROFL:LOL:ROFL:ROFL')
    bot.say('          _________|________')
    bot.say(' L       /                 []')
    bot.say('LOL====== [] [] [] []  USA   \\')
    bot.say(' L       _____________________|')
    bot.say('                  | |')
    bot.say('               —————————–/-/')
roflcopter.commands = ['rofl', 'roflcopter']

def nakedping(bot, input):
    bot.say('https://blogs.gnome.org/markmc/2014/02/20/naked-pings/')
nakedping.commands = ['nakedping']
