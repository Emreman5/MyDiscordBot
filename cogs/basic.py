from discord.ext import commands

class basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def sa(self, ctx):
       await ctx.send("as")
    
def setup(bot):
    bot.add_cog(basic(bot))