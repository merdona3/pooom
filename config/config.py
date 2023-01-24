import os 
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("session_name", "BACGr1dXj2OY_Hymmbrv8-MTMOTqqiD1SDG0JiXwTAwAiAXPJ_OHO-0nGorgmeIy2JwRLdBuDHvgt3hJvu0x4t008W0vLUeE6Ry5F2Q803-OhMmnOyN_Tc1UG_jTpfTI5BNSV-puhcoIkmhMV61rD2WcUfkRE65ULVcGTcFqsG3o8gH0TUgIXv4gkbPGtQ6qfY1-rH57FA1_43lmd1RBYZ3hScVPGmqu4FZ5zhO2mi4tkZa_8yy9l8i8c0rLN6FOKt-CZKMetGyJ8ihGEgaOE0Jjb5651exR8kB0e6cgqJI0AVSDKqmgiTvwTmiGlQIPdhAWXPKr34WpqsTQbulCtSz3UhAOHgA")
API_ID = int(getenv("api_id", "9316256"))
API_HASH = getenv("api_hash", "5a8a277605c3038129c536a9e79cd761")
CHANNEL_ID = getenv("channel_id", "-687819550")
last_messages_amount = 90
