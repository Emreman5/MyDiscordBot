from unittest import async_case
from discord.ext import commands,tasks
from settings import *
import os
from discord.utils import find
import discord
bot = commands.Bot(command_prefix='',activity = discord.Game(name="Duygularınla"))


@bot.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'genel',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send(f'**SAKİN BEYLER ENGİZ DOLMUŞ GELDİ!**')
        await general.send("@everyone")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f"cogs.{filename[:-3]}")


print("BOT HAZIRR")
bot.run(TOKEN)
