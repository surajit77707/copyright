import os
import re
import sys
import time
import datetime
import random
import asyncio
import platform
import logging
from pytz import timezone
from pyrogram import filters, Client, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.enums import ChatMemberStatus, ChatType
from pyrogram.raw.types import UpdateEditMessage, UpdateEditChannelMessage
import traceback
from pyrogram import Client, filters

from apscheduler.schedulers.background import BackgroundScheduler

API_ID = 23967991
API_HASH = "a2c3ccfaff4c2dbbff7d54981828d4f1"
BOT_TOKEN = "8151352194:AAFZFL1TO2Iuht3W4hoSTl2T3Xk3Y4jCHdA"
DEVS = [1883889098, 7638575366]
BOT_USERNAME = "banxeditbot" # change your bot username without 
OWNER_ID = 7638575366

ALL_GROUPS = []
TOTAL_USERS = []
MEDIA_GROUPS = []
DISABLE_CHATS = []
GROUP_MEDIAS = {}
APPROVED_USERS = []


DELETE_KEYWORDS = ["baap", "beta", "Batichod", "hydrogen", "energy", "Gand", "papa", "porn", "xxx", "sex", "Bahenchod", "XII", "page", "Madarchod", "meiotic", "divisions", "System.in", "Scanner", "void", "nextInt","🅐‌»", 
"🄰🄻🄻🄴🄽 ",
"🅲🅻🅰🆂🆂🆁🅾🅾🅼",
"🅲🅾🅽🆃🅰🅲🆃",
"🅿🆁🅾🅶🆁🅰🅼🅼🅴",
"🅒🅐🅡🅔🅔🅡 ",
"🅘🅝🅢🅣🅘🅣🅤🅣🅔",
"🅑🅐🅣🅗  🅢🅔🅔🅢 🅐 🅞🅢🅔 🅣🅢🅣",
"🅐🅒🅐🅓🅔🅜🅘🅒 ",
"🅢🅔🅢🅢🅘🅞🅝",
"🅐🅛🅛🅔🅝 ",
"🅒🅛🅐🅢🅢🅡🅞🅞🅜 🅒🅞🅝🅣🅐🅒🅣",
"🅿🆁🅾🅶🆁🅰🅼🅼🅴",
"🅲🅰🆁🅴🅴🆁 ",
"🅸🅽🆂🆃🅸🆃🆄🆃🅴",
"🅑🅐🅣🅗 ",
"🅢🅔🅔🅢 🅐 🅞🅢🅔 🅣🅢🅣", 
"🅐🅒🅐🅓🅔🅜🅘🅒",
"🅢🅔🅢🅢🅘🅞🅝",
"➋⓿➋➌",
"➋⓿➋➍",
"🅔🅝🅣🅗🅤🅢🅘🅐🅢🅣",
"🅛🅔🅐🅓🅔🅡  ",
"🅐🅒🅗🅘🅔🅥🅔🅡 ",
"🅒🅞🅤🅡🅢🅔",
"🅟🅗🅐🅢🅔 ",
"🅢🅡🅛-➋",
"🅣🅐🅡🅖🅔🅣",
"🅟🅡🅔",
"🅜🅔🅓🅘🅒🅐🅛",
"➋⓿➋➊",
"🅃🄴🅂🅃 ",
"🅃🅈🄿🄴",
"🄼🄸🄽🄾🅁 🅃🄴🅂🅃 ",
"🄿🄰🅃🅃🄴🅁🄽 ",
"🄽🄴🄴🅃 ",
"🅄🄶",
"Module ",
"module",
"Porn ",
"porn",
"Sex ",
"sex",
"Allen", 
"allen",
"Physicswala",
"physicswala",

"Rigid",

"rigid",

"𝕮𝕬𝖑𝖑𝖊𝖓",
"𝕻𝖆𝖌𝖊", 
"=Â»",
"𝕷𝕬𝕾𝕾𝕽𝕺𝕺𝕸 𝕮𝕺𝕹𝕿𝕬𝕮𝕿 𝕻𝕽𝕺𝕲𝕽𝕬𝕸𝕸𝕰",
"𝕮𝕬𝕽𝕰𝕰𝕽 𝕴𝕹𝕾𝕿𝕴𝕿𝖀𝕿𝕰",
"𝕬𝖈𝖆𝖉𝖊𝖒𝖎𝖈 𝕾𝖊𝖘𝖘𝖎𝖔𝖓 ",
"𝕰𝖓𝖙𝖍𝖚𝖘𝖎𝖆𝖘𝖙",
"𝕷𝖊𝖆𝖉𝖊𝖗 ",
 "𝕬𝖈𝖍𝖎𝖊𝖛𝖊𝖗",
 "𝕮𝖔𝖚𝖗𝖘𝖊",
"𝕻𝕳𝕬𝕾𝕰",
 "𝕾𝕽𝕷",
"𝕿𝕬𝕽𝕲𝕰𝕿", 
"𝕻𝕽𝕰-𝕸𝕰𝕯𝕴𝕮𝕬𝕷", 
"𝕿𝖊𝖘𝖙 𝕿𝖞𝖕𝖊 ",
"𝕸𝕴𝕹𝕺𝕽 𝕿𝖊𝖘𝖙 𝕻𝖆𝖙𝖙𝖊𝖗𝖓", 
"𝕹𝕰𝕰𝕿 (𝖀𝕲)",
"𝕿𝕰𝕾𝕿 𝕯𝕬𝕿𝕰 ",
">",
"<",
"=",
"𝕾𝕰𝕮𝕿𝕴𝕺𝕹-𝕬", 
"𝕹𝖔",
"𝖒𝖊𝖎𝖔𝖙𝖎𝖈 ",
"𝖉𝖎𝖛𝖎𝖘𝖎𝖔𝖓𝖘 ",
"𝖗𝖊𝖖𝖚𝖎𝖗𝖊𝖉", 
"𝖘𝖊𝖊𝖉𝖘 ",
"𝖆𝖓𝖌𝖎𝖔𝖘𝖕𝖊𝖗𝖒", 
"𝖓𝖚𝖒𝖇𝖊𝖗",
 "𝕬𝖓𝖘",
 "𝖕𝖆𝖌𝖊 ",
 "𝕹𝕮𝕰𝕽𝕿 𝖃𝕴𝕴",

"Keywords",

"negligible",
"particle",
"collision",
"initial",
"velocity",
"coefficient",
"restitution",
"velocities",
"collide", 
"dimension", 
"velocities",
"collision",         
"m/s",

"Acceleration",
"Quantity",
"Measured",

"Negligible",
"Particle",
"Collision",
"Initial",
"Velocity",
"Coefficient",
"Restitution",
"Velocities",
"Collide",
"Dimension",  
"Velocities",
"Collision",         
"m/s",

"acceleration",
"quantity",
"measured",

"Experiment",

"experiment",

"Vibrational",",
"Monoatomic",
"Frictionless",
"Adiabatically",
"Piston",
"PHYSICS ",
"CHEMISTRY ",
"BIOLOGY",
"Trachea",
"Stapedius",
"Sartorius",
"Epimysium",
"Vrms",
"Nitrogen", 
"Hydride",

"vibrational",
"monoatomic",
"frictionless",
"adiabatically",
"piston",
"physics",
"chemistry", 
"biology ",
"trachea",
"stapedius",
"sartorius",
"epimysium",
"vrms",
"nitrogen", 
"hydride"]

START_MESSAGE = """<b>𝑯𝑬𝒀 𝑮𝑼𝒀 🦍</b>

</b>「 ⌜ Ꮆ卄ㄖ丂ㄒ 乂 乇ᗪ丨ㄒ ⌟ 」 </b>


ɪ ᴄᴀɴ ꜱᴀᴠᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘꜱ ꜰʀᴏᴍ ᴄᴏᴘʏʀɪɢʜᴛꜱ 😉   
**ᴘʀᴏᴄᴇꜱꜱ?:** ꜱɪᴍᴘʟʏ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇ ᴀꜱ ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴅᴇʟᴇᴛᴇ ᴍᴇꜱꜱᴀɢᴇꜱ ʀ
"""

app = Client('bot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(_, msg):
    buttons = [
        [
            InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
            InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="dil_back")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(buttons)

    await msg.reply_photo(
        photo="https://envs.sh/bu4.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )

gd_buttons = [
    [
        InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/UmbrellaUCorp"),
        InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url="https://t.me/moviiieeeesss"),
    ]
]

@app.on_callback_query(filters.regex("dil_back"))
async def dil_back(_, query: CallbackQuery):
    await query.message.edit_caption(START_MESSAGE,
                                    reply_markup=InlineKeyboardMarkup(gd_buttons),)

start_time = time.time()

bot = Client('bot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

def add_user(user_id):
    if user_id not in TOTAL_USERS:
        TOTAL_USERS.append(user_id)

def time_formatter(milliseconds):
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)

    time_format = (
        (f"{days}d, " if days else "") +
        (f"{hours}h, " if hours else "") +
        (f"{minutes}m, " if minutes else "") +
        (f"{seconds}s, " if seconds else "") +
        (f"{milliseconds}ms" if milliseconds else "")
    )
    return time_format

@bot.on_message(filters.command(["ping", "speed"]))
async def ping(_, e: Message):
    start = datetime.datetime.now()
    add_user(e.from_user.id)
    rep = await e.reply_text("**Pong !!**")
    end = datetime.datetime.now()
    ms = (end-start).microseconds / 1000
    python_version = platform.python_version()
    start_time = time.time()  # Define start_time here
    uptime = time_formatter((time.time() - start_time) * 1000)
    await rep.edit_text(f"🤖 ᑭOᑎᘜ: `{ms}`ᴍs\n"
                        f"➪ᗷᗩᑎᑎᗴᖇ ᐯᗴᖇՏIOᑎ: {python_version}\n"
                        f"➪Oᗯᑎᗴᖇ: @bannerx69\n"
                        f"➪ՏᑌᑭᑭOᖇT: @UmbrellaUCorp \n"
                        )

# Broadcasting Function with DM and Group Messages
@bot.on_message(filters.command("broadcast") & filters.user(DEVS))
async def broadcast(_, msg: Message):
    if len(msg.command) < 2:
        await msg.reply_text("Please provide a message to broadcast.")
        return

    broadcast_message = " ".join(msg.command[1:])
    
    total_sent_dm = 0
    failed_sent_dm = 0
    total_sent_group = 0
    failed_sent_group = 0

    # Sending to all users' DMs
    for user_id in TOTAL_USERS:
        try:
            await bot.send_message(user_id, broadcast_message)
            total_sent_dm += 1
        except Exception as e:
            failed_sent_dm += 1
            print(f"Failed to send message to user {user_id}: {e}")

    # Sending to all groups
    for group_id in ALL_GROUPS:
        try:
            await bot.send_message(group_id, broadcast_message)
            total_sent_group += 1
        except Exception as e:
            failed_sent_group += 1
            print(f"Failed to send message to group {group_id}: {e}")

    # Reporting the result
    await msg.reply_text(
        f"Broadcast complete!\n"
        f"Sent to {total_sent_dm} users' DMs, Failed to send to {failed_sent_dm} users.\n"
        f"Sent to {total_sent_group} groups, Failed to send to {failed_sent_group} groups."
    )

@bot.on_message(filters.command("stats") & filters.user(DEVS))
async def stats(_, msg: Message):
    total_users_count = len(TOTAL_USERS)  # Number of users the bot is tracking
    total_groups_count = len(ALL_GROUPS)  # Number of groups the bot is tracking
    total_deleted_messages = sum(len(msg_list) for msg_list in GROUP_MEDIAS.values())  # Number of messages deleted
    total_dm_sent = len([user for user in TOTAL_USERS if user in sent_dm])  # Count of DM sent (if you track this)
    
    # Format the stats message
    stats_message = (
        f"**Bot Stats**\n\n"
        f"Total Users: {total_users_count}\n"
        f"Total Groups: {total_groups_count}\n"
        f"Messages Deleted: {total_deleted_messages}\n"
        f"Total DMs Sent: {total_dm_sent}\n"
        f"Bot Uptime: {time_formatter((time.time() - start_time) * 1000)}"
    )

    # Send the stats message to the developer
    await msg.reply_text(stats_message)




@bot.on_message(filters.command(["help", "start"]))
async def start_message(_, message: Message):
    add_user(message.from_user.id)
    BUTTON = [[InlineKeyboardButton("Support Group", url="https://t.me/UmbrellaUCorp")]]
    await message.reply(START_MESSAGE.format(message.from_user.mention), reply_markup=InlineKeyboardMarkup(BUTTON))

@bot.on_message(filters.user(DEVS) & filters.command(["restart", "reboot"]))
async def restart_(_, e: Message):
    await e.reply("**Restarting.....**")
    try:
        await bot.stop()
    except Exception:
        pass
    args = [sys.executable, "copyright.py"]
    os.execl(sys.executable, *args)
    quit()



FORBIDDEN_KEYWORDS = ["baap", "beta", "Batichod", "hydrogen", "energy", "Gand", "papa", "porn", "xxx", "sex", "Bahenchod", "XII", "page", "Madarchod", "meiotic", "divisions", "System.in", "Scanner", "void", "nextInt"]

@bot.on_message()
async def handle_message(client, message):
    if any(keyword in message.text for keyword in FORBIDDEN_KEYWORDS):
        logging.info(f"Deleting message with ID {message.id}")
        await message.delete()
      #  user_mention = from_user.mention
        await message.reply_text(f"@{message.from_user.username} 𝖣𝗈𝗇'𝗍 𝗌𝖾𝗇𝖽 𝗇𝖾𝗑𝗍 𝗍𝗂𝗆𝖾!")
    elif any(keyword in message.caption for keyword in FORBIDDEN_KEYWORDS):
        logging.info(f"Deleting message with ID {message.id}")
        await message.delete()
       # user_mention = from_user.mention
        await message.reply_text(f"@{message.from_user.username} 𝖣𝗈𝗇'𝗍 𝗌𝖾𝗇𝖽 𝗇𝖾𝗑𝗍 𝗍𝗂𝗆𝖾!")




@bot.on_message(filters.document)
async def delete_pdf_files(_, message: Message):
    if message.document.mime_type == "application/pdf":
        await message.delete()
        buttons = [
            [InlineKeyboardButton("Support Group", url="https://t.me/UmbrellaUCorp")]
        ]
        await message.reply(
            "PDF files are not allowed and have been deleted.",
            reply_markup=InlineKeyboardMarkup(buttons)
        )

@bot.on_message(filters.all & filters.group)
async def watcher(_, message: Message):
    chat = message.chat
    user_id = message.from_user.id
    if chat.type == ChatType.GROUP or chat.type == ChatType.SUPERGROUP:
        if chat.id not in ALL_GROUPS:
            ALL_GROUPS.append(chat.id)
        if chat.id not in MEDIA_GROUPS:
            MEDIA_GROUPS.append(chat.id)
        if (message.video or message.photo or message.animation or message.document):
            check = GROUP_MEDIAS.get(chat.id)
            if check:
                GROUP_MEDIAS[chat.id].append(message.id)
                print(f"Chat: {chat.title}, message ID: {message.id}")
            else:
                GROUP_MEDIAS[chat.id] = [message.id]
                print(f"Chat: {chat.title}, message ID: {message.id}")



@bot.on_message(filters.text & filters.group)
async def delete_keyword_messages(_, message: Message):
    try:
        # Check if the message contains more than 200 words
        if len(message.text.split()) > 100:
            await message.delete()
            await message.reply(
                "Your message was too long and has been deleted.",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Support Group", url="https://t.me/UmbrellaUCorp")]])
            )
            print(f"Deleted message from {message.from_user.id} for exceeding word limit.")
            return
        
        # Check for prohibited keywords
        if any(re.search(rf'\b{re.escape(keyword)}\b', message.text.lower()) for keyword in DELETE_KEYWORDS):
            await message.delete()
            await message.reply(
                "Your message contained prohibited keywords and has been deleted.",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Support Group", url="https://t.me/UmbrellaUCorp")]])
            )
            print(f"Deleted message from {message.from_user.id} containing blacklisted keywords.")
    except Exception as e:
        print(f"Error deleting message: {e}")

@bot.on_raw_update(group=-1)
async def better(client, update, _, __):
    if isinstance(update, UpdateEditMessage) or isinstance(update, UpdateEditChannelMessage):
        e = update.message
        try:
            if not getattr(e, 'edit_hide', False):
                user_id = e.from_id.user_id
                if user_id in DEVS:
                    return

                chat_id = f"-100{e.peer_id.channel_id}"
                
                await client.delete_messages(chat_id=chat_id, message_ids=e.id)
                
                user = await client.get_users(e.from_id.user_id)
                
                buttons = [
                    [InlineKeyboardButton("Support Group", url="https://t.me/UmbrellaUCorp")]
                ]
                
                await client.send_message(
                    chat_id=chat_id,
                    text=f"{user.mention} just edited a message, and I deleted it 🐸.",
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
        except Exception as ex:
            print("Error occurred:", traceback.format_exc())

def AutoDelete():
    if len(MEDIA_GROUPS) == 0:
        return

    for i in MEDIA_GROUPS:
        if i in DISABLE_CHATS:
            return
        message_list = list(GROUP_MEDIAS.get(i))
        try:
            hue = bot.send_message(i, random.choice(DELETE_KEYWORDS))
            bot.delete_messages(i, message_list, revoke=True)
            time.sleep(1)
            hue.delete()
            GROUP_MEDIAS[i].delete()
            gue = bot.send_message(i, text="Deleted All Media's")
        except Exception:
            pass
    MEDIA_GROUPS.remove(i)
    print("clean all medias ✓")
    print("waiting for 1 hour")

scheduler = BackgroundScheduler(timezone=timezone('Asia/Kolkata'))
scheduler.add_job(AutoDelete, "interval", seconds=180)
scheduler.start()

def starter():
    print('Starting Bot...')
    bot.start()
    print('Bot Started ✓')
    idle()

if __name__ == "__main__":
    starter()
