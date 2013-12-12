import re
import sys
import wunderground

class Phenny(object):
    def say(self, msg):
        print msg

wunderground.wuweather(Phenny(), re.match('()(.*)', sys.argv[1]))
