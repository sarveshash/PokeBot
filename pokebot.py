import asyncio
from pyrogram import Client

app = Client("Bot")

async def main():
  async with app:
    await app.send_message("me","Hi")

app.run(main())
