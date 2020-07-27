import os
import discord

key = os.environ['TOKEN']

#CREATE THE BOT INSTANCE
client = discord.Client()

client.run(key, bot=False)