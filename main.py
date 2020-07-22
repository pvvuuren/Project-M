--- channel.py.old  2017-02-27 15:02:23.000000000 -0800
+++ channel.py  2020-07-22 02:44:03.000000000 -0700
@@ -27,13 +27,28 @@
 from . import utils
 from .permissions import Permissions, PermissionOverwrite
 from .enums import ChannelType
-from collections import namedtuple
 from .mixins import Hashable
 from .role import Role
 from .user import User
 from .member import Member
import os
import discord
import asyncio
import giphypop

from discord.ext import commands
 
-Overwrites = namedtuple('Overwrites', 'id allow deny type')
+class Overwrites:
+    __slots__ = ('id', 'allow', 'deny', 'type')
+
+    def __init__(self, **kwargs):
+        self.id = kwargs.pop('id')
+        self.allow = kwargs.pop('allow', 0)
+        self.deny = kwargs.pop('deny', 0)
+        self.type = kwargs.pop('type')
+
+    def _asdict(self):
+        return {
+            'id': self.id,
+            'allow': self.allow,
+            'deny': self.deny,
+            'type': self.type,
+        }
+
 
 class Channel(Hashable):

key = os.environ['TOKEN']
PREFIX = ">"

# Creating selfbot instance
bot = commands.Bot(command_prefix=PREFIX, self_bot=True)

###################
# C O M M A N D S #
###################

#@bot.command(pass_context=True, aliases=['g'])
#async def game(ctx, *args):
	#if args:
        #cstatus = ctx.message.server.get_member(bot.user.id).status
        #txt = " ".join(args)
        #await bot.change_presence(game=Game(name=txt), status=cstatus)
        #msg = await bot.send_message(ctx.message.channel, embed=Embed(color=Color.green(), description="Changed game to `%s`!" % txt))
    #else:
        #await bot.change_presence(game=None, status=cstatus)
        #msg = await bot.send_message(ctx.message.channel, embed=Embed(color=Color.gold(), description="Disabled game display."))
    #await bot.delete_message(ctx.message)
    #await asyncio.sleep(3)
    #await bot.delete_message(msg)


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
            msg = await bot.send_message(ctx.message.channel, embed=Embed(description="Changed current status to `%s`." % args[0], color=Color.gold()))
    else:
        await bot.change_presence(game=cgame, status=Status.online, afk=False)
        msg = await bot.send_message(ctx.message.channel, embed=Embed(description="Changed current status to `online`.", color=Color.gold()))
    await bot.delete_message(ctx.message)
    await asyncio.sleep(3)
    await bot.delete_message(msg)
bot.run(key, bot=False)
