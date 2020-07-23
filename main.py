import os
import discord
from discord.ext import commands, tasks

key = os.environ['TOKEN']

client = commands.Bot(command_prefix="$")

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print("------")
    # To start background tasks
    game_info.start()

@tasks.loop(minutes=2)
async def game_info():
    activity = discord.Activity(name="testing", type=discord.ActivityType.playing)
    await client.change_presence(activity=activity)


client.run(key)