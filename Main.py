import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import os
from discord import Game
import time

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
		await bot.send_message(message.channel, ":x: You do not have the permission to do that <@%s>" % (userI
	await bot.process_commands(message)

@bot.command(pass_context=True)
async def help(ctx):
		server = ctx.message.server
		author = ctx.message.author
		embed = discord.Embed(title="Help is here!", description=" ", color=0xFFFF)
		embed.add_field(name="inviteme", value="gives you bot invite link")
		embed.add_field(name=".ping", value="the bot ping you")
		embed.add_field(name="hello", value="the bot will say hello to you")
		embed.set_thumbnail(url=server.icon_url)
		embed.set_footer(text="Requested by: " + author.name)
		await bot.say(embed=embed)
    
bot.run(os.environ['BOT_TOKEN'])
