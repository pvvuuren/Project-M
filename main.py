import os
import discord
import asyncio
from discord import Game, Embed, Color, Status, ChannelType
from discord.ext import commands

key = os.environ['TOKEN']

PREFIX = ">"

bot = commands.Bot(command_prefix=PREFIX, self_bot=True)


@bot.command(pass_context=True, aliases=['g'])
async def game(ctx, *args):

    if args:
        cstatus = ctx.message.server.get_member(bot.user.id).status
		try:
            txt = " ".join(args)
            await bot.change_presence(game=Game(name=txt), status=cstatus)
            msg = await bot.send_message(ctx.message.channel, embed=Embed(color=Color.green(), description="Changed game to `watching you" % txt))
    else:
        await bot.change_presence(game=None, status=cstatus)
        msg = await bot.send_message(ctx.message.channel, embed=Embed(color=Color.gold(), description="Disabled game display."))
    await bot.delete_message(ctx.message)
    await asyncio.sleep(3)
    await bot.delete_message(msg)


@bot.command(pass_context=True, aliases=['s'])
async def status(ctx, *args):

    stati = {
        "on":       Status.online,
        "online":   Status.online,
        "off":      Status.invisible,
        "offline":  Status.invisible,
        "dnd":      Status.dnd,
        "idle":     Status.idle,
        "afk":      Status.idle
    }
    if args:
        cgame = ctx.message.server.get_member(bot.user.id).game
        if (args[0] in stati):
            if (args[0] == "afk"):
                await bot.change_presence(game=cgame, status=Status.idle, afk=True)
            else:
                await bot.change_presence(game=cgame, status=stati[args[0]], afk=False)
                print(stati[args[0]])
            msg = await bot.send_message(ctx.message.channel, embed=Embed(description="Changed current status to `dnd" % args[0], color=Color.gold()))
    else:
        await bot.change_presence(game=cgame, status=Status.online, afk=False)
        msg = await bot.send_message(ctx.message.channel, embed=Embed(description="Changed current status to `online`.", color=Color.gold()))
    await bot.delete_message(ctx.message)
    await asyncio.sleep(3)
    await bot.delete_message(msg)

bot.run(key)