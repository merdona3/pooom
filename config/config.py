import os 
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("session_name", "BADAs-QDCS-nZZk5XmxCRGeRmlUeEM-PIgCh4PM1tRgRz-7nD5Sa9oO2zzUvQWJsvKLovmXOGqRtyCJrfRXR4kspj2UcyraYBwzjBHkobQZPRnSsZ96BtT49Xb0dlVpYbs7yUqXBytB5qqgPxEJA4Qce4SMECZ0HjEd_sIZLL73nrLJ4p1sN-X35AGLHw_klQa5FMNq8-E_11MfzBdSNmwARag4qzwjda8-DaM30ZQixXVjaENG1vxaIJD0cd9Zk3-uDsIkSzvphsuP588qJF6Z6eFNbDkPnjqgIKy5aBWnGoSr5d1b8VnUtOjiBDQBVdZFHXKlHR-8MZBcbUi4TnS2UAAAAAS9MITIA ")
API_ID = int(getenv("api_id", "29119916"))
API_HASH = getenv("api_hash", "066ac8983fb76ff3d96e100732eb09b3")
CHANNEL_ID = getenv("channel_id", "-834903726")
last_messages_amount = 50 
