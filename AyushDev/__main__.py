


import asyncio
import importlib

from pyrogram import idle

from Kawaii.modules import ALL_MODULES

loop = asyncio.get_event_loop()


async def initiate_bot():
    for all_module in ALL_MODULES:
        importlib.import_module("Kawaii.modules." + all_module)
    print("Started Kawaii AFK Bot.")
    await idle()
    print("GoodBye! Stopping Bot")


if __name__ == "__main__":
    loop.run_until_complete(initiate_bot())
