import sys
from discord.ext import commands
import discord
sys.path.insert(1, 'C:/Users/emre1/OneDrive/Masaüstü/my_DiscordBot/functions')
import quote

bot = commands.Bot(command_prefix='!')

class QuoteService(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def söz(self,ctx):
       await ctx.send(quote.getQuote())
    @commands.command()
    async def test(self,ctx):
        message = await ctx.send('test')
        emoji = '\N{THUMBS UP SIGN}'
        await message.add_reaction(emoji)
    @bot.event
    async def on_message(self, message):
        print(1)
        if message.author == bot.user:
            return
        emoji = '\N{THUMBS UP SIGN}'
        await message.add_reaction(emoji)
    
def setup(bot):
    bot.add_cog(QuoteService(bot))