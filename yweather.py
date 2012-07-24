import urllib
from xml.dom import minidom
import sys

WEATHER_URL = 'http://xml.weather.yahoo.com/forecastrss?p=%s'
WEATHER_NS = 'http://xml.weather.yahoo.com/ns/rss/1.0'

def weather_for_zip(zip_code):
    url = WEATHER_URL % zip_code
    dom = minidom.parse(urllib.urlopen(url))
    forecasts = []
    for node in dom.getElementsByTagNameNS(WEATHER_NS, 'forecast'):
        forecasts.append({
            'date': node.getAttribute('date'),
            'low': node.getAttribute('low'),
            'high': node.getAttribute('high'),
            'condition': node.getAttribute('text')
        })
    ycondition = dom.getElementsByTagNameNS(WEATHER_NS, 'condition')[0]
    return {
        'current_condition': ycondition.getAttribute('text'),
        'current_temp': ycondition.getAttribute('temp'),
        'forecasts': forecasts,
        'title': dom.getElementsByTagName('title')[0].firstChild.data
    }

def yweather(phenny, input):
    zip = input.group(2)
    try:
        forecast = weather_for_zip(zip) 
    except:
        phenny.say("Failed")
        return
    phenny.say('[%s] %s, %s degrees' % (forecast['title'].split('- ', 1)[1], forecast['current_condition'], forecast['current_temp']))
yweather.commands = ['yweather']

