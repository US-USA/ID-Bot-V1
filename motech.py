import pyrogram

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

from pyrogram import Client 
logging.getLogger("pyrogram").setLevel(logging.WARNING)
from BOTidSBot.Config import Config

if __name__ == "__main__" :
    plugins = dict(
        root="BOTidSBot"
    )
    mt_botz = Client(
        "BOTidSBot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins,
        workers=100
    )
    mt_botz.run()
 
