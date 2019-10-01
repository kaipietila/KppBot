import discord
from discord.ext import commands

"""
Dota 2 Chatwheel cog to KppBot. Play chatwheel voice emotes until the sun comes up.
"""
    
class Chatwheel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx, emote):
        pass

    @commands.command(name="join")
    async def join(self, ctx):
        client = ctx.guild.voice_client
        await client.connect()

    @commands.command()
    async def leave(self, ctx):
        server = ctx.message.server
        voice_channel = self.bot.voice_channel_in(server)
        await voice_channel.disconnect()
        
def setup(bot):
    bot.add_cog(Chatwheel(bot))
