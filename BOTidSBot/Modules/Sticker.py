from pyrogram import filters
from pyrogram import Client as BOTidSBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from BOTidSBot.Translation import Translation
from BOTidSBot.Config import Config

UPDATE_CHANNEL=Config.UPDATE_CHANNEL # Update Channel Forces Subscribe
BOT_USERNAME=Config.BOT_USERNAME # ReStart Option 
JOIN=Translation.JOIN_TEXT # Button Text (Update Channel)
TRY=Translation.TRY_TEXT # Button Text (Update Channel)
SUB_TEXT=Translation.FSUB_TEXT # FSUB Information Text

# ADDED STICKER ID GETTING. COPYRIGHT UNDER AND RE-GENERATED AND
#  BY @TE_GitHub AND TO @us7a5

@BOTidSBot.on_message(filters.command(["stickerid"]))
async def stickerid(bot, message):   
    update_channel = UPDATE_CHANNEL
    if update_channel:
        try:
            user = await motech.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked out":
               await update.reply_text("🔮 𝚂𝙾𝚁𝚁𝚈 𝙳𝚄𝙳𝙴, 𝚈𝙾𝚄 𝙰𝚁𝙴 **🅤︎🅢︎🅐︎ 🇺🇸**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"𝙹𝙾𝙸𝙽 @{Channel User Name} 𝚃𝙾 𝚄𝚂𝙴 𝙼𝙴") From Motech.py
            await update.reply_text(
                text=f"<b>{SUB_TEXT}</b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=f"{JOIN}", url=f"t.me/{UPDATE_CHANNEL}")],
                    [ InlineKeyboardButton(text=f"{TRY}", url=f"https://t.me/{BOT_USERNAME}?start=try")]
              ])
            )
            return
        except Exception:
            await update.reply_text(f"@{UPDATE_CHANNEL}")
            return  
    if message.reply_to_message.sticker:
       await message.reply(f"**𝚈𝙾𝚄𝙰 𝚂𝚃𝙸𝙴𝙲𝙺𝙴𝚂 𝙸𝙳 𝙸𝚂 **  \n `{message.reply_to_message.sticker.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.sticker.file_unique_id}`", quote=True)
    else: 
       await message.reply(" 𝙷𝙼𝙼𝙼 𝙸𝚃'𝚂 𝙽𝙾𝚃 𝙰 𝚂𝚃𝙸𝙲𝙺𝚆𝚁...!!!")
    
