import os 
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

session_name = getenv("session_name", "1BJWap1sBuxhhasn3x26wSC3RkUMn_l5GcF0ZMYX07wdwj73PC3Du9Q4-hiiM5hAeSjuwhS6ZEh4xkQtxHuH4X4k7qr-KVpaWnVXUY60NeVHQAeW-tNIMTgBIuv3Zg2Grsu8kTL5PISQ6WRX4PnLWxzqg9HIN5tcVCY8v_2dp1kqhNm-9vYqPinKWPjeCxQ0osCzhVRx1_KJEnJPcpvGR3oRFWKvdlhOOXHahtOpfjO9SsFj7VL351BeHcBCTtWZ0zjYt5R7FE7wQHdnFvhIfSwhgPMbUH3pSKr-8AYq5MyaQpVqQDIPC0upIUvAw3oS1R1ZiKbGnGQAlh_X4rV3u_24J9eJTJYU=")
api_id = int(getenv("api_id", "28113782"))
api_hash = getenv("api_hash", "72ac0911ddf53a020560e0dde09650a6")
channel_id = getenv("channel_id", "")
last_messages_amount = 90
