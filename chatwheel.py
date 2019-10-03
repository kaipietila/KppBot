import os
from pathlib import Path

import discord
from discord.ext import commands

"""
Dota 2 Chatwheel cog to KppBot. Play chatwheel voice emotes until the sun comes up.
"""
EMOTE_DIR = Path(__file__).resolve().parent.joinpath('emotes')

def find_emote(keyword):
    emotes = [f for f in os.listdir(EMOTE_DIR)]
    for emote in emotes:
        if keyword in emote:
            return emote
    else:
        return None

def find_and_play(voice, keyword):
    emote = find_emote(keyword)
    if emote:
        emote_path = os.path.join(EMOTE_DIR, emote)
        voice.play(discord.FFmpegPCMAudio(emote_path))
    else:
        raise ValueError

class Chatwheel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx, keyword):
        voice = ctx.voice_client
        if voice and voice.is_connected():
            try:
                find_and_play(voice, keyword)
            except ValueError:
                await ctx.send(f'Did not find anything with {keyword}')
        else:    
            channel = ctx.message.author.voice.channel
            if channel is None:
                await ctx.send('Your are not in a voice channel!')
                return False
            await channel.connect()
            voice = ctx.voice_client
            try:
                find_and_play(voice, keyword)
            except ValueError:
                await ctx.send(f'Did not find anything with {keyword}')
    
    @commands.command(name="emotes")
    async def emotes(self, ctx):
        emotes = [f for f in os.listdir(EMOTE_DIR)]
        for emote in emotes:
            emote = emote.replace('.mp3','')
            await ctx.send(f'{emote} available to play')

    @commands.command(name="join")
    async def join(self, ctx):
        channel = ctx.message.author.voice.channel
        if channel is None:
            await ctx.send('Your are not in a voice channel!')
            return False
        await channel.connect()

    @commands.command()
    async def leave(self, ctx):
        voice = ctx.voice_client
        if voice and voice.is_connected():
            await voice.disconnect()
        else:
            await ctx.send('Cant leave channel. sorry!')
        
def setup(bot):
    bot.add_cog(Chatwheel(bot))
