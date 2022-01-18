from discord.ext import commands
class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self,ctx):
        await ctx.send("pong")
    @commands.command()
    async def bin(self,ctx):
        await ctx.send("** Engiz Dolmuşuna biniliyor... **")

def setup(bot):
    bot.add_cog(Test(bot))