from pyrogram import client, filters

api_id = 20058505
api_hash = "c6416428be72db3174999c1740524b88"
bot_token = "6563744619:AAG4v_ABfLA3lCSGbcNLWlS07ZA_qUmseqM"

app = client("Join Bot",api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_mesaage(filters.command('start')&filters.private)
async def start(client, message):
    await message.reply("Hello User! \nI am Join Bot made by my master! \nI have been rebooted by my Master!!!")


app.run()
