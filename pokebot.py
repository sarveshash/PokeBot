import asyncio
from pyrogram import Client

api_id = 20058505
api_hash = "c6416428be72db3174999c1740524b88"


async def main():
    async with Client("my_account", api_id, api_hash) as app:
        await app.send_message("me", "Greetings from **Pyrogram**!")


asyncio.run(main())
