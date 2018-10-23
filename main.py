import os
import discord      # pip3 install discord.py
import asyncio
from discord import Game, Embed, Color, Status, ChannelType
from discord.ext import commands
#from os import path

key = os.environ['TOKEN']

# Creating selfbot instance
bot = commands.Bot(command_prefix=PREFIX, description='''Selfbot by zekro''', self_bot=True)



###################
# C O M M A N D S #
###################

@bot.command(pass_context=True)
async def test(ctx, *args):
    """
    Just a command for testing purposes and debugging
    """
    print(ctx.message.server.get_member(bot.user.id).game)


@bot.command(pass_context=True, aliases=['g'])
async def game(ctx, *args):
    """
    Command for changing 'game' status
    """
    if args:
        cstatus = ctx.message.server.get_member(bot.user.id).status
        txt = " ".join(args)
        await bot.change_presence(game=Game(name=txt), status=cstatus)
        msg = await bot.send_message(ctx.message.channel, embed=Embed(color=Color.green(), description="Changed game to `%s`!" % txt))
    else:
        await bot.change_presence(game=None, status=cstatus)
        msg = await bot.send_message(ctx.message.channel, embed=Embed(color=Color.gold(), description="Disabled game display."))
    await bot.delete_message(ctx.message)
    await asyncio.sleep(3)
    await bot.delete_message(msg)


@bot.command(pass_context=True, aliases=['em', 'e'])
async def embed(ctx, *args):
    """
    Sending embeded messages with color (and maby later title, footer and fields)
    """
    colors = {
        "red": Color.red(),
        "green": Color.green(),
        "gold": Color.gold(),
        "orange": Color.orange(),
        "blue": Color.blue()
    }
    if args:
        argstr = " ".join(args)
        if "-c " in argstr:
            text = argstr.split("-c ")[0]
            color_str = argstr.split("-c ")[1]
            color = colors[color_str] if color_str in colors else Color.default()
        else:
            text = argstr
            color = Color.default()
        await bot.send_message(ctx.message.channel, embed=Embed(color=color, description=text))
    await bot.delete_message(ctx.message)


@bot.command(pass_context=True, aliases=['s'])
async def status(ctx, *args):
    """
    Change account status visible for others*
    *an effect of using a userbot is, that the bot displays your status as 'online'
    for other users while you can change your status to 'idle' or 'dnd', but
    noone will see it until the bot changes the status.
    """
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
            msg = await bot.send_message(ctx.message.channel, embed=Embed(description="Changed current status to `%s`." % args[0], color=Color.gold()))
    else:
        await bot.change_presence(game=cgame, status=Status.online, afk=False)
        msg = await bot.send_message(ctx.message.channel, embed=Embed(description="Changed current status to `online`.", color=Color.gold()))
    await bot.delete_message(ctx.message)
    await asyncio.sleep(3)
    await bot.delete_message(msg)


@bot.command(pass_context=True)
async def faq(ctx, *args):
    """
    Thats just a verry helpful command for myself because a lot of people
    asking me always the same questions in PM, so I can answer with
    this short command easily.
    """
    if args:
        if args[0] in FAQS:
            await bot.send_message(ctx.message.channel, embed=FAQS[args[0]][0])
    else:
        cont = ""
        for k, v in FAQS.items():
            cont += "*%s*  -  `%s`\n" % (v[1], k)
        await bot.send_message(ctx.message.channel, embed=Embed(description=cont))
    await bot.delete_message(ctx.message)


@bot.command(pass_context=True)
async def gif(ctx, *args):
    """
    A simple command to send gifs by keyword from giphy api
    """
    if args:
        query = " ".join(args)
        index = 0
        if " -" in query:
            try:
                index = int(query.split(" -")[1])
            except:
                pass
            query = query.split(" -")[0]
        giphy = giphypop.Giphy() if GIPHY_TOKEN == "" else giphypop.Giphy(api_key=GIPHY_TOKEN)
        gif = [x for x in giphy.search(query)][index]
        if gif:
            await bot.send_message(ctx.message.channel, gif)
    await bot.delete_message(ctx.message)


@bot.command(pass_context=True, aliases=['server'])
async def guild(ctx, *args):
    """
    Shows stats and information about current guild.
    ATTENTION: Please only use this on your own guilds or with explicit
    permissions of the guilds administrators!
    """
    if ctx.message.channel.is_private:
        await bot.delete_message(ctx.message)
        return

    g = ctx.message.server

    gid = g.id
    owner = [g.owner.name + "#" + g.owner.discriminator, g.owner.id]
    region = str(g.region)
    membs = str(len(g.members))
    membs_on = str(len([m for m in g.members if not m.status == Status.offline]))
    users = str(len([m for m in g.members if not m.bot]))
    users_on = str(len([m for m in g.members if not m.bot and not m.status == Status.offline]))
    bots = str(len([m for m in g.members if m.bot]))
    bots_on = str(len([m for m in g.members if m.bot and not m.status == Status.offline]))
    tchans = str(len([c for c in g.channels if c.type == ChannelType.text]))
    vchans = str(len([c for c in g.channels if c.type == ChannelType.voice]))
    created = str(g.created_at)
    roles = ", ".join([r.name for r in g.roles])

    em = Embed(title="Guild Information")
    em.description =    "```\n" \
                        "ID:        %s\n" \
                        "Owner:     %s (%s)\n" \
                        "Region:    %s\n" \
                        "Members:   %s (%s)\n" \
                        "  Users:   %s (%s)\n" \
                        "  Bots:    %s (%s)\n" \
                        "Channels:\n" \
                        "  Text:    %s\n" \
                        "  Voice:   %s\n" \
                        "Created:   %s\n" \
                        "Roles:\n" \
                        "%s" \
                        "```" % (gid, owner[0], owner[1], region, membs, membs_on, users, users_on, bots, bots_on, tchans, vchans, created, roles)

    await bot.send_message(ctx.message.channel, embed=em)
    await bot.delete_message(ctx.message)
        

@bot.command(pass_context=True, aliases=['google'])
async def lmgtfy(ctx, *args):
    """
    Just a simple lmgtfy command embeding the link into the message.*
    *Links are still visible because discord asks you if this link is safe :/
    """
    if args:
        url = "http://lmgtfy.com/?q=" + "+".join(args)
        await bot.send_message(ctx.message.channel, embed=Embed(description="**[Look here!](%s)**" % url, color=Color.gold()))
    await bot.delete_message(ctx.message)


@bot.command(pass_context=True, aliases=['gnick', 'gn'])
async def globalnick(ctx, *args):
    """
    With this command, you can change your nickname on all discord servers
    you are on and you have the permission to chnage your nickname.
    ATTENTION: Please don't overuse this command because I dont know,
    if it could lead to a discord account ban!
    """
    if args:
        newname = args[0]
        errors = []
        for s in bot.servers:
            await bot.edit_message(ctx.message, embed=Embed(description="Changing nickname on `%s`..." % s.name))
            try:
                await bot.change_nickname(s.get_member(bot.user.id), newname)
            except:
                errors.append(s.name)
                pass
        if errors:
            msg = await bot.send_message(ctx.message.channel, embed=Embed(color=Color.red(), description="**Failed changing nickanme on following servers:**\n\n" + "\n".join(errors)))
        else:
            msg = await bot.send_message(ctx.message.channel, embed=Embed(color=Color.green(), description="Successfully changed nick on all servers!"))
    await bot.delete_message(ctx.message)
    await asyncio.sleep(3)
    await bot.delete_message(msg)

bot.run(key)
