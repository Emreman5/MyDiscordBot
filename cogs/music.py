from discord.ext import commands
import youtube_dl
import discord

class music(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def gel(self,ctx):
        if ctx.author.voice is None:
            await ctx.send(f"**Kanalda değilsin** {ctx.author.mention}")
            return
        if ctx.voice_client is None:
            voice_channel = ctx.author.voice.channel
            await voice_channel.connect()
            return
        else:
            voice_channel = ctx.author.voice.channel
            await ctx.voice_client.move_to(voice_channel)
            return
    @commands.command()
    async def çık(self,ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def oynat(self,ctx,url):
        FFMPEG_OPTS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTS = {'format': 'bestaudio'}
        vc = ctx.voice_client
        with youtube_dl.YoutubeDL(YDL_OPTS) as ydl:
            info = ydl.extract_info(url,download = False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTS)
            vc.play(source)
    @commands.command()
    async def durdur(self,ctx):
        await ctx.voice_client.pause()
        await ctx.send("Durduruldu")
    @commands.command()
    async def devam(self, ctx):
        await ctx.voice_client.resume()
        await ctx.send("Devam ke")
def setup(bot):
    bot.add_cog(music(bot))