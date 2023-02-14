import os 
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("session_name", "BAFfkgoAJ0PCH1xn2zuxN3psiVT0X-WTYgx1ya5N7CCAQZzNuZU39mVQmGS5O1xueZDSvCM_kIbGE2i9QgLex0sZ20ntjZm0pZCrWzzqPddHF8yJ7tqTYDkap-nKml-mEtf5Oi9B10ermCf0RAD3J0e4-Xp7uLkAGxOEb_k9uZJZik_rGVE8pi-26pk6_gO3hlquvz2KpJFCpfaPSqB59cDQeeqHm4H7O-U--mD1410VsupX44HVwiI6T5_HP0ouZ-UiUsdSFsoq5jVO9UZDiGiHv7qNmzmz9bnPwLG8vq36e7JGSFYpCPiJ3TVolzvnGYQoiYJivKyXFRFdV7xmaSfYVE6z4gAAAAFx92mLAA")
API_ID = int(getenv("api_id", "23040522"))
API_HASH = getenv("api_hash", "56d5c718f86dab5c947e5cc80b6d6f30")
CHANNEL_ID = getenv("channel_id", "-890240622")
last_messages_amount = 90
