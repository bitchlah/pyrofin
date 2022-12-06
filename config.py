# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

from base64 import b64decode
from distutils.util import strtobool
from os import getenv

from dotenv import load_dotenv

load_dotenv("config.env")


ALIVE_EMOJI = getenv("ALIVE_EMOJI", "🔥")
ALIVE_LOGO = getenv("ALIVE_LOGO", "https://telegra.ph/file/7b2a3fa167686dfaa3da8.jpg")
ALIVE_TEKS_CUSTOM = getenv("ALIVE_TEKS_CUSTOM", "Hey, I am ALBY-PYROBOT 🔥")
API_HASH = getenv("API_HASH", "4599e8f16f52517e608b719fa4665467")
API_ID = int(getenv("API_ID", "16436100"))
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001638078842]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BOT_VER = "1.1.5@main"
BRANCH = "main"
CHANNEL = getenv("CHANNEL", "ruangprojects")
CMD_HANDLER = getenv("CMD_HANDLER", ".")
DB_URL = getenv("DATABASE_URL", "")
GIT_TOKEN = getenv(
    "GIT_TOKEN",
    b64decode("Z2hwX01oY1hFS3dJZWRwa0ZteGxnb1lqWnNXZkRGYkl2aTNrY09vVQ==").decode(
        "utf-8"
    ),
)
GROUP = getenv("GROUP", "ruangdiskusikami")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
PMPERMIT_PIC = getenv("PMPERMIT_PIC", None)
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "True"))
REPO_URL = getenv(
    "REPO_URL",
    b64decode("aHR0cHM6Ly9naXRodWIuY29tL1B1bnlhQWxieS9QWVJPQUxCWQ==").decode("utf-8"),
)
STRING_SESSION1 = getenv("STRING_SESSION1", "BQAhIHQALBbP8f56NDXoJZNjOd1S4p0MAg3hwSf6O4QyQQWnlsxVLqgPZRQsbmahlD1vgsNMMzYu-moLdIKCDQWLkBHStxsdvMn7ZmTZcjhv0p4ATo-mmDN_89fJR0ipNYp5-wTFazMB-NcWWFlNukjgSWIuRXQ7gTI5AlDcyjIMq1bc05iyfu6dUfW1MKNXkPuPeBEYVTdCarfVBrpSgNFYI7vLIbLVc2Ha-ui-Fv3WZVTWKnWw3hGsyGHTMRruWeSPwmLh21ieKQo12zAh8OOLgy1XXz2iJv5xAJXb0nuGQwJosVhsaTZRob6si53x5mCOAXIzi4icb-5JuRYnwRJVfdLQ8AAAAAAwSxg3AA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
