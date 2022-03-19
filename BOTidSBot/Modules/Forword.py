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

@BOTidSBot.on_message(filters.private & filters.forwarded)
async def info(motech, msg):
    update_channel = UPDATE_CHANNEL
    if update_channel:
        try:
            user = await motech.get_chat_member(update_channel, msg.chat.id)
            if user.status == "kicked out":
               await update.reply_text("🔮 Sorry Dude, You are **🅤︎🅢︎🅐︎ 🇺🇸**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{Channel User Name} To Use Me") From Motech.py
            await msg.reply_text(
                text=f"<b>{SUB_TEXT}</b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=f"{JOIN}", url=f"t.me/{UPDATE_CHANNEL}")],
                    [ InlineKeyboardButton(text=f"{TRY}", url=f"https://t.me/{BOT_USERNAME}?start=try")]
              ])
            )
            return
        except Exception:
            await msg.reply_text(f"@{UPDATE_CHANNEL}")
            return
    if msg.forward_from:
        text = "<u>𝙵𝙾𝚁𝚆𝙰𝚁𝙳 𝙸𝙽𝙵𝙾𝚁𝙼𝙰𝚃𝙸𝙾𝙽 💚🐸</u> \n\n"
        if msg.forward_from["is_bot"]:
            text += "<u>💛 𝙱𝙾𝚃 𝙸𝙽𝙵𝙾</u>"
        else:
            text += "<u>💛 𝚄𝙰𝙴𝚁 𝙸𝙽𝙵𝙾</u>"
        text += f'\n\n💛 𝙽𝙰𝙼𝙴 ➻ {msg.forward_from["first_name"]}'
        if msg.forward_from["username"]:
            text += f'\n\n💛 𝚄𝚂𝙴𝚁 𝙽𝙰𝙼𝙴 ➻ @{msg.forward_from["username"]} \n\n💛 𝙸𝙳 ➻ <code>{msg.forward_from["id"]}</code>'
        else:
            text += f'\n\n💛 𝙸𝙳 ➻ `{msg.forward_from["id"]}`'
        await msg.reply(text, quote=True)
    else:
        hidden = msg.forward_sender_name
        if hidden:
            await msg.reply(
                f"❌️ 𝙴𝚁𝚁𝙾𝚁 <b><i>{hidden}</i></b> ❌️ 𝙴𝚁𝚁𝙾𝚁",
                quote=True,
            )
        else:
            text = f"<u>𝙵𝙾𝚁𝚆𝙰𝚁𝙳 𝙸𝙽𝙵𝙾𝚁𝙼𝙰𝚃𝙸𝙾𝙽 💚🐸</u>.\n\n"
            if msg.forward_from_chat["type"] == "channel":
                text += "<u>❤️🍓 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 </u>"
            if msg.forward_from_chat["type"] == "supergroup":
                text += "<u>🗣️ 𝙶𝚁𝙾𝚄𝙿</u>"
            text += f'\n\n📃 𝙽𝙰𝙼𝙴 ➻ {msg.forward_from_chat["title"]}'
            if msg.forward_from_chat["username"]:
                text += f'\n\n💚 𝙵𝚁𝙾𝙼 ➻ @{msg.forward_from_chat["username"]}'
                text += f'\n\n🆔 𝙸𝙳 ➻ `{msg.forward_from_chat["id"]}`'
            else:
                text += f'\n\n🆔 𝙸𝙳 ➻ `{msg.forward_from_chat["id"]}`\n\n'
            await msg.reply(text, quote=True)
