import discord
import os # default module
from dotenv import load_dotenv
from discord import ApplicationContext

BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env-var')) # load all the variables from the env file
bot = discord.Bot(intents=discord.Intents.all(), activity=discord.Activity(type=discord.ActivityType.playing, name="Duel against Tourist"))

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name = "hi", description = "Say hello to the bot")
async def hello(ctx: ApplicationContext):
    await ctx.respond("Hey!")

@bot.slash_command(name = "about", description = "Get to know খেলিলি আইয়ুন")
async def about(ctx: ApplicationContext):
    embed = discord.Embed(
        title="About খেলিলি আইয়ুন",
        description=(
            "খেলিলি আইয়ুন is a discord bot created to work as a helping hand for CP communities\n"
            "The name of the bot was inspired by মেজ্জান হাইলে আইয়ুন\n\n"
            ":point_right: Check out our GitHub repo [here](https://github.com/cuet-dev-corpse/khelile-ayyun)\n"
            ":construction: The bot is currently under construction. All features may not work properly"
        ),
        color=discord.Colour.from_rgb(65,135,235),
    )
    embed.set_footer(text="Made with 💖 by CUET Dev Corpse") # footers can have icons too
    await ctx.respond(embed=embed, ephemeral=True)

bot.run(os.getenv('TOKEN')) # run the bot with the token