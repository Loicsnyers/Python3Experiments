####  DELETE WEBEX "DEMO" SPACES
from webexteamssdk import WebexTeamsAPI
### Access Token 12 hours: https://developer.webex.com/docs/api/getting-started (login required)
access_token = "NzE4MDYyODctODNmOC00MTU5LWJlZDEtNjJiYzI2NzFmY2VlMTdjYjdjMDMtZjJh_P0A1_71b6b34c-abff-4407-ac50-5e62323aed80"
api = WebexTeamsAPI(access_token=access_token)
# Find all rooms that should be removed
all_rooms = api.rooms.list()

demo_rooms = [room for room in all_rooms if 'GROUP_1' in room.title]

# Delete all of the demo rooms
for room in demo_rooms:
    print("Deleting ... " + room.title)
    api.rooms.delete(room.id)