import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "29732337"))
  API_HASH = os.environ.get("API_HASH", "27c900a8bac51da6d0fd91aad09ef779")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6561956588:AAFElWnnqYYrgamjMlY3NkFGR_L3RkXb_hU")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "MBfilestoreBot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "2014221486"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', ")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "5790619836"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://dokefiv235:ZHnCNX9nbViXFMuZ@snapdemon1.x0iinji.mongodb.net/?retryWrites=true&w=majority")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "2038807427")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "2014221486"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [MB FileStore Bot](https://t.me/MBfilestoreBot)
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [Jᴀcκ々sᴘᴀʀʀow™](https://telegram.me/Capta1_n)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/Capta1_n)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

💲 Activate Bot First ✅

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
"""
