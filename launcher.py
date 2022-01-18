from unittest import async_case
from discord.ext import commands
from settings import *
import os
from discord.utils import find

bot = commands.Bot(command_prefix='!')
LOCK = 1


for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f"cogs.{filename[:-3]}")


print("BOT HAZIRR")
bot.run(TOKEN)
