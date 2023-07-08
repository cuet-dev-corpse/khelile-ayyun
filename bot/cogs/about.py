import discord as d
from discord.ext import commands
from bot.constants import ABOUT_DESCRIPTION, ABOUT_FOOTER, ABOUT_TITLE, PRIMARY_COLOR


class About(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.slash_command(name="about", description="Get to know খেলিলি আইয়ুন")
    async def about(self, ctx: d.ApplicationContext):
        embed = d.Embed(
            title=ABOUT_TITLE,
            description=ABOUT_DESCRIPTION,
            color=PRIMARY_COLOR,
        )
        embed.set_footer(text=ABOUT_FOOTER)
        await ctx.respond(embed=embed, ephemeral=True)


def setup(bot):
    bot.add_cog(About(bot))
