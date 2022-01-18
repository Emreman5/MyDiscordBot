from unittest import async_case
from discord.ext import commands
import discord
import aiohttp
CATEGORIES = ["waifu","neko","shinobu","cuddle","kill"]
class EmbeddedImages(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def animeli(self,ctx,*args):
        if len(args) > 0 and args[0] in CATEGORIES:
            async with aiohttp.ClientSession() as cs:
                async with cs.get(f"https://api.waifu.pics/sfw/{args[0]}") as r:
                    data = await r.json()
                    embed = discord.Embed(title=f"{args[0]}")
                    embed.set_image(url = data["url"])
                    embed.set_footer(text = "Ah be abim")
                    await ctx.send(embed=embed)
        else:
            await ctx.send("Tanımlı kategori giriniz")

def setup(bot):
    bot.add_cog(EmbeddedImages(bot))