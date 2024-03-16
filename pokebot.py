import asyncio
from pyrogram import Client,emoji, filters

api_id = 20058505
api_hash = "c6416428be72db3174999c1740524b88"
bot_token = "6563744619:AAG4v_ABfLA3lCSGbcNLWlS07ZA_qUmseqM"
TARGET = -1002034491551
MESSAGE = "{} Welcome to [Pyrogram](https://docs.pyrogram.org/)'s group chat {}!"


app = Client("Bot",api_id = api_id, api_hash = api_hash, bot_token = bot_token)

@app.on_message(filters.chat(TARGET) & filters.new_chat_members)
async def welcome(client, message):
    # Build the new members list (with mentions) by using their first_name
    new_members = [u.mention for u in message.new_chat_members]
    # Build the welcome message by using an emoji and the list we built above
    text = MESSAGE.format(emoji.SPARKLES, ", ".join(new_members))
    # Send the welcome message, without the web page preview
    await message.reply_text(text, disable_web_page_preview=True)

app.run()
