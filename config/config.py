import os 
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("session_name", "BACZ4OcJ1XnS0ujrKs2ek9fwDwSXwqp_gz5g2MGZWIFA7OhIf-2lL4gIpFNvLwsHtFkk8d9X_65zsHOH1b93fzwGs-lGhHcAsx3ccsvE1OmPJ3V_c9R2nZAjeb5xFiMCVF4MGn1taH2aZ_A-Tp2_Y-khz165hQxWYWwx_m2TXaIK94xvUeholqufLjtFCnl5X9qo210YijW8GrpJJXla7LJlsPQms7-gWPoWKgQWSPLnuMCw4HmgaDCu784gnPb5iVyAsNtAO90pl6HLeghq7TF_Em4yg52L_xBsM95WRRSQsW-TSZ5pBAtzbJLi2QvzOZdZYhtRIxB0STyuF-h8-uh0UhAOHgA")
API_ID = int(getenv("api_id", "9316256"))
API_HASH = getenv("api_hash", "5a8a277605c3038129c536a9e79cd761")
CHANNEL_ID = getenv("channel_id", "-1001853845425")
last_messages_amount = 50 
