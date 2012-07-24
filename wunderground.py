import urllib
import json

def wuweather(phenny, input):
    loc = input.group(2)

    #grab weather from api
    try:
        weather = json.loads(urllib.urlopen('http://api.wunderground.com/api/587a76efcc30bee2/conditions/almanac/astronomy/forecast/pws:0/q/' + loc +'.json').read())
    except:
        return
    if not weather:
        return

    try:
        #format the city name
        city = "[%s, %s, %s]" % \
        (weather['current_observation']['display_location']['city'],
        weather['current_observation']['display_location']['state'],
        weather['current_observation']['display_location']['country'])

        #output the averages, sunrise, moon
        output = "%s Avg High: %sF, %sC Low: %sF, %sC / Sunrise: %s:%s Sunset: %s:%s / Moon: %s%%\n" % \
        (city,
        weather['almanac']['temp_high']['normal']['F'],
        weather['almanac']['temp_high']['normal']['C'],
        weather['almanac']['temp_low']['normal']['F'],
        weather['almanac']['temp_low']['normal']['C'],
        weather['moon_phase']['sunrise']['hour'],
        weather['moon_phase']['sunrise']['minute'],
        weather['moon_phase']['sunset']['hour'],
        weather['moon_phase']['sunset']['minute'],
        weather['moon_phase']['percentIlluminated'])

        #output the current weather
        output += "%s Current: %s %sF, %sC Humidity: %s, Wind: %s\n" % \
        (city,
        weather['current_observation']['weather'],
        weather['current_observation']['temp_f'],
        weather['current_observation']['temp_c'],
        weather['current_observation']['relative_humidity'],
        weather['current_observation']['wind_string'])

        #output first 3 days of forcast (today, tomorrow, second day)
        counter = 0
        for index in weather['forecast']['simpleforecast']['forecastday']:
            counter +=1
            output += "%s %s: %s [Chance of Percipitation: %s%%] [High: %sF, %sC Low: %sF, %sC] Humidity: [Max: %s, Min: %s, Avg: %s] Wind: [%smph, %skph]\n" % \
            (city,
            index['date']['weekday'],
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
            index['avewind']['kph'])
            if counter >= 2: break
    except:
        return

    #print output
    phenny.say(output)

wuweather.commands = ['wuweather']
