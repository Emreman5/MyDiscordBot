from discord.ext import commands
import discord
from discord import ChannelType
import time

class dolmus(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def dolmus(self,ctx,*args):
        if len(args) == 0:
            if ctx.author.voice and ctx.author.voice.channel:
                channels = ctx.guild.voice_channels
                current_channel = ctx.author.voice.channel
                await ctx.send(f"**{ctx.author.name} BALONU ENGİZ DOLMUŞUNA BİNİYOR... **")
                while True:
                    for i in channels:
                        await ctx.author.move_to(i)
                        time.sleep(1)
                    await ctx.author.move_to(current_channel)
            else:
                await ctx.send("Kanalda değilsin")
        else:
           await ctx.send("siktir git")


def setup(bot):
    bot.add_cog(dolmus(bot))
