import discord
from discord.ext import commands
import asyncio
import time
import os

bot = commands.Bot(command_prefix = ".")
bot.remove_command('help')

@bot.event
async def on_ready():
	await bot.change_presence(game=discord.Game(name="163 servers | 591,925 users",
url="https://twitch.tv/celabrat", type=1))
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')

@bot.event
async def on_message(message):
	if message.content.startswith('hello'):
		msg = 'Hello {0.author.mention}'.format(message)
		await bot.send_message(message.channel, msg)
	if message.content.startswith('.welcome'):
		msg = 'Thanks for having me in your server {0.author.mention}!'.format(message)
		await bot.send_message(message.channel, msg)
	if message.content.startswith('.ping'):
		userID = message.author.id
		await bot.send_message(message.channel, "<@%s> Pong!" % (userID))
	if message.content.startswith("inviteme"):
		userID = message.author.id
		msg = "https://discordapp.com/api/oauth2/authorize?client_id=529463184910712872&permissions=0&scope=bot {0.author.mention}".format((message))
		await bot.send_message(message.channel, msg)
	if message.content.startswith('.adminme'):
		userID = message.author.id
		await bot.send_message(message.channel, ":x: You do not have the permission to do that <@%s>" % (userID))
		await bot.process_commands(message)

@bot.command()
async def pings():
	await bot.say("test {}".format(ctx.message.author.mention)
		      
bot.run(os.environ['BOT_TOKEN'])
