import discord, random
from discord.ext import commands
from imgurpython import ImgurClient

TOKEN = 'TOKEN CODE GOES HERE'
bot = commands.Bot(command_prefix = '!')

client_id = 'CLIENT IT GOES HERE'
client_secret = 'CLIENT SECRET GOES HERE'
client = ImgurClient(client_id, client_secret)

@bot.event
async def on_ready():
    print('Kitty Bot is ready.')

# Posts imgur links from r/aww
@bot.command()
async def aww(ctx):
    images = client.subreddit_gallery(subreddit='aww')
    rand = random.choice(images)
    await ctx.send(rand.link)

# Posts imgur links from r/kitties
@bot.command()
async def kitty(ctx):
    images = client.subreddit_gallery(subreddit='kitties')
    rand = random.choice(images)
    await ctx.send(rand.link)

# Posts imgur links from r/rarepuppers
@bot.command()
async def pupper(ctx):
    images = client.subreddit_gallery(subreddit='rarepuppers')
    rand = random.choice(images)
    await ctx.send(rand.link)

bot.run(TOKEN)
