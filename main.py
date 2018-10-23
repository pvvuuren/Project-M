import os
import discord
import asyncio
import random
from copy import deepcopy

key = os.environ['TOKEN']

client = discord.Client()

async def background_loop():
    await client.wait_until_ready()
    await client.change_presence(game=discord.Game(name="Watching you"))
	await asyncio.sleep(21600)

client.loop.create_task(background_loop())
client.run(key)