#15-11-2021
#okbei

from details import API_ID, API_HASH, BOT_TOKEN, ADMIN, START_IMG, START_MSG, BUTTON_1, BUTTON_2, LINK_1, LINK_2, SESSION_NAME               
from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InlineQuery, User, Message, InlineQueryResultArticle, \
    InputTextMessageContent

Bot = Client(
     session_name=SESSION_NAME,
     api_id=API_ID,
     api_hash=API_HASH,
     bot_token=BOT_TOKEN
)



@Bot.on_message(filters.command(['start']) & filters.private)
async def start(bot, message):
    buttons = [[
                 InlineKeyboardButton(f'{BUTTON_1}', url=f"{LINK_1}"),
                 InlineKeyboardButton(f'{BUTTON_2}', url=f"{LINK_2}")
              ]]

    await message.reply_photo(photo=START_IMG,
                              caption=START_MSG.format(
                                      first = message.from_user.first_name,
                                      last = message.from_user.last_name,
                                      mention = message.from_user.mention,
                                      id = message.from_user.id),
                               reply_markup = InlineKeyboardMarkup(buttons)
                              )

            

@Bot.on_message(filters.command('submit') & filters.private)
async def report(bot, message):
        if message.reply_to_message:
                                  await bot.send_message(chat_id=ADMIN, text=f"<b>⭕️NEW MESSAGE⭕️\n \n🧿 Name: {message.from_user.mention}\n🧿 User ID:</b> <code>{message.chat.id}</code>")
                                  await bot.forward_messages(chat_id=ADMIN, from_chat_id=message.from_user.id, message_ids=message.reply_to_message.message_id)
                                  await message.reply_text("<b>✅ Your Feedback Successfully Submitted to the Admins</b>")
        else:
             await message.reply_text("<b>Use this command as the reply of any Message to Report</b>")

                         
        
@Bot.on_message(filters.command('reply') & filters.private)
async def replyt(bot, message):
    if message.from_user.id == ADMIN: 
               if message.reply_to_message:
                                    userid=int(message.text.replace("/reply"," "))
                                    await bot.send_message(chat_id=userid, text=f"<b>An Admin is responded to your feedback ✨</b>")
                                    await bot.copy_message(chat_id=userid, from_chat_id=ADMIN, message_id=message.reply_to_message.message_id)
                                    await message.reply_text("<b>✅ Your Reply Successfully Send to the User</b>")
               else:
                    await message.reply_text("<b>Use this command as the reply of any Message to Reply</b>")                         
    else:
         await message.reply_text("<b>That's not for you bruh 😅</b>")


                          
@Bot.on_message(filters.command('send') & filters.private)
async def send(bot, message):
    if message.from_user.id == ADMIN: 
               if message.reply_to_message:
                                    chatid=int(message.text.replace("/send"," "))
                                    await bot.copy_message(chat_id=chatid, from_chat_id=ADMIN, message_id=message.reply_to_message.message_id)
                                    await message.reply_text("<b>✅ Message Successfully Send to the Group</b>")
               else:
                    await message.reply_text("<b>Use this command as the reply of any Message to Send in Group</b>")                         
    else:
         await message.reply_text("<b>That's not for you bruh 😅</b>")


                                    
@Bot.on_message(filters.command('pin') & filters.private)
async def pin(bot, message):
    if message.from_user.id == ADMIN: 
               if message.reply_to_message:
                                    chatid=int(message.text.replace("/pin"," "))
                                    p=await bot.copy_message(chat_id=chatid, from_chat_id=ADMIN, message_id=message.reply_to_message.message_id)
                                    await p.pin()
                                    await message.reply_text("<b>✅ Message Successfully Send to the Group And pinned</b>")
               else:
                    await message.reply_text("<b>Use this command as the reply of any Message to Send in Group</b>")                         
    else:
         await message.reply_text("<b>That's not for you bruh 😅</b>")
                                    
@Bot.on_inline_query()
async def inline_handlers(_, event: InlineQuery):
    answers = list()
    # If Search Query is Empty
    if event.query == "":
        answers.append(
            InlineQueryResultArticle(
                title="Tutorial Video",
                description="If you are facing any problem In opening Tnlink, Watch this Tutorial...",
                thumb_url="https://i.imgur.com/6jZsMYG.png",
                input_message_content=InputTextMessageContent(
                    message_text="Please watch this video if you are facing problem in opening links.",
                    disable_web_page_preview=True
                ),
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("Watch Tutorial", url="https://jmp.sh/q24v5ga")]
                ])
            )
        )
        answers.append(
            InlineQueryResultArticle(
                title="Support Channel & Group",
                description="Channel - @pocketfmhub\nGroup - @pocketfmhubchat",
                thumb_url="https://i.ibb.co/cNYJHYZ/IMG-20210815-144921.jpg",
                input_message_content=InputTextMessageContent(
                    message_text="Using this bot you can search all the available audiobooks of pocket Fm Hub without visiting main channel",
                    disable_web_page_preview=True
                ),
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("Support Group", url="https://t.me/pocketfmhubchat"),
                     InlineKeyboardButton("Bots Channel", url="https://t.me/pocketfmhub")],
                    [InlineKeyboardButton("Search Here", switch_inline_query_current_chat="")]
                ])
            )
        )
        try:
            await event.answer(
            results=answers,
            cache_time=0
            )
            print(f"[{Config.BOT_SESSION_NAME}] - Answered Successfully - {event.from_user.first_name}")
        except QueryIdInvalid:
            print(f"[{Config.BOT_SESSION_NAME}] - Failed to Answer - {event.from_user.first_name}")
    # Search Channel Message using Search Query Words
    else:
        txt="All results\n\n"
        async for message in User.search_messages(chat_id=Config.CHANNEL_ID, limit=49, query=event.query):
            if message.text:
                answers.append(InlineQueryResultArticle(
                    title="{}".format(message.text.split("\n", 1)[0]),
                    description="{}".format(message.text.rsplit("\n", 1)[-1]),
                    thumb_url="https://i.ibb.co/BwYhZTr/IMG-20210914-015740-238.jpg",
                    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Search Again", switch_inline_query_current_chat="")]]),
                    input_message_content=InputTextMessageContent(
                        message_text=message.text.markdown,
parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                ))
                txt=txt+"{} - https://t.me/pocketfmhub/{}".format(message.text.split("\n", 1)[0],message.message_id)+"\n\n"
        answers.append(InlineQueryResultArticle(
                    title="All Episodes",
                    description="All Episodes",
                    thumb_url="https://i.ibb.co/4dPd52s/Png-Item-5099442-1.png",
                    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Search Again", switch_inline_query_current_chat="")]]),
                    input_message_content=InputTextMessageContent(
                        message_text=txt,
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                ))
        try:
            await event.answer(
            results=answers,
            cache_time=0
            )
            print(f"[{Config.BOT_SESSION_NAME}] - Answered Successfully - {event.from_user.first_name}")
        except QueryIdInvalid:
            print(f"[{Config.BOT_SESSION_NAME}] - Failed to Answer - {event.from_user.first_name}")

@Bot.on_message(filters.command('id') & filters.group)
async def id(bot, message):
    await message.reply_text(f"<b>➲ Chat ID:</b> <code>{message.chat.id}</code>")
    
# Start Clients
Bot.start()
User.start()
# Loop Clients till Disconnects
idle()
# After Disconnects,
# Stop Clients
Bot.stop()
User.stop()
