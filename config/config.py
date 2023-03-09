import os 
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("session_name", "1BJWap1wBu5aPPkRebSEsXG3sUX-XgFFV6bjTm09svsu_jW1NM6nGQX86zKQS8lum3AqJhyekn_oppUTZixY8_BMAk-Ill7BrEse98_Q2QfCTGR72D0AhUl46cEjepFRTeALhUEmOXUfGaegfoT0Bs-38dJSgEClAHicLqCGAYY4QH4XqLRkzN9UToTASOcgT-qK7e2y95TAfGuQhOyiaUM59Bl5RgZT717_iBS3j63ad0ildxGwdifmdeNY6svf6V1LqfpR_otRWqry9JTpoUnFWFxxy5RNS-EeObAvSQtbB4UM2U22vjqXcPGPaaEjVVys6aVXrLgxIDClpUfCY-jgK6cne-tw=")
API_ID = int(getenv("api_id", "9316256"))
API_HASH = getenv("api_hash", "5a8a277605c3038129c536a9e79cd761")
CHANNEL_ID = getenv("channel_id", "-965159896")
last_messages_amount = 90
