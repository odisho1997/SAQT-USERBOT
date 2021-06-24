#   ICSS - USERBOT
#   TELE - @NIIIN2

#  ======================================================= #

from userbot.Config import Config

USERID = Config.OWNER_ID 
ALIVE_NAME = Config.ALIVE_NAME
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "SAQT-USERBOT"
mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"

#  ======================================================= #
