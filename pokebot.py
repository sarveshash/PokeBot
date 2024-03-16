import asyncio
from pyrogram import Client,emoji, filters

api_id = 20058505
api_hash = "c6416428be72db3174999c1740524b88"
bot_token = "6563744619:AAG4v_ABfLA3lCSGbcNLWlS07ZA_qUmseqM"
TARGET = -1002034491551
MESSAGE = "{} Welcome to [Pyrogram](https://docs.pyrogram.org/)'s group chat {}!"


app = Client("Bot",api_id = api_id, api_hash = api_hash, bot_token = bot_token)


# Define the handler for the /start command
@app.on_message(filters.command("start"))
async def start_command_handler(client, message):
    # Define the text message
    text = "Welcome to the Bot! Click the button below to do something."

    # Create an inline keyboard with a single button
    inline_keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Click Me!", callback_data="button_clicked")]
    ])

    # Send the message with the inline keyboard
    await message.reply_text(text, reply_markup=inline_keyboard)

# Define the handler for the inline button
@app.on_callback_query()
async def inline_button_handler(client, callback_query):
    if callback_query.data == "button_clicked":
        await callback_query.answer("Button Clicked!")

app.run()
