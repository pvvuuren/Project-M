import os
import discord
import asyncio
import giphypop
from discord import game, status

key = os.environ['TOKEN']

client = discord.Client()

async def background_loop():
    await client.change_presence(game=discord.Game(name="testing"))
	await asyncio.sleep(3)

client.run(key, bot=False)
