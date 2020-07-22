import os
import discord
import asyncio
import giphypop
#from discord import game, status
from discord.ext import commands

key = os.environ['TOKEN']

# Creating selfbot instance
bot = commands.Bot(command_prefix=PREFIX, self_bot=True)

@bot.command(pass_context=True, aliases=['s'])

bot.run(key, bot=False)
