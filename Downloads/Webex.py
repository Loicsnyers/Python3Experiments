import requests

# Replace with your OpenWeatherMap API key
WEATHER_API_KEY = 'dd4a8717685dce5c83d62addeee32dc0'

def get_weather_info(location):
    if not location:
        return "Please provide a location."

    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={WEATHER_API_KEY}'
    response = requests.get(url)
    data = response.json()

    if data['cod'] == 200:
        temperature = data['main']['temp'] - 273.15  # Convert to Celsius
        lat = data['coord']['lat']
        lon = data['coord']['lon']
        return f"The weather in {location}:\n- Temperature: {temperature:.2f}°C\n- Latitude: {lat}\n- Longitude: {lon}"
    else:
        return "Sorry, I couldn't retrieve the weather data for that location."

# Ask for user input and get weather information
city = input("Enter a city: ")
weather_info = get_weather_info(city)
print(weather_info)

