from discord.ext import commands

class handling(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_command_error(self,ctx,ex):
        if isinstance(ex, commands.CommandNotFound):
            return
        print(ex)
        await ctx.send("Hop napüyün")


def setup(bot):
    bot.add_cog(handling(bot))