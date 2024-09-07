import requests

weather_key = "b444c5dddd9190f1e31244703020fa3f"
weatherAPI_url = "https://api.openweathermap.org/data/2.5/weather"
location_key = "564226ef90f34ac9be8c25addd3c1d0e"
location_url = "https://api.geoapify.com/v1/geocode/search"

print("WELCOME TO WEATHER APP")
city = input("Enter your city: ")
state = input("Enter your state: ")

location_paramters={
    "apiKey": location_key,
    "city": city,
    "state": state,
}

response = requests.get(location_url,params=location_paramters)
data  = response.json()
longitude = data["features"][0]["properties"]["lon"]
latitude =  data["features"][0]["properties"]["lat"]

weather_parameters ={
    "lat" : latitude,
    "lon" : longitude,
    "appid": weather_key,
    "units": "metric"
}

response = requests.get(weatherAPI_url,params=weather_parameters)
data  = response.json()

description = data["weather"][0]["description"]
humidity = data["main"]["humidity"]
temperature = data["main"]["temp"]
wind_speed = data["wind"]["speed"]

print(f"Weather at {city.title()},{state.title()} is ")
print(f"Weather Description: {description} \nTemperature: {temperature}°C \nHumidity: {humidity}% \nWind speed: {wind_speed}m/s")
