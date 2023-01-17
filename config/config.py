import os 
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("session_name", "BABUJulFz23H3QJWuE3KS0unPVVvSjWsTURwnSpE1xsIqsahxPi6vm38X1bHtevsvktDarJzCzDYnsKd2BGfsP7rcWoVjzl7p9PTk-HcL5t6E2yFW9Ckb8wWbwmFMtZ_gtUV4EAiezAq6nRMTG8URX7unLR0LyAuXu2rUzbJFLsjHm529qAMsXYrSmLCVkDNxKt4yKalFLhgyVJdYaDG9vlz3joV3WSjf6xpwyPECAjkEQKeklVoSReqnnqHtjI5FoPtgxTn7SDnuA4XU2Wn4Jx0S564Tc19WzjSJZJn0UJ5OfXFDmQ7kSSjqSA_wU8dVJ31mGENu6nS7hsMb_fD6tXNAAAAAVHgN2AA ")
API_ID = int(getenv("api_id", "27424907"))
API_HASH = getenv("api_hash", "0383f79be1b5d77b5b7a1b9d8359588f")
CHANNEL_ID = getenv("channel_id", "-524202205")
last_messages_amount = 50 
