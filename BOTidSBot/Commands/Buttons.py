from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

START_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("💛 𝙱𝚈",  url=f"tg://openmessage?user_id=1257421053"),
       InlineKeyboardButton("🇺🇲 𝙱𝚈", url=f"tg://openmessage?user_id=2146813672")
       ],[
       InlineKeyboardButton("⬇️ 𝙼𝙾𝚁𝙴 𝙸𝙽𝙵𝙾𝚁𝙼𝙰𝚃𝙸𝙾𝙽 ⬇️", callback_data="help")
       ],[
       InlineKeyboardButton("★ 𝙽𝙴𝚆 𝚈𝙾𝚁𝙺 ★", url=f"https://t.me/us7a5")
       ]]
       )

HELP_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙸𝙳", callback_data="id"),
       InlineKeyboardButton("𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙸𝙽𝙵𝙾", callback_data="info")
       ],[
       InlineKeyboardButton("🏠 𝙷𝙾𝙼𝙴", callback_data="start"),
       InlineKeyboardButton("⬇️ 𝙲𝙻𝙾𝚂𝙴", callback_data="close"),
       InlineKeyboardButton("🐸 𝙰𝙱𝙾𝚄𝚃", callback_data="about")
       ]]
       )

ABOUT_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("🔙 𝙱𝙰𝙲𝙺", callback_data="help"),
       InlineKeyboardButton("🏠 𝙷𝙾𝙼𝙴", callback_data="start"),
       InlineKeyboardButton("⬇️ 𝙲𝙻𝙾𝚂𝙴", callback_data="close")
       ]]
       )
