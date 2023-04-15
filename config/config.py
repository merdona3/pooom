import os 
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("session_name", "BACOJ6AAYHEuOVcLdxTZWw_tz5Kwfd3_VSAyhyj9Quz4fZNkDPYV9yV_qwVuogASTP6ZhOciVZ5j76gulE1Rb8-S9GHCRMIiTaYBxyUkWRCybZ4CyVdpfB4Kck7LEt7HnQsiQQQSUMZoFlAOizjvaZW2fH86IGvpYAKgpilZQkX2cy4QHuQgkpv1dC7SG4DtYVhHaMA57j4aStQTjurgSO5SkgDcHF2Q7-l14CXzTiQooTuXbf_XAO2g1YTn3lg9CBw8ngkCxJNdMA7bXpuo3S7mUqLPwqqnoFhZ0hjn9uZENGT9O9vLYatJw_DudSAbfJB0kdIxNqDBwiVusREZeO266ZbregAAAAFQVNUKAA")
API_ID = int(getenv("api_id", "9316256"))
API_HASH = getenv("api_hash", "5a8a277605c3038129c536a9e79cd761")
CHANNEL_ID = getenv("channel_id", "-858719770")
last_messages_amount = 90
