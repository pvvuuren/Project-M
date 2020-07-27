import os
import discord

key = os.environ['TOKEN']

#CREATE THE BOT INSTANCE
client = discord.Client(self_bot=True)

client.run(key, bot=False)