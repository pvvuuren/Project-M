import os
import discord

key = os.environ['TOKEN']

client = discord.Client()

@client.event
async def game_info():
    activity = discord.Activity(name="I am watching", type=discord.ActivityType.playing)
    await bot.change_presence(activity=activity)
	
	
client.run(key, bot=False) 