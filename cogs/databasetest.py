from discord.ext import commands
import pyodbc
import sys
sys.path.insert(1, 'C:/Users/emre1/OneDrive/Masaüstü/my_DiscordBot/DataAccess')
import context
import discord


conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=(localdb)\mssqllocaldb;"
    "Database=Northwind;"
    "Trusted_Connection=yes;"
)

class databaseTest(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.command()    
    async def Kullanıcılar(self,ctx):
        data = context.GetUsers()
        embed = discord.Embed(title = "Sample Embed", description = "Kullanıcılar Listesi ", color = discord.Color.red())
        embed.set_author(name= "Engiz Dolmuşu", icon_url="https://www.truck1.com.tr/img/auto/XXL/4486/4486_6811333511295.jpg")
        for i in data:
            embed.add_field(name=f"{i[0]}", value=i[1])
        await ctx.send(embed=embed)
    @commands.command()
    async def kayit(self,ctx):
        data = context.GetUsers()
        for i in data:
            if str(ctx.author.id) in i:
                await ctx.send("Zaten kayıtlısın")
                return 
        context.register(ctx.author)
        await ctx.send("Başarılı")
    @commands.command()
    async def kayıtsil(self,ctx):
        data = context.GetUsers()
        for i in data:
            if str(ctx.author.id) in i:
                context.Delete(ctx.author)
                await ctx.send("Kayıt başarıyla silindi")
                return
        await ctx.send("Kayıt Bulunamadı")

    @commands.command()
    async def kayitEt(self,ctx,target:discord.Member = None):
        if target is None:
            await ctx.send("???")
            return
        data = context.GetUsers()
        for i in data:
            if str(target.id) in i:
                await ctx.send("Zaten Kayıtlı")
                return 
        context.register(target)
        await ctx.send("Kayıt Başarılı")
        
        
def setup(bot):
    bot.add_cog(databaseTest(bot))