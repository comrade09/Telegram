import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
class Config(object):
    log = True
    APP_ID = getenv("API_ID", "6435225")
    API_HASH = getenv("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    TOKEN = getenv("TOKEN", "5744245230:AAFuipcdKfCHL5xyo0agw1BDO1JCdC2WQEQ")
    OWNER_ID = getenv("OWNER_ID","1036568809")
    STRING_SESSION = getenv("STRING_SESSION","1BVtsOLwBux8CljXK6g6j0eE8hy-q430aLSWDY0kPtgB2yMkEqu0LlmKNobODQn_5_0aVmrbmX9iTeSn8v6EeTvp_sW7v6ErXLR13jHY9f2laudhC3qn3OkVsTGEmgJRXnVYhlHWI4T_dd8bOjjn0pqKddBPyXoXxF2uVHBIGksIvK5LACAA9PciNOLG5guVXHoY4bmuLoGMieAP0XKAL2GEZu5FPwfIUdr3pz-DWqgbV7obGFx1mvpTzAwGfyvni6pt9U2y5ZDDDyDixq5TBPINsMFnk-2OzZqbKMrkOX_vEDx8xv0OhNsyLMCN608F9R5VQ90AV01WQJayDZLq2qPNbltWmAtQ=")
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
