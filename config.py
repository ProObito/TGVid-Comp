import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "20718334")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "4e81464b29d79c58d0ad8a0c55ece4a5") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7287471605:AAGP4g-5aI41I7j2zQCjP7yhZea5N_tb_BE") # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', '-1002155796547 -1001930406310 -1002072642438') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL", "mongodb+srv://Sukuna:Sukuna123@cluster0.xya73s9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","Cluster0") 

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "5585016974")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1002078429106')) # ⚠️ Required
    BOT_UPTIME = BOT_UPTIME  = time.time()
    START_PIC = os.environ.get("START_PIC", "https://envs.sh/qDs.jpg")

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


    caption = """
**File Name**: {0}

**Original File Size:** {1}
**Encoded File Size:** {2}
**Compression Percentage:** {3}

__Downloaded in {4}__
__Encoded in {5}__
__Uploaded in {6}__
"""
