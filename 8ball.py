import random
from discord.ext import commands
"""
Magic 8ball cog to KppBot
"""

class EightBall():
    def __init__(self, bot):
        self.bot = bot
        self.possible_answers = [
                "It is certain",
                "It is decidedly so",
                "Without a doubt",
                "Yes - definitely",
                "You may rely on it",
                "As I see it, yes",
                "Most likely",
                "Outlook good",
                "Yes"
                "Signs point to yes",
                "Reply hazy, try again",
                "Ask again later",
                "Better not tell you now",
                "Cannot predict now",
                "Concentrate and ask again",
                "Don't count on it",
                "My reply is no",
                "My sources say no",
                "Outlook not so good",
                "Very doubtful",
            ]
    @commands.command(name="8ball")
    async def eightball(self, message=''):
        """!8ball will display one of the possible answers 
        and reply like the magic 8ball"""
        if len(message) != 0:
            await self.bot.say(random.choice(self.possible_answers))
        else: 
            await self.bot.say("What question do you want to ask me?")

def setup(bot):
    bot.add_cog(EightBall(bot))