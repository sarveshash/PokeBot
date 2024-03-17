from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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
        await callback_query.edit_message_text("hi")


# Define a list of admin user IDs (replace these with actual user IDs)
admin_ids = [123456789, 987654321]

# Define a custom filter to check if the user is an admin
def is_admin(_, __, update):
    return update.from_user.id in admin_ids

# Define a command handler to promote a user to admin
@app.on_message(filters.command("promote") & is_admin)
async def promote_command_handler(client, message):
    # Check if a username was mentioned in the command
    if len(message.command) != 2:
        await message.reply_text("Please mention the username of the user you want to promote.")
        return

    # Get the username mentioned in the command
    username = message.command[1]

    # Get the user ID from the username
    try:
        user = await app.get_users(username)
        user_id = user.id
    except Exception as e:
        await message.reply_text(f"Error: {e}")
        return

    # Add the user ID to the list of admin IDs
    admin_ids.append(user_id)

    # Respond to the user indicating successful promotion
    await message.reply_text(f"User {username} has been promoted to admin.")

# Run the Pyrogram client



app.run()
