import os 
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("session_name", "BACGr1dXj2OY_Hymmbrv8-MTMOTqqiD1SDG0JiXwTAwAiAXPJ_OHO-0nGorgmeIy2JwRLdBuDHvgt3hJvu0x4t008W0vLUeE6Ry5F2Q803-OhMmnOyN_Tc1UG_jTpfTI5BNSV-puhcoIkmhMV61rD2WcUfkRE65ULVcGTcFqsG3o8gH0TUgIXv4gkbPGtQ6qfY1-rH57FA1_43lmd1RBYZ3hScVPGmqu4FZ5zhO2mi4tkZa_8yy9l8i8c0rLN6FOKt-CZKMetGyJ8ihGEgaOE0Jjb5651exR8kB0e6cgqJI0AVSDKqmgiTvwTmiGlQIPdhAWXPKr34WpqsTQbulCtSz3UhAOHgA")
API_ID = int(getenv("api_id", "23040522"))
API_HASH = getenv("api_hash", "56d5c718f86dab5c947e5cc80b6d6f30")
CHANNEL_ID = getenv("channel_id", "-890240622")
last_messages_amount = 90
