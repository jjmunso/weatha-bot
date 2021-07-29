'''
Automatic Forecast Collection for WeathaBot (Tester to be appended to main program)
Software 3-4
By Jeremie Munso
20/07/2021 @ St Leonards College


USING Python OPEN WEATHER MAP

USING API KEY f9b5ecc7fdf88f18cc9459a629a88455 :D lol
'''


import requests, json, datetime


api_key = "f9b5ecc7fdf88f18cc9459a629a88455"
lat = "-37.814"
lon = "144.96332"
url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
response = requests.get(url)
data = json.loads(response.text)
print(data)


'''
# API KEY
api_key = "API"
complete_url = "http://api.openweathermap.org/data/2.5/weather?" + "appid=" + api_key + "&q=" + "Melbourne"
response = requests.get(complete_url)

x = response.json()

if x["cod"] != "404":
    y = x["main"]
    z = x["rain"]
    current_temp_max = y["temp_max"]
    current_temp_min = y["temp_min"]
    current_rainfall = z["3h"]
    print(" Temperature max (in celsius unit) = " +
                    str(current_temp_max-273.15) +
          "\n Temperature min (in celsius unit) = " +
                    str(current_temp_min-273.15) +
          "\n rainfall (in mm) = " +
                    str(current_rainfall-273.15))
else:
    print(" City Not Found ")
    '''
