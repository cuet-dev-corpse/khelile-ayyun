from math import log2
from typing import Optional
import discord as d
from bot.models import Duel
from bot.constants import (
    ABOUT_DESCRIPTION,
    ABOUT_FOOTER,
    ABOUT_TITLE,
    EMOJI_SUCCESS,
    EMOJI_WARNING,
    PRIMARY_COLOR,
    TOP_25_TAGS,
)
from bot.utils import add_fields
from services.codeforces.exceptions import CFStatusFailed
from services.codeforces.methods import problemset_problems, user_info
from services import db

bot = d.Bot(
    intents=d.Intents.all(),
    activity=d.Activity(type=d.ActivityType.playing, name="Duel against Tourist"),
)

cog_list = [
    "about",
    "ping",
    "handle",
    "duelist",
    "duel"
]

for cog in cog_list:
    bot.load_extension(f"bot.cogs.{cog}")


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
