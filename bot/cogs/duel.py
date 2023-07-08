from typing import Optional
import discord as d
from discord.ext import commands
from bot.constants import EMOJI_WARNING, PRIMARY_COLOR, TOP_25_TAGS
from services import db
from bot import models


class Duel(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.slash_command()
    @d.guild_only()
    async def duel_challenge(
        self,
        ctx: d.ApplicationContext,
        rating: d.Option(int, description="Rating of problem", required=True),  # type: ignore
        tag: d.Option(str, choices=TOP_25_TAGS, required=False),  # type: ignore
        opponent: d.Option(d.Member, description="Keep it blank for open duel", required=False),  # type: ignore
    ):
        """Challenge someone for a duel

        Handled Cases:
        - Opponent mentioned is the bot itself
        - Challengee or Challenger didn't set handle
        - Challengee or Challenger already in a duel
        - Open challenge with no duelist in the server
        - CFStatusFailed
        """
        embed = d.Embed(color=PRIMARY_COLOR)
        opponent_id = opponent.id if opponent else None
        if opponent_id == self.bot.user.id:  # type: ignore
            embed.description = ":sob: I don't have a codeforces account"
            await ctx.respond(embed=embed, ephemeral=True)
            return
        if not db.get_handle(ctx.user.id):
            embed.description = f"{EMOJI_WARNING} <@{ctx.user.id}>, please set your handle using /handle_set first"
            await ctx.respond(f"<@{ctx.user.id}>", embed=embed, ephemeral=True)
            return
        if opponent_id and not db.get_handle(opponent_id):
            embed.description = f"{EMOJI_WARNING} <@{opponent_id}>, please set your handle using /handle_set first"
            await ctx.respond(f"<@{opponent_id}>", embed=embed, ephemeral=True)
            return
        duel = models.Duel(challengerId=ctx.user.id, challengeeId=opponent_id, rating=rating)
        existing_duel = db.add_duel(ctx.guild_id, duel)  # type: ignore
        if existing_duel:
            if existing_duel.challengeeId == None:
                embed.description = (
                    f"<@{existing_duel.challengerId}>, you are already in an open duel"
                )
            else:
                embed.description = f"<@{existing_duel.challengerId}>, you are already in a duel with <@{existing_duel.challengeeId}>"
            await ctx.respond(embed=embed, ephemeral=True)
        else:
            opponent_mention: Optional[str] = None
            if opponent_id:
                opponent_mention = f"<@{opponent_id}>"
            else:
                for role in ctx.guild.roles:  # type: ignore
                    if role.name == "duelist":
                        opponent_mention = role.mention
            if not opponent_mention:
                embed.description = f"{EMOJI_WARNING} This server does not have `duelist` role. Please use /duelist_create_role to create the role"
                await ctx.respond(embed=embed, ephemeral=True)
                return
            embed.title = "Are you up for a duel?"
            embed.add_field(name="Opponent", value=f"<@{ctx.user.id}>")
            embed.add_field(name="Rating", value=str(rating))
            if tag:
                embed.add_field(name="Tag", value=tag)
            await ctx.respond(opponent_mention, embed=embed, ephemeral=True)

    @commands.slash_command(description="Withdraw a duel")
    @d.guild_only()
    async def duel_witdraw(self, ctx: d.ApplicationContext):
        embed = d.Embed(color=PRIMARY_COLOR)
        embed.description = "The feature is not implemented yet"
        await ctx.respond(embed=embed, ephemeral=True)


def setup(bot):
    bot.add_cog(Duel(bot))
