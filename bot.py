import discord
from discord import app_commands
from discord.ext import commands
import random
import time

BOT_TOKEN = "MTEwMTY4NjkyMzkyOTU4Mzc0OA.GJDUMV.f33eohR1zrulemkPFfunzbujy8vXgcHsXc4z2w"
CHANNEL_ID = 1096483275796652034

bot = commands.Bot("$", intents=discord.Intents.all())

def genNumber(start, end):
	number = random.randint(start, end)
	return number

@bot.event
async def on_ready():
	print('JAUB has started.')
	await bot.change_presence(activity=discord.Game('$commands'))
	try:
		synced = await bot.tree.sync()
		print(f'Synced {len(synced)} command(s)')
	except Exception as e:
		print(e)
	channel = bot.get_channel(CHANNEL_ID)
	await channel.send('Thank you for waking me up!')

@bot.event
async def on_command_error(ctx, error):
	await ctx.send(f'Oops! An error occured: {str(error)}')

@bot.command()
async def hello(ctx):
	await ctx.send('Hello, I am JAUB, or Just Another Useful Bot!')

@bot.command()
async def randomnumber(ctx, x, y):
	await ctx.send(str(genNumber(int(x), int(y))))

@bot.command()
async def flipcoin(ctx):
	side = ["It's heads!", "It's tails!"]
	result = random.choice(side)
	await ctx.send(result)

@bot.command()
async def commands(ctx):
	await ctx.send('''Here are some useful commands:
$hello - A simple greeting.
$randomnumber - Generates a random number given a specified range.
$flipcoin - Flips a coin, and provides the random result.
$commands - Provides a list of useful commands.''')

@bot.tree.command(name='hello', description='A simple greeting.')
async def hello(interaction: discord.Interaction):
	await interaction.response.send_message(f'Hey {interaction.user.mention}!')

@bot.tree.command(name='help', description='Gives information about JAUB.')
async def help(interaction: discord.Interaction):
	await interaction.response.send_message('''Help [JAUB]:
/hello - A simple greeting.
/help - Provides information about JAUB.
$hello - Another simple greeting.
$randomnumber [x] [y] - Generates a random number given a specified range.
$flipcoin - Flips a coin, and provides the random result.
$commands - A simpler approach to the help menu (does not include / commands).''')

bot.run(BOT_TOKEN)