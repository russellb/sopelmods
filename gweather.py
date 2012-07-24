import pywapi

def gweather(phenny, input):
    loc = input.group(2)
    try:
        weather = pywapi.get_weather_from_google(loc)
    except:
        return

    if not weather:
        return

    try:
        result = "[%s] %s, %sF, %sC, %s, %s" % \
            (weather['forecast_information']['city'],
                weather['current_conditions']['condition'],
                weather['current_conditions']['temp_f'],
                weather['current_conditions']['temp_c'],
                weather['current_conditions']['humidity'],
                weather['current_conditions']['wind_condition'])
    except:
        return

    phenny.say(result)
gweather.commands = ['gweather']
