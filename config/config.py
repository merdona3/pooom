import os 
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("session_name", "BACdw678eyTnXDgl5UYxRzX_2SueNhGnCqrGKdt-iUqnCTysZubIPOlGXK-KTDlKabUI55vrnSz2ehEc3iRNktXzzTlyAhAwnZ3RKpPE7CWzOq4OnlH-2R7Tk91lWsG9SwXbO8Dg9Tzu2EB3pO26BgVZ35vR6353t2lKnsrS3K5uVKIgob3xwf-wi3rbT63NvxLj7Sb7eT2ccHoTYqG5vFc8orNDEt9RfLqULWELcLCqYEswvTkmwbPXOmRMlsjFDFhhC1ckXlzWLS_SybZhedUanStX3Rh1pNJluK_ov8WphsBlDKc8uLiHtdOGfvcdXNxPZyxHKfkE4VGZwyAXv_shAAAAAVHgN2AA")
API_ID = int(getenv("api_id", "27424907"))
API_HASH = getenv("api_hash", "0383f79be1b5d77b5b7a1b9d8359588f")
CHANNEL_ID = getenv("channel_id", "-524202205")
last_messages_amount = 90
