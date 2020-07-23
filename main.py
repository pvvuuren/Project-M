import os
import discord

key = os.environ['TOKEN']

client = discord.Client()

async def background_loop():
    await client.change_presence(game=discord.Game(name="testing"))

client.run(key)