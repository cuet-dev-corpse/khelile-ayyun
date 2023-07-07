import os
from dotenv import load_dotenv
from bot import bot

BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, ".env-var"))

bot.run(os.getenv("TOKEN"))
