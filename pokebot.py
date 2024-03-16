
from pyrogram import Client

api_id = 20058505
api_hash = "c6416428be72db3174999c1740524b88"
bot_token = "6563744619:AAG4v_ABfLA3lCSGbcNLWlS07ZA_qUmseqM"

app = Client("my_account", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

app.run()
