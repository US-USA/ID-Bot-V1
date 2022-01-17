class Translation(object):

    START_MSG = """
👋𝐇𝐞𝐲 {},

𝐈𝐚𝐦 𝐚 𝐒𝐢𝐦𝐩𝐥𝐞 𝐁𝐨𝐭 𝐅𝐨𝐫 𝐅𝐢𝐧𝐝𝐢𝐧𝐠 𝐈𝐃𝐬 𝐢𝐧 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦.. 🔍 🆔

𝐂𝐥𝐢𝐜𝐤 𝐭𝐡𝐞 𝐇𝐞𝐥𝐩 𝐁𝐮𝐭𝐭𝐨𝐧 𝐨𝐫 /help 𝐅𝐨𝐫 𝐌𝐨𝐫𝐞 𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧
"""

    HELP_MSG = """
<u>× 𝐓𝐡𝐞 𝐅𝐨𝐥𝐥𝐨𝐰𝐢𝐧𝐠 𝐈𝐬 𝐓𝐡𝐞 𝐈𝐃 𝐑𝐞𝐯𝐞𝐚𝐥𝐢𝐧𝐠 𝐌𝐞𝐭𝐡𝐨𝐝</u>

  ✮ 𝐂𝐥𝐢𝐜𝐤 𝐓𝐡𝐞 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐈𝐝 𝐁𝐮𝐭𝐭𝐨𝐧 𝐎𝐫 /id 𝐁𝐞𝐥𝐨𝐰 𝐓𝐨 𝐏𝐢𝐜𝐤 𝐘𝐨𝐮𝐫 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐈𝐝

  ✮ 𝐂𝐥𝐢𝐜𝐤 𝐓𝐡𝐞 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐈𝐧𝐟𝐨 𝐁𝐮𝐭𝐭𝐨𝐦 𝐎𝐫 /info 𝐁𝐞𝐥𝐨𝐰 𝐓𝐨 𝐏𝐢𝐜𝐤 𝐔𝐩 𝐘𝐨𝐮𝐫 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧

  ✮ 𝐈𝐟 𝐲𝐨𝐮 𝐬𝐞𝐧𝐝 𝐚 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 [𝐮𝐬𝐢𝐧𝐠 𝐭𝐡𝐞 𝐟𝐨𝐫𝐰𝐚𝐫𝐝 𝐭𝐚𝐠] 𝐟𝐫𝐨𝐦 𝐲𝐨𝐮𝐫 [𝐩𝐮𝐛𝐥𝐢𝐜 𝐨𝐫 𝐩𝐫𝐢𝐯𝐚𝐭𝐞] 𝐠𝐫𝐨𝐮𝐩 𝐲𝐨𝐮 𝐰𝐢𝐥𝐥 𝐫𝐞𝐜𝐞𝐢𝐯𝐞 𝐭𝐡𝐞 𝐈𝐃 𝐨𝐟 𝐭𝐡𝐚𝐭 𝐆𝐫𝐨𝐮𝐩

  ✮ 𝐈𝐟 𝐲𝐨𝐮 𝐬𝐞𝐧𝐝 𝐚 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 [𝐮𝐬𝐢𝐧𝐠 𝐭𝐡𝐞 𝐟𝐨𝐫𝐰𝐚𝐫𝐝 𝐭𝐚𝐠] 𝐟𝐫𝐨𝐦 𝐲𝐨𝐮𝐫 [𝐩𝐮𝐛𝐥𝐢𝐜 𝐨𝐫 𝐩𝐫𝐢𝐯𝐚𝐭𝐞] 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐲𝐨𝐮 𝐰𝐢𝐥𝐥 𝐫𝐞𝐜𝐞𝐢𝐯𝐞 𝐭𝐡𝐞 𝐈𝐃 𝐨𝐟 𝐭𝐡𝐚𝐭 𝐂𝐡𝐚𝐧𝐧𝐞𝐥

  ✮ 𝐈𝐟 𝐘𝐨𝐮 𝐍𝐞𝐞𝐝 𝐓𝐡𝐞 𝐈𝐝 𝐎𝐟 𝐀𝐧𝐲 𝐁𝐨𝐭, 𝐒𝐞𝐧𝐝 𝐁𝐨𝐭 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐇𝐞𝐫𝐞 𝐅𝐫𝐨𝐦 𝐓𝐡𝐚𝐭 𝐁𝐨𝐭 [𝐖𝐢𝐭𝐡 𝐅𝐨𝐫𝐰𝐚𝐫𝐝 𝐓𝐚𝐠]

  ✮ 𝐈𝐟 𝐘𝐨𝐮 𝐍𝐞𝐞𝐝 𝐚 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐔𝐬𝐞𝐫 𝐈𝐝, 𝐅𝐨𝐫𝐰𝐚𝐫𝐝 𝐀 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐓𝐨 𝐓𝐡𝐞𝐦 𝐇𝐞𝐫𝐞 [𝐰𝐢𝐭𝐡 𝐅𝐨𝐫𝐰𝐚𝐫𝐝 𝐓𝐚𝐠]

  ✮ 𝐈𝐟 𝐲𝐨𝐮 𝐠𝐢𝐯𝐞 𝐲𝐨𝐮𝐫 𝐫𝐞𝐩𝐥𝐲 /Json 𝐚𝐧𝐲 [𝐦𝐞𝐬𝐬𝐚𝐠𝐞, 𝐟𝐢𝐥𝐞𝐬, 𝐦𝐞𝐝𝐢𝐚, 𝐬𝐭𝐢𝐜𝐤𝐞𝐫𝐬] 𝐲𝐨𝐮 𝐰𝐢𝐥𝐥 𝐠𝐞𝐭 𝐭𝐡𝐞 𝐉𝐬𝐨𝐧 𝐟𝐢𝐥𝐞𝐬 𝐨𝐟 𝐭𝐡𝐨𝐬𝐞 𝐟𝐢𝐥𝐞𝐬
  
  ✮ 𝐈𝐟 𝐲𝐨𝐮 𝐧𝐞𝐞𝐝 𝐭𝐨 𝐠𝐞𝐭 𝐚𝐧 𝐈'𝐝 𝐨𝐟 𝐚 𝐬𝐭𝐢𝐜𝐤𝐞𝐫 𝐩𝐚𝐜𝐤 𝐣𝐮𝐬𝐭 𝐬𝐞𝐧𝐝 𝐭𝐡𝐞 𝐬𝐭𝐢𝐜𝐤𝐞𝐫 𝐚𝐧𝐝 𝐫𝐞𝐩𝐥𝐲 𝐢𝐭 𝐰𝐢𝐭𝐡 /stickerid 𝐜𝐨𝐦𝐦𝐚𝐧𝐝 𝐲𝐨𝐮 𝐰𝐨𝐮𝐥𝐝 𝐠𝐞𝐭 𝐢𝐭𝐬 𝐈𝐝.
"""

    ABOUT_MSG = """
<u>🤖 𝐌𝐲 𝐍𝐚𝐦𝐞</u> : <a href='https://t.me/{}'>𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧 𝐁𝐨𝐭</a> 
  
<u>📝 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞</u> : <a href='https://www.python.org/'>𝐏𝐲𝐭𝐡𝐨𝐧3</a>

<u>🧰 𝐅𝐫𝐚𝐦𝐞𝐖𝐨𝐫𝐤</u> : <a href='https://github.com/pyrogram/pyrogram'>𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦</a>

<u>👨‍💻 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫</u> : <a href='t.me/{}'>𝐮𝐬𝟕𝐚𝟓</a>

<u>👨‍💻 𝐂𝐨 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫</u> : <a href='https://t.me/{}' >𝐮𝐬𝐚</a>

<u>👥 𝐆𝐫𝐨𝐮𝐩</u> :   <a href='t.me/{}'>𝐀𝐦𝐞𝐫𝐢𝐜𝐚</a>
 
<u>📢 𝐂𝐡𝐚𝐧𝐧𝐞𝐥</u> : <a href='t.me/{}'>𝐍𝐞𝐰 𝐘𝐨𝐫𝐤</a>

<u>❣️ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞</u> : <a href='https://youtube.com/channel/UCe-gwa48GwgTIE7T5fmpbJw'>𝐘𝐨𝐮𝐓𝐮𝐛𝐞</a>

<u>🔘 𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐨𝐝𝐞</u> : <a href='{}'>𝐏𝐫𝐞𝐬𝐬 𝐌𝐞 🔮</a>
"""

    JOIN_TEXT = """
📢 𝐉𝐨𝐢𝐧 𝐌𝐲 𝐔𝐩𝐝𝐚𝐭𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 📢
"""
 
    TRY_TEXT = """
🔃 𝐑𝐞𝐒𝐭𝐚𝐫𝐭 𝐍𝐨𝐰 🔃
"""

    FSUB_TEXT = """
📢 𝐉𝐨𝐢𝐧 𝐌𝐲 𝐔𝐩𝐝𝐚𝐭𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐓𝐡𝐞𝐧 𝐔𝐬𝐞 𝐓𝐡𝐢𝐬 𝐁𝐨𝐭 📢
"""

    ID_TEXT = """
🆔 𝐘𝐨𝐮𝐫 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐈𝐃 𝐢𝐬 :- <code>{}</code>
"""

    INFO_TEXT = """
<u>💫 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧</u>

 🙋🏻‍♂️ 𝐅𝐢𝐫𝐬𝐭 𝐍𝐚𝐦𝐞 : <b>{}</b>

 🧖‍♂️ 𝐒𝐞𝐜𝐨𝐧𝐝 𝐍𝐚𝐦𝐞 : <b>{}</b>

 🧑🏻‍🎓 𝐔𝐬𝐞𝐫𝐍𝐚𝐦𝐞 : <b>@{}</b>

 🆔 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐈𝐃 : <code>{}</code>

 🌌 𝐏𝐫𝐨𝐟𝐢𝐥𝐞 𝐋𝐢𝐧𝐤 : <b>{}</b>

 🌍 𝐃𝐂 : <b>{}</b>

 🎤 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞 : <b>{}</b>

 🤠 𝐒𝐭𝐚𝐭𝐮𝐬 : <b>{}</b>
"""
