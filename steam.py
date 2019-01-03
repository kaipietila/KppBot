import random
from bs4 import BeautifulSoup
import requests
from discord.ext import commands
"""
Scraping steampowered.com for the most played games.
Command !steam will display the about 10 most played games on steam.
"""

class Steam():
    def __init__(self, bot):
        self.bot = bot
            
    @commands.command()
    async def steam(self):
        data = requests.get("https://store.steampowered.com/stats/?l=finnish")
        msg = 'The most played games on steam right now are:\n'
        position = 1
        soup = BeautifulSoup(data.text, 'html.parser')
        leaderboard = soup.find('div', {'id': 'detailStats'})
        table = leaderboard.find('table')

        for tr in table.find_all('tr',{'class': 'player_count_row'}):
            current_users = tr.find_all('td')[0].text.strip()
            game = tr.find_all('td')[3].text.strip()
            msg += (f'{position}. {current_users} playing {game}\n')
            position += 1
            if len(msg) > 450:
                break
        
        await self.bot.say(msg)


def setup(bot):
    bot.add_cog(Steam(bot))