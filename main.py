import discord
import os  # default module
from dotenv import load_dotenv
from discord import ApplicationContext
from constants import PRIMARY_COLOR, ABOUT_DESCRIPTION, ABOUT_TITLE, ABOUT_FOOTER

BASEDIR = os.path.abspath(os.path.dirname(__file__))
# load all the variables from the env file
load_dotenv(os.path.join(BASEDIR, '.env-var'))
bot = discord.Bot(
    intents=discord.Intents.all(),
    activity=discord.Activity(
        type=discord.ActivityType.playing,
        name="Duel against Tourist",
    ),
    status=discord.Status.dnd,
)


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


@bot.slash_command(name="duel", description="Play duel against an opponent")
async def duel(ctx: ApplicationContext):
    await ctx.respond("The feature is not implemented yet", ephemeral=True)


@bot.slash_command(name="about", description="Get to know খেলিলি আইয়ুন")
async def about(ctx: ApplicationContext):
    embed = discord.Embed(title=ABOUT_TITLE, description=ABOUT_DESCRIPTION, color=PRIMARY_COLOR)
    embed.set_footer(text=ABOUT_FOOTER)
    await ctx.respond(embed=embed, ephemeral=True)

bot.run(os.getenv('TOKEN'))  # run the bot with the token
