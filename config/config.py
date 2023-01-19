import os 
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("session_name", "BAAzhU0mRiqiczUOdAHjaLc210LjldlmgTUHMEgMHS_97lMqGYdP3s-giNQYkdTKK5YfGeoBa-UqE8zIwmyOisJmD1UQkS9hR7nAAT8KskxWxOGk4KSqdo3-s2Pq4GkI5cd7LiAkChch8svvugULUCstxTAdhyNisNc9LGkLTADA7uB4Q4dr5BYhDOunTA1oG4rbt6QtBOuswROvpg_PUVskZ02FfwX2jozVTw3Ldph7Iz5yJYGV52PlaCsfdVQgAFpNcDJKwt02wvEIytbLuynMD3NqrF4NsHjpzMA2JSXRaPT-Ej4tIAPCWgBmTne3J1swJ5tq9apjoVPCp66nh2lqAAAAAS9MITIA")
API_ID = int(getenv("api_id", "29119916"))
API_HASH = getenv("api_hash", "066ac8983fb76ff3d96e100732eb09b3")
CHANNEL_ID = getenv("channel_id", "-834903726")
last_messages_amount = 50 
