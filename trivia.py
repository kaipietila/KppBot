import requests
from discord.ext import commands
"""
jeopardy question quiz cog
"""
class Trivia():
    def __init__(self, bot):
        self.bot = bot

    def get_random_question(self, amount=1):
        try:
            questions = requests.get("http://jservice.io/api/random", data={'count':f'{amount}'}).json()
            return questions
        except Exception as e:
            print(e)

    @commands.command()
    async def quiz(self):
        quiz_data = get_random_question()
        question = quiz_data[0]['question']
        answer = quiz_data[0]['answer']
        await self.bot.say(question)
        await asyncio.sleep(5)
        await self.bot.say(answer)


def setup(bot):
    bot.add_cog(Trivia(bot))