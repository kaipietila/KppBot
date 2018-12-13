import discord
from vars import *
import random
from bs4 import BeautifulSoup
import requests

TOKEN = DISCORD_BOT_SECRET

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith("!roll"):
        roll = random.randint(0,100)
        user = "{0.author.mention}".format(message)
        msg = f"{user} rolls {roll}"
        with open("roll_record.txt", "a") as f:
            f.write(f"{msg}\n")

        await client.send_message(message.channel, msg)

    if message.content.startswith("!legend"):
        roll_record = open("roll_record.txt", "r")
        record = roll_record.read()
        roll_record.close()
        await client.send_message(message.channel, record)

    if message.content == ("!steam"):
        data = requests.get("https://store.steampowered.com/stats/?l=finnish")
        msg = ''
        soup = BeautifulSoup(data.text, 'html.parser')

        leaderboard = soup.find('div', {'id': 'detailStats'})
        table = leaderboard.find('table')

        for tr in table.find_all('tr',{'class': 'player_count_row'}):
            current_users = tr.find_all('td')[0].text.strip()
            game = tr.find_all('td')[3].text.strip()
            msg = (f'{current_users} playing {game}')
            await client.send_message(message.channel, msg)
    

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)