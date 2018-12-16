import discord
from vars import *
import random
from bs4 import BeautifulSoup
import requests

TOKEN = DISCORD_BOT_SECRET

client = discord.Client()

possible_answers = [
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
        roll_record = open("roll_record.txt", "a")
        user = "{0.author.mention}".format(message)
        msg = f"{user} rolls {roll}"
        roll_record.write(f"{msg}\n")
        roll_record.close()
        await client.send_message(message.channel, msg)

    if message.content.startswith("!results"):
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

    if message.content.startswith("!8ball"):
        await client.send_message(message.channel, random.choice(possible_answers))
    

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)