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
	if message.content.startswith('.hello'):
		await bot.send_message(message.channel, "Hello {0.author.mention}".format(message))
	
	if message.content.startswith('.welcome'):
		await bot.send_message(message.channel, 'Thanks for having me in your server {0.author.mention}!'.format(message))
	
	if message.content.startswith('.ping'):
		await bot.send_message(message.channel, "{0.author.mention} Pong!".format(message))
	
	if message.content.startswith("inviteme"):
		msg = "https://discordapp.com/api/oauth2/authorize?client_id=529463184910712872&permissions=0&scope=bot {0.author.mention}".format(message)
		await bot.send_message(message.channel, msg)
	
	if message.content.startswith('.adminme'):
		await bot.send_message(message.channel, ":x: You do not have the permission to do that <@%s>".format(message)
	await bot.process_commands(message)

@bot.command()
async def test():
	await bot.say("test {}".format(ctx.message.author.mention))
	
@bot.command(pass_context=True, no_pm=True)
async def help(ctx):
	embed = discord.Embed(title="Help section", description=" ", color=0xFFFF)
	embed.add_field(name=".hello", value="make the bot say hello to you")
	embed.add_field(name=".welcome", value="welcome message")
	embed.add_field(name=".ping", value="make the bot ping you")
	embed.add_field(name="inviteme", value="to get bot invite link")
	await bot.say(embed=embed)
		      
bot.run(os.environ['BOT_TOKEN'])
