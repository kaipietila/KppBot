from discord.ext import commands

#get the bot secret token from txt file
TOKEN = open('config.txt', 'r').read()

description = 'KppBot at your service. Get commands from !commands'

startup_extensions = ['roll', '8ball', 'steam', 'trivia', 'chatwheel']

bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def hello(ctx):
    msg = 'Hello {0.message.author.mention}'.format(ctx)
    await ctx.send(msg) 

@bot.command()
async def kill(ctx):
    """
    Kills connection
    """
    await ctx.send("shutting down")
    await bot.close()

@bot.command()
async def comms(ctx):
    commands = ("Bot Commands: \n!roll to roll 0-100 \n!results for the roll results\n"
                "!8ball + question to ask the magic 8ball a question \n"
                "!hello for a simple hello and\n!steam to get the ~10 most played games on steam."
                "Steam command does not work well atm"
                "!quiz you get a question, jeopardy style")
    await ctx.send(commands)


if __name__ == "__main__":
    """loading extensions on startup"""
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
            print(f'{extension} loaded successfully!')
        except Exception as e:
            print(f'Failed to load {extension} \n{e}')

    bot.run(TOKEN)