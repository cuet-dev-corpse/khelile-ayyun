import discord as d
from discord.ext import commands
from bot.constants import EMOJI_INFO, PRIMARY_COLOR


class Ping(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.slash_command()
    async def ping(self, ctx):
        """Sends the bot's latency in miliseconds"""
        embed = d.Embed(color=PRIMARY_COLOR)
        embed.description = f"{EMOJI_INFO} Latency is {int(self.bot.latency*1000)}ms"
        await ctx.respond(embed=embed, ephemeral=True)


def setup(bot):
    bot.add_cog(Ping(bot))
