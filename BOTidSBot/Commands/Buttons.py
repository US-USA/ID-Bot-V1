from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

START_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("💛 𝙱𝚈",  url=f"tg://openmessage?user_id=1257421053"),
       InlineKeyboardButton("🇺🇲 𝙱𝚈", url=f"tg://openmessage?user_id=2146813672")
       ],[
       InlineKeyboardButton("⬇️ 𝙼𝙾𝚁𝙴 𝙸𝙽𝙵𝙾𝚁𝙼𝙰𝚃𝙸𝙾𝙽 ⬇️", callback_data="help")
       ],[
       InlineKeyboardButton("★ 𝙻𝙽𝚅𝙸𝚃𝙴 𝚃𝙷𝙴 𝙱𝙾𝚃 𝚃𝙾 𝚃𝙷𝙴 𝙶𝚁𝙾𝚄𝙿 ★",  url=f"https://telegram.me/BOTidSBot?startgroup=start")
       ]]
       )

HELP_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐈𝐝", callback_data="id"),
       InlineKeyboardButton("𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐈𝐧𝐟𝐨", callback_data="info")
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
