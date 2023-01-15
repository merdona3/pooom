import os 
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("session_name", "BACM01YnPd5ku2fcBtgmeiWWMhsoV4ocNPPDwh2qsTNLWp0roVRp8VNjA9F4zXJk3Qm5pUGuCjYnLrxTyRq92yz_yXn6pomxaV-5VIhOBF1U2gVBgv1ozlCDozEuqJnOuTteibKwg7v1Z5IgwWGVLRrH-HmYnNUPM9FzEof_autmHndfYS3NYzZ2_g92KAgyLh4_zqNDVtyu2oHcDHszYn-FmYDlo3G8VyPpWKzkmRSJsDp8LpODfclUqRixiSrhY9Kpir9g3YDk8Q0tjGJAT8gYJVmc-OFwjK_s2q_os23d05K_yPLa0y12p6h2sNJ2yb9ockqgEvcTEY5ASnQiPMg-AAAAAVHgN2AA")
API_ID = int(getenv("api_id", "9316256"))
API_HASH = getenv("api_hash", "5a8a277605c3038129c536a9e79cd761")
CHANNEL_ID = getenv("channel_id", "-1001853845425")
last_messages_amount = 50 
