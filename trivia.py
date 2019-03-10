import requests
import asyncio
from discord.ext import commands
from random import randint
"""
jeopardy question quiz cog
"""

def get_random_question(difficulty=100):
    try:
        questions = requests.get("http://jservice.io/api/clues", data={'value':f'{difficulty}'}).json()
        return questions
    except Exception as e:
        print(e)

class Trivia(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
        self.timeout = 10           

    @commands.command()
    async def quiz(self, ctx):
        quiz_data = get_random_question()
        index = randint(0, 100)
        question = quiz_data[index]['question']
        answer = quiz_data[index]['answer'].lower()
        await ctx.send(question)

        def check(m):
            return m.content.lower() == answer

        try:
            msg = await self.bot.wait_for('message', check=check, timeout=self.timeout) 
        except asyncio.TimeoutError:
            await ctx.send(f"The correct answer was {answer}")
        else:
            await ctx.send(f'Correct {msg.author}!')

        

def setup(bot):
    bot.add_cog(Trivia(bot))