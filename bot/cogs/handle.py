import discord as d
from discord.ext import commands
from bot.constants import EMOJI_INFO, EMOJI_SOB, EMOJI_SUCCESS, EMOJI_WARNING, PRIMARY_COLOR
from bot.utils import add_fields
from services import db
from services.codeforces.exceptions import CFStatusFailed
from services.codeforces.methods import user_info


class Handle(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.slash_command()
    async def handle_set(
        self,
        ctx: d.ApplicationContext,
        handle: d.Option(str, description="Codeforces handle", required=True),  # type: ignore
        member: d.Option(d.Member, description="d.Member of this server", required=False),  # type: ignore
    ):
        """Register/change Codeforces handle

        Handled Cases:
        - Member mentioned is the bot itself
        - CFStatusFailed
            - Handle is not a valid CF handle
        """
        embed = d.Embed(color=PRIMARY_COLOR)
        try:
            user = user_info(handles=[handle])[0]
            uid = member.id if member else ctx.user.id
            if uid == self.bot.user.id:  # type: ignore
                embed.description = f"{EMOJI_SOB} I don't have a codeforces account"
            else:
                db.set_handle(uid, handle)
                add_fields(embed, user)
                embed.set_thumbnail(url=user.avatar)
                embed.description = (
                    f"{EMOJI_SUCCESS} Handle of <@{uid}> set to `{handle}`"
                )
        except CFStatusFailed as e:
            embed.description = f"{EMOJI_WARNING} {str(e)}"
        await ctx.respond(embed=embed, ephemeral=True)

    @commands.slash_command()
    async def handle_get(
        self,
        ctx: d.ApplicationContext,
        member: d.Option(d.Member, description="Member of this server"),  # type: ignore
    ):
        """Look up someone's handle

        Handled Cases:
        - Member mentioned is the bot itself
        - CFStatusFailed
        """
        embed = d.Embed(color=PRIMARY_COLOR)
        if member.id == self.bot.user.id:  # type: ignore
            embed.description = f"{EMOJI_SOB} I don't have a codeforces account"
        else:
            handle = db.get_handle(member.id)
            if handle:
                try:
                    user = user_info(handles=[handle])[0]
                    embed.description = f"{EMOJI_INFO} Here is everything I know about {member.mention}>"
                    embed.set_thumbnail(url=user.avatar)
                    add_fields(embed, user)
                except CFStatusFailed as e:
                    embed.description = str(e)
            else:
                embed.description = f"{EMOJI_WARNING} <@{member.id}> didn't set their handle yet"
        await ctx.respond(embed=embed, ephemeral=True)


def setup(bot):
    bot.add_cog(Handle(bot))
