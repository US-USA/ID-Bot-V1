from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

START_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("🪧 𝐋𝐧𝐯𝐢𝐭𝐞 𝐓𝐡𝐞 𝐁𝐨𝐭 𝐓𝐨 𝐓𝐡𝐞 𝐆𝐫𝐨𝐮𝐩",  url=f"https://telegram.me/BOTidSBot?startgroup=start"),
       InlineKeyboardButton("💙 𝐁𝐘",  url=f"tg://openmessage?user_id=1257421053"),
       InlineKeyboardButton("🇺🇲 𝐁𝐘 ", url=f"tg://openmessage?user_id=2146813672")
       ],[
       InlineKeyboardButton("⬇️ 𝐌𝐨𝐫𝐞 𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧 ⬇️", callback_data="help")
       ]]
       )

HELP_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐈𝐝", callback_data="id"),
       InlineKeyboardButton("𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐈𝐧𝐟𝐨", callback_data="info")
       ],[
       InlineKeyboardButton("🏠 𝐇𝐨𝐦𝐞", callback_data="start"),
       InlineKeyboardButton("⬇️ 𝐂𝐥𝐨𝐬𝐞", callback_data="close"),
       InlineKeyboardButton("🤠 𝐀𝐛𝐨𝐮𝐭", callback_data="about")
       ]]
       )

ABOUT_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("🔙 𝐁𝐚𝐜𝐤", callback_data="help"),
       InlineKeyboardButton("🏠 𝐇𝐨𝐦𝐞", callback_data="start"),
       InlineKeyboardButton("⬇️ 𝐂𝐥𝐨𝐬𝐞", callback_data="close")
       ]]
       )
