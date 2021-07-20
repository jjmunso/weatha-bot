'''
Automatic Forecast Collection for WeathaBot (Tester to be appended to main program)
Software 3-4
By Jeremie Munso
20/07/2021 @ St Leonards College


USING Python OPEN WEATHER MAP

USING API KEY f9b5ecc7fdf88f18cc9459a629a88455
'''

# Python program to find current
# weather details of any city
# using openweathermap api

# import required modules
import requests, json

# Enter your API key here
api_key = "f9b5ecc7fdf88f18cc9459a629a88455"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name
city_name = "Melbourne"

# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

# get method of requests module
# return response object
response = requests.get(complete_url)

# json method of response object
# convert json format data into
# python format data
x = response.json()

# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
if x["cod"] != "404":

    # store the value of "main"
    # key in variable y
    y = x["main"]
    z = x["rain"]

    # store the value corresponding
    # to the "temp" key of y
    current_temp_max = y["temp_max"]

    # store the value corresponding
    # to the "pressure" key of y
    current_temp_min = y["temp_min"]

    # store the value corresponding
    # to the "humidity" key of y
    current_rainfall = z["3h"]


    # print following values
    print(" Temperature max (in kelvin unit) = " +
                    str(current_temp_max) +
          "\n Temperature min (in kelvin unit) = " +
                    str(current_temp_min) +
          "\n humidity (in percentage) = " +
                    str(current_rainfall))
else:
    print(" City Not Found ")
