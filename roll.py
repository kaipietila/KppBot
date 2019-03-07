import random
import discord
from discord.ext import commands
"""
RNG rolling cog to KppBot. In RNGesus we trust!
"""
    
class Roll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def roll(self, ctx, limit = 100):
        """Rolls a dice or something for the user. Limit by default 100
        but can be changed by entering something"""
        user_roll = random.randint(1, limit)
        user = ctx.message.author.mention
        msg = f"{user} rolls {user_roll}"
        
        with open("roll_record.txt", "a") as f:
            f.write(f"{msg}\n")
        
        await ctx.send(msg)

    @commands.command()
    async def results(self, ctx):
        """Says the roll results on file"""
        with open("roll_record.txt", "r") as f:
            record = f.read()
        if len(record)>0:   
            await ctx.send(record)
        else:
            await ctx.send("No results to show")

    @commands.command(name = "clear_all")
    async def clear_results(self, ctx):
        """Erase results list"""
        open("roll_record.txt", "w").close()
        await ctx.send("Results have been resetted")

def setup(bot):
    bot.add_cog(Roll(bot))
