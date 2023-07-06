from math import log2
import discord as d
from discord.ext.commands import has_permissions
from bot.models import Duel
from bot.constants import (
    ABOUT_DESCRIPTION,
    ABOUT_FOOTER,
    ABOUT_TITLE,
    PRIMARY_COLOR,
    TOP_25_TAGS,
)
from bot.utils import add_fields
from services.codeforces.exceptions import CFStatusFailed
from services.codeforces.methods import problemset_problems, user_info
from services.db import add_duel, get_handle, set_handle


bot = d.Bot(
    intents=d.Intents.all(),
    activity=d.Activity(type=d.ActivityType.playing, name="Duel against Tourist"),
)


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


@bot.slash_command()
async def ping(ctx):
    """Sends the bot's latency in miliseconds"""
    embed = d.Embed(color=PRIMARY_COLOR)
    embed.description = f"Latency is {int(bot.latency*1000)}ms"
    await ctx.respond(embed=embed, ephemeral=True)


@bot.slash_command()
async def handle_set(
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
        if uid == bot.user.id:  # type: ignore
            embed.description = "I don't have a codeforces account :sob:"
        else:
            set_handle(uid, handle)
            add_fields(embed, user)
            embed.set_thumbnail(url=user.avatar)
            embed.description = f"Handle of <@{uid}> set to `{handle}`"
    except CFStatusFailed as e:
        embed.description = str(e)
    await ctx.respond(embed=embed, ephemeral=True)


@bot.slash_command()
async def handle_get(
    ctx: d.ApplicationContext,
    member: d.Option(d.Member, description="Member of this server"),  # type: ignore
):
    """Look up someone's handle

    Handled Cases:
    - Member mentioned is the bot itself
    - CFStatusFailed
    """
    embed = d.Embed(color=PRIMARY_COLOR)
    if member.id == bot.user.id:  # type: ignore
        embed.description = "I don't have a codeforces account :sob:"
    else:
        handle = get_handle(member.id)
        if handle:
            try:
                user = user_info(handles=[handle])[0]
                embed.set_thumbnail(url=user.avatar)
                add_fields(embed, user)
            except CFStatusFailed as e:
                embed.description = str(e)
        else:
            embed.description = f"<@{member.id}> didn't set their handle yet"
    await ctx.respond(embed=embed, ephemeral=True)


@bot.slash_command()
@d.guild_only()
async def duel_challenge(
    ctx: d.ApplicationContext,
    rating: d.Option(int, description="Rating of problem", required=True),  # type: ignore
    tag: d.Option(str, choices=TOP_25_TAGS, required=False),  # type: ignore
    opponent: d.Option(d.Member, description="Keep it blank for open duel", required=False),  # type: ignore
):
    """Challenge someone for a duel

    Handled Cases:
    - Opponent mentioned is the bot itself
    - Challengee or Challenger didn't set handle
    - Open challenge with no duelist in the server
    - CFStatusFailed
    """
    embed = d.Embed(color=PRIMARY_COLOR)
    duel = Duel(challengerId=ctx.user.id, rating=rating)
    existing_duel = add_duel(ctx.guild_id, duel)  # type: ignore
    if existing_duel:
        embed.description = f"There is already a duel between <@{existing_duel.challengeeId}> and <@{existing_duel.challengerId}>"
        await ctx.respond(embed=embed, ephemeral=True)
    else:
        embed.title = "Are you up for a duel?"
        embed.add_field(name="Opponent", value=f"<@{ctx.user.id}>")
        embed.add_field(name="Rating", value=str(rating))
        if tag:
            embed.add_field(name="Tag", value=tag)
        opponent_id = opponent.id if opponent else "UNDER CONSTRUCTION"
        await ctx.respond(f"<@{opponent_id}>", embed=embed, ephemeral=True)


@bot.slash_command(description="Withdraw a duel")
@d.guild_only()
async def duel_witdraw(ctx: d.ApplicationContext):
    embed = d.Embed(color=PRIMARY_COLOR)
    embed.description = "The feature is not implemented yet"
    await ctx.respond(embed=embed, ephemeral=True)


@bot.slash_command(description="Withdraw the current tournament")
@d.guild_only()
@has_permissions(moderate_members=True)
async def tournament_withdraw(ctx: d.ApplicationContext):
    embed = d.Embed(color=PRIMARY_COLOR)
    embed.description = "The feature is not implemented yet"
    await ctx.respond(embed=embed, ephemeral=True)


@bot.slash_command(description="Create a new tournament")
@d.guild_only()
@has_permissions(moderate_members=True)
async def tournament_create(
    ctx: d.ApplicationContext,
    n: d.Option(int, description="Number of players", required=True),  # type: ignore
):
    # verification
    embed = d.Embed(color=PRIMARY_COLOR)
    embed.description = (
        "Number of players should be\n"
        ":point_right: an integer\n"
        ":point_right: a power of 2\n"
        ":point_right: between [8,128]"
    )
    if not n.isdecimal():
        await ctx.respond(embed=embed, ephemeral=True)
        return
    n = log2(int(n))
    if not (n.is_integer() and 3 <= n <= 7):
        await ctx.respond(embed=embed, ephemeral=True)
        return

    # TODO
    embed.description = "The feature is not implemented yet"
    await ctx.respond(embed=embed, ephemeral=True)


@bot.slash_command(name="about", description="Get to know খেলিলি আইয়ুন")
async def about(ctx: d.ApplicationContext):
    embed = d.Embed(
        title=ABOUT_TITLE,
        description=ABOUT_DESCRIPTION,
        color=PRIMARY_COLOR,
    )
    embed.set_footer(text=ABOUT_FOOTER)
    await ctx.respond(embed=embed, ephemeral=True)
