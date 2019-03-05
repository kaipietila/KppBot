import requests
import asyncio
from discord.ext import commands
"""
jeopardy question quiz cog
"""

def get_random_question(amount=1):
        try:
            questions = requests.get("http://jservice.io/api/random", data={'count':f'{amount}'}).json()
            return questions
        except Exception as e:
            print(e)

class Trivia():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def quiz(self):
        quiz_data = get_random_question()
        question = quiz_data[0]['question']
        answer = quiz_data[0]['answer']
        await self.bot.say(f'Question: {question}')
        await asyncio.sleep(5)
        await self.bot.say(f'Answer: {answer}')


def setup(bot):
    bot.add_cog(Trivia(bot))