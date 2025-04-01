import logging
from discord.ext import commands
from discord import MessageType, ChannelType, Embed, Webhook


log = logging.getLogger("cogs.testing")


class Testing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


async def setup(bot):
    await bot.add_cog(Testing(bot))
