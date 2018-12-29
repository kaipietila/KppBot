import discord
import random
from bs4 import BeautifulSoup
import requests

TOKEN = open('config.txt', 'r').read()

client = discord.Client()

#answers for the !8ball command
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

    # With the command !hello the bot replies hello
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(message.channel, msg)

    #With the command !roll the bot rolls 0-100 for you
    if message.content.startswith("!roll"):
        roll = random.randint(0,100)
        user = "{0.author.mention}".format(message)
        msg = f"{user} rolls {roll}"
        with open("roll_record.txt", "a") as f:
            f.write(f"{msg}\n")
        await message.channel.send(msg)

    #command !results displays the roll results
    if message.content.startswith("!results"):
        with open("roll_record.txt", "r") as f:
            record = f.read()
        await message.channel.send(record)

    #Command !steam will display the 10 most played games on steam.
    if message.content == ("!steam"):
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
        
        await message.channel.send(msg)

    #command !8ball will display one of the possible answers and reply like the magic 8ball
    if message.content.startswith("!8ball"):
        await message.channel.send(random.choice(possible_answers))
    
    #to print to commandline whose mentioned. Work in progress on something
    if message.mentions != []:
        pass

    if message.content.startswith("!commands"):
        commands = ("Bot Commands: \n!roll to roll 0-100 \n!record for the roll results\n"
                    "!8ball + question to ask the magic 8ball a question \n"
                    "!hello for a simple hello and\n!steam to get the ~10 most played games on steam."
                    "Steam command does not work well atm")
        await message.channel.send(commands)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)