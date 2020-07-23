import os
import discord

key = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print("------")
    # To start background tasks
    game_info.start()

async def game_info():
    activity = discord.Activity(name="testing", type=discord.ActivityType.playing)
    await bot.change_presence(activity=activity)
	
	
client.run(key, bot=False) 