from dotenv import load_dotenv
import discord
from discord import app_commands
from discord.ext import commands
import random
import time
import os

load_dotenv()

BOT_TOKEN = os.environ.get('token') #Create a .env for storing ideally
CHANNEL_ID = #ChannelID Here

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
async def rps(ctx, user_choice):
	moves = ['rock', 'paper', 'scissors']
	bot_choice = random.choice(moves)
	if user_choice not in moves:
		await ctx.send('Please choose a valid move!')
	else:
		await ctx.send(f'You chose {user_choice}')
		await ctx.send(f'I chose {bot_choice}')
		if user_choice == bot_choice:
			await ctx.send(f"We both chose {user_choice}, it's a tie!")
		elif user_choice == 'rock':
			if bot_choice == 'scissors':
				await ctx.send('Rock smashes scissors! You win!')
			else:
				await ctx.send('Paper covers rock! You lose.')
		elif user_choice == 'paper':
			if bot_choice == 'rock':
				await ctx.send('Paper covers rock! You win!')
			else:
				await ctx.send('Scissors cuts paper! You lose.')
		elif user_choice == 'scissors':
			if bot_choice == 'paper':
				await ctx.send('Scissors cuts paper! You win!')
			else:
				await ctx.send('Rock smashes scissors! You lose.')

@bot.command()
async def commands(ctx):
	await ctx.send('''Here are some useful commands:
$hello - A simple greeting.
$randomnumber - Generates a random number given a specified range.
$flipcoin - Flips a coin, and provides the random result.
$rps [choice] - Play rock paper scissors with JAUB.
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
$rps [choice] - Play rock paper scissors with JAUB.
$commands - A simpler approach to the help menu (does not include / commands).''')

bot.run(BOT_TOKEN)
