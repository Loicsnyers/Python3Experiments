import requests
from webexteamssdk import WebexTeamsAPI

# Replace with your Webex Teams API token
WEBEX_TEAMS_ACCESS_TOKEN = "MWI2MmExNWQtYWMyYy00ZWM1LWI0MDQtMjFlYjQ2OTk4M2ExMWRiMzA5MDItMWZj_P0A1_71b6b34c-abff-4407-ac50-5e62323aed80"

# Replace with your OpenWeatherMap API key
OPENWEATHERMAP_API_KEY = "dd4a8717685dce5c83d62addeee32dc0"

# Initialize the Webex Teams API
api = WebexTeamsAPI(access_token=WEBEX_TEAMS_ACCESS_TOKEN)

# Function to get weather information for a city using OpenWeatherMap API
def get_weather(city):
    weather_api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP_API_KEY}"
    response = requests.get(weather_api_url)
    data = response.json()

    if data["cod"] == 200:
        temperature_kelvin = data["main"]["temp"]
        temperature_celsius = temperature_kelvin - 273.15
        latitude = data["coord"]["lat"]
        longitude = data["coord"]["lon"]
        return temperature_celsius, latitude, longitude
    else:
        return None

# Function to send location data and receive a response
def send_location_to_bot(room_id, city):
    weather_data = get_weather(city)

    if weather_data:
        temperature_celsius, latitude, longitude = weather_data
        message = f"City: {city}\nTemperature: {temperature_celsius:.2f}°C\nLatitude: {latitude:.6f}\nLongitude: {longitude:.6f}"

        api.messages.create(roomId=room_id, markdown=message)
    else:
        api.messages.create(roomId=room_id, markdown=f"Unable to fetch data for {city}")

# Main function
if __name__ == "__main__":
    room_id = "ef819a60-6d9f-11ee-8978-6106fdd52d3e"  # Replace with the Webex Teams room where you want to send the location

    while True:
        city = input("Enter the city (or type 'exit' to quit): ")
        if city.lower() == "exit":
            break
        send_location_to_bot(room_id, city)
