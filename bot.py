from discord.ext import commands

#get the bot secret token from txt file
TOKEN = open('config.txt', 'r').read()

description = 'KppBot at your service. Get commands from !commands'

startup_extensions = ['roll', '8ball', 'steam', 'trivia', ]

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
    commands = ("Bot Commands: \n!roll to roll 0-100 \n!record for the roll results\n"
                "!8ball + question to ask the magic 8ball a question \n"
                "!hello for a simple hello and\n!steam to get the ~10 most played games on steam."
                "Steam command does not work well atm")
    await ctx.send(commands)

@bot.command()
async def load(extension_name, ctx):
    """manual loading of extension"""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await ctx.send(f"```py\n{str(e)}\n```")
        return
    await ctx.send(f"{extension_name} loaded, Have fun!")

if __name__ == "__main__":
    """loading extensions on startup"""
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load {extension} \n{e}')

    bot.run(TOKEN)