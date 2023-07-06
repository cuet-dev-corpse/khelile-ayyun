import os
from math import log2
from discord import (
    Activity,
    ActivityType,
    ApplicationContext,
    Bot,
    Embed,
    Intents,
    Member,
    Option,
    Status,
)
from discord.ext.commands import has_permissions
from dotenv import load_dotenv
from pydantic import BaseModel
from constants import (
    ABOUT_DESCRIPTION,
    ABOUT_FOOTER,
    ABOUT_TITLE,
    IGNORE_FIELDS,
    PRIMARY_COLOR,
    TOP_25_TAGS,
)
from services.cf_api.exceptions import CFStatusFailed
from services.cf_api.methods import problemset_problems, user_info
from services.db import get_handle, set_handle

# path of this file
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# load all the variables from the env file
load_dotenv(os.path.join(BASEDIR, ".env-var"))

# initialize the bot
bot = Bot(
    intents=Intents.all(),
    activity=Activity(type=ActivityType.playing, name="Duel against Tourist"),
    status=Status.do_not_disturb,
)
handle = bot.create_group("handle", "Codeforces handle")
duel = bot.create_group("duel", "Play Duel matches")
tournament = bot.create_group("tournament", "Play tournaments")


def add_fields(embed: Embed, model: BaseModel):
    for key, val in model.model_dump().items():
        if key not in IGNORE_FIELDS and val is not None:
            embed.add_field(name=key, value=str(val))


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


@bot.command(description="Sends the bot's latency.")
async def ping(ctx):
    embed = Embed(color=PRIMARY_COLOR)
    embed.description = f"Pong! Latency is {int(bot.latency*1000)}ms"
    await ctx.respond(embed=embed, ephemeral=True)


@handle.command(description="Register/change your codeforces handle")
async def set(
    ctx: ApplicationContext,
    handle: Option(str, description="Codeforces handle", required=True),  # type: ignore
    member: Option(Member, description="Member of this server", required=False),  # type: ignore
):
    embed = Embed(color=PRIMARY_COLOR)
    try:
        user = user_info(handles=[handle])[0]
        uid = member.id if member else ctx.user.id
        set_handle(uid, handle)
        add_fields(embed, user)
        embed.set_thumbnail(url=user.avatar)
        embed.description = f"Handle of <@{uid}> set to `{handle}`"
    except CFStatusFailed as e:
        embed.description = str(e)
    await ctx.respond(embed=embed, ephemeral=True)


@handle.command(description="Play duel against an opponent")
async def get(
    ctx: ApplicationContext,
    member: Option(Member, description="Member of this server"),  # type: ignore
):
    embed = Embed(color=PRIMARY_COLOR)
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


@duel.command(description="Play duel against an opponent")
async def challenge(
    ctx: ApplicationContext,
    rating: Option(int, description="Rating of problem", required=True),  # type: ignore
    tag: Option(str, choices=TOP_25_TAGS, required=False),  # type: ignore
    opponent: Option(Member, description="Keep it blank for open duel", required=False),  # type: ignore
):
    embed = Embed(color=PRIMARY_COLOR)
    await ctx.respond(embed=embed, ephemeral=True)


@duel.command(description="Play duel against an opponent")
async def witdraw(ctx: ApplicationContext):
    embed = Embed(color=PRIMARY_COLOR)
    embed.description = "The feature is not implemented yet"
    await ctx.respond(embed=embed, ephemeral=True)


@tournament.command(description="Cancel the current tournament")
@has_permissions(moderate_members=True)
async def withdraw(ctx: ApplicationContext):
    embed = Embed(color=PRIMARY_COLOR)
    embed.description = "The feature is not implemented yet"
    await ctx.respond(embed=embed, ephemeral=True)


@tournament.command(description="Create a new tournament")
@has_permissions(moderate_members=True)
async def create(
    ctx: ApplicationContext,
    n: Option(int, description="Number of players", required=True),  # type: ignore
):
    # verification
    embed = Embed(color=PRIMARY_COLOR)
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


@bot.command(name="about", description="Get to know খেলিলি আইয়ুন")
async def about(ctx: ApplicationContext):
    embed = Embed(
        title=ABOUT_TITLE,
        description=ABOUT_DESCRIPTION,
        color=PRIMARY_COLOR,
    )
    embed.set_footer(text=ABOUT_FOOTER)
    await ctx.respond(embed=embed, ephemeral=True)


bot.run(os.getenv("TOKEN"))  # run the bot with the token
