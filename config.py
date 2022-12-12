import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
class Config(object):
    log = True
    APP_ID = getenv("API_ID","27340010")
    API_HASH = getenv("API_HASH","76297aded23b5e3e61480d82a4f25771")
    TOKEN = getenv("TOKEN", "5959631394:AAGZAnzjaDJt0xWnwei-9rXRIuLQL5PHhwg")
    OWNER_ID = getenv("OWNER_ID","1036568809")
    STRING_SESSION = getenv("STRING_SESSION","1BVtsOMUBuwajK-mmjiNOsezQpBHRacgh3IX4wFBhj0n-w-j8logzqJf9zRx6S52gQtji_EtW9IfxVZKBc1ihM57cjWjWvkx_4uO8ExZbytxzssn-LKYGX4wC_kqMAK7-PHkW8sAA-6b34ktacfnY0xswqisDEPmuq9O5WjfIDCwXbGkgDmbpbmKab1MlD21Urh4SItk1Q6G7PKzW-oFSGsCB5CHxoRNDG9_WKM_CDp5Mr61bk5Scgfh-L-w9cCimmOm9x_7s5wjL7UxKJUJqZZGCJ-SKufQMRzhYBKy-YrEI0V-hWIEO2zVet_4cIUJN9jFrphTHcNeSCDapLyBnJfWNz0YuuIc=")
    OWNER_USERNAME = getenv("OWNER_USERNAME", "wodlike")
    DB_URI = getenv("DATABASE_URL" , "postgres://altxcmqe:bqNFRK-cFk3fnTGl4trJHNIxgpRX6SxA@heffalump.db.elephantsql.com/altxcmqe")
    DB_URI = DB_URI.replace("postgres", "postgresql")
    MESSAGE_DUMP = getenv("MESSAGE_DUMP", "-1001878165791")
    GBAN_LOGS = getenv("GBAN_LOGS", "-1001878165791")
    SYS_ADMIN = getenv("SYS_ADMIN", "1669178360")
    DEV_USERS = getenv("DEV_USERS", "1669178360")
    LOAD = getenv("LOAD")
    WEBHOOK = False
    SPB_MODE = True
    DROP_UPDATES = False
    DEBUG = False
    URL = None
    INFOPIC = True
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    BAN_STICKER = getenv("BAN_STICKER", "")
    ALLOW_EXCL = True
    CUSTOM_CMD = False
    CASH_API_KEY = getenv("CASH_API_KEY", "https://www.alphavantage.co/support/#api-key")
    TIME_API_KEY = getenv("TIME_API_KEY", "https://timezonedb.com/api")
    WALL_API = getenv("WALL_API", "https://wall.alphacoders.com/api.php")
    spamwatch_api = getenv("spamwatch_api", "https://t.me/SpamWatchBot")
    SPAMMERS = getenv("SPAMMERS", "")
    LASTFM_API_KEY = getenv("LASTFM_API_KEY", "https://www.last.fm/api/account/create")
    CF_API_KEY = getenv("CF_API_KEY", "coffehouse.intellivoid.net")
    BOT_API_URL = getenv("BOT_API_URL", "https://api.telegram.org/bot")
    BOT_API_FILE_URL = getenv("BOT_API_FILE_URL", "https://api.telegram.org/file/bot")
    SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1669178360").split()))
    ZAID_USER = list(map(int, getenv("DEV_USERS", "1669178360").split()))
    NO_LOAD = list(map(int, getenv("NO_LOAD", "").split()))
