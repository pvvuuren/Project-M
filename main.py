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
 
 key = os.environ['TOKEN']

# Creating selfbot instance
bot = commands.Bot(command_prefix=PREFIX, self_bot=True)

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
bot.run(key, bot=False)
