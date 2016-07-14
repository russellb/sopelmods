import json
import re
import sys
import urllib
from sopel import module


def wuweather_full(bot, input, verbose=True):
    loc = input.group(2)
    pws = loc.startswith('pws:') and '1' or '0'

    #grab weather from api
    try:
        weather = json.loads(urllib.urlopen('http://api.wunderground.com/api/587a76efcc30bee2/conditions/almanac/astronomy/forecast/pws:' + pws + '/q/' + loc +'.json').read())
    except:
        return
    if not weather:
        return

    #does the response contain an error
    if 'error' in weather['response']:
        bot.say("wuweather: %s" % weather['response']['error']['description'])
        return
    #does the response contain extra 'results'
    elif 'results' in weather['response']:
        output = 'wuweather: Ambiguous Search, options: '
        counter = 0
        for index in weather['response']['results']:
            if counter == 0:
                output += "%s %s %s " % (index['city'], index['state'], index['country'])
            else:
                output += "/ %s %s %s " % (index['city'], index['state'], index['country'])                
            counter += 1
        bot.say(output)
        return

    #if we made it here, everything should be good
    try:
        #format the city name
        if pws == '1':
            loc_key = 'observation_location'
        else:
            loc_key = 'display_location'
        city = "[%s, %s, %s]" % \
        (weather['current_observation'][loc_key]['city'],
        weather['current_observation'][loc_key]['state'],
        weather['current_observation'][loc_key]['country'])

        #output the averages, sunrise, moon
        #some locations don't have an almanac
        if weather['almanac']['airport_code'] != "":
            almanac_output = "Avg High: %sF, %sC Low: %sF, %sC " % \
            (weather['almanac']['temp_high']['normal']['F'],
            weather['almanac']['temp_high']['normal']['C'],
            weather['almanac']['temp_low']['normal']['F'],
            weather['almanac']['temp_low']['normal']['C'])
        else:
            almanac_output = ""

        if verbose:
            #output sunrise w/ almanac if available
            bot.say("%s %sSunrise: %s:%s Sunset: %s:%s" % \
            (city,
            almanac_output,
            weather['moon_phase']['sunrise']['hour'],
            weather['moon_phase']['sunrise']['minute'],
            weather['moon_phase']['sunset']['hour'],
            weather['moon_phase']['sunset']['minute']))

        #output the current weather
        bot.say("%s Current: %s %sF, %sC (Feels like: %sF, %sC), Humidity: %s, Wind: %s" % \
        (city,
        weather['current_observation']['weather'],
        weather['current_observation']['temp_f'],
        weather['current_observation']['temp_c'],
        weather['current_observation']['feelslike_f'],
        weather['current_observation']['feelslike_c'],
        weather['current_observation']['relative_humidity'],
        weather['current_observation']['wind_string']))

        if not verbose:
            return

        #output first 3 days of forcast (today, tomorrow, second day)
        counter = 0
        for index in weather['forecast']['simpleforecast']['forecastday']:
            if counter == 0:
                day = 'Today'
            elif counter == 1:
                day = 'Tomorrow'
            else:
                day = index['date']['weekday']

            bot.say("%s %s: %s [POP: %s%%] [High: %sF, %sC Low: %sF, %sC] Humidity: [Max: %s%%, Min: %s%%, Avg: %s%%] Wind: [%smph, %skph]" % \
            (city,
            day,
            index['conditions'],
            index['pop'],
            index['high']['fahrenheit'],
            index['high']['celsius'],
            index['low']['fahrenheit'],
            index['low']['celsius'],
            index['maxhumidity'],
            index['minhumidity'],
            index['avehumidity'],
            index['avewind']['mph'],
            index['avewind']['kph']))
            counter +=1
            if counter >= 3: break
        bot.say("%s URL: %s" % (city, weather['current_observation']['forecast_url']))
    except:
        return


def wuweatherverbose(bot, input):
    return wuweather_full(bot, input)
wuweatherverbose.commands = ['wuweatherverbose']


def wuweather(bot, input):
    return wuweather_full(bot, input, verbose=False)
wuweather.commands = ['wuweather']


if __name__ == '__main__':
    import tests.utils
    wuweather(tests.utils.Sopel(), re.match('()(.*)', sys.argv[1]))
