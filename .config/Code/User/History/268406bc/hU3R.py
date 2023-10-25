from webexteamssdk import WebexTeamsAPI
import requests

# Replace with your Webex Teams bot token
BOT_TOKEN = 'GZkNjlkYTAtM2E4Ni00MjAzLTlkOWUtYWMwMzU0NDdjMmRlNzM2YTkyMGYtOGRm_P0A1_71b6b34c-abff-4407-ac50-5e62323aed80'

# Initialize the Webex Teams API client
api = WebexTeamsAPI(access_token=BOT_TOKEN)

def on_message_created(event):
    message = event.data
    if message.personId == api.people.me().id:
        return

    if message.text.startswith('/weather'):
        location = message.text[8:].strip()  # Remove '/weather' from the message
        weather_data = get_weather(location)
        send_message(message.roomId, weather_data)

def send_message(room_id, text):
    api.messages.create(roomId=room_id, text=text)

def get_weather(location):
    if not location:
        return "Please provide a location for the weather, e.g., '/weather London'."

    # You can choose another weather API here
    # Replace 'YOUR_API_KEY' with the actual API key if required
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid=YOUR_API_KEY'
    response = requests.get(url)
    data = response.json()

    if data['cod'] == 200:
        temperature = data['main']['temp'] - 273.15  # Convert to Celsius
        weather = data['weather'][0]['description']
        return f"The weather in {location} is {weather} with a temperature of {temperature:.2f}°C."
    else:
        return "Sorry, I couldn't retrieve the weather data for that location."

api.messages.on_created = on_message_created

if __name__ == "__main__":
    input("Weather Bot is running. Press Enter to exit...\n")