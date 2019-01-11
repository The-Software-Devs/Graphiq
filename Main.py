import discord
from discord.ext import commands
import asyncio
import time
import inspect
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
	
	if message.content.startswith(".inviteme"):
		msg = "https://discordapp.com/api/oauth2/authorize?client_id=529463184910712872&permissions=0&scope=bot {0.author.mention}".format(message)
		await bot.send_message(message.channel, msg)
	
	if message.content.startswith('.bothelp'):
		await bot.send_message(message.channel, "Need help? Join our server for more info. Our friendly staff will always help you. https://discord.gg/a5X8v7D".format(message))
	await bot.process_commands(message)

@bot.command(pass_context=True)
async def test(ctx):
	await bot.say("test {}".format(ctx.message.author.mention))
	
def user_is_me(ctx):
	return ctx.message.author.id == "277983178914922497", "341933833136111617"
	
@bot.command(pass_context=True, no_pm=True)
async def help(ctx):
	embed = discord.Embed(title="Help section", description="Help Is Here! ", color=0xFFFF)
	embed.add_field(name=".hello", value="Make the bot say hello to you.")
	embed.add_field(name=".welcome", value="Welcome message.")
	embed.add_field(name=".ping", value="Make the bot ping you.")
	embed.add_field(name=".inviteme", value="To get bot invite link.")
	embed.add_field(name=".bug", value="Only use this command if the bot is acting weird on specific command.")
	embed.add_field(name=".idea", value="Send your idea about new commands the bot don't have.")
	embed.add_field(name=".bothelp", value="Bot help within server.")
	embed.set_footer(text="Requested by: " + author.name)
	await bot.say(embed=embed)
	channel = bot.get_channel('532949494036168706')
	embed = discord.Embed(title=f"User: {ctx.message.author.name} have used help command", description=f"ID: {ctx.message.author.id}", color=0xff9393)
	await bot.send_message(channel, embed=embed)

	
@bot.command(pass_context=True)
async def bug(ctx, *, reportmsg: str):
    channel = bot.get_channel('532949494036168706')
    msg = embed = discord.Embed(title=f"User: {ctx.message.author.name}", description=f"Bug reports: {reportmsg}", color=0xFFFF)
    await bot.send_message(channel, embed=embed)
    text = embed = discord.Embed(title="Your bot bug reports has been submitted", description=f"{ctx.message.author.name}'s message: {reportmsg} ", color=0xFFFF)
    await bot.delete_message(ctx.message)
    await bot.say(embed=embed)
    
@bot.command(pass_context=True)
async def idea(ctx, *, reportmsg: str):
    channel = bot.get_channel('532949494036168706')
    msg = embed = discord.Embed(title=f"User: {ctx.message.author.name}", description=f"Idea: {reportmsg}", color=0xFFFF)
    await bot.send_message(channel, embed=embed)
    embed = discord.Embed(title="Your idea has been submitted", description=f"{ctx.message.author.name}'s message: {reportmsg} ", color=0xFFFF)
    await bot.delete_message(ctx.message)
    await bot.say(embed=embed)
	
@bot.command(name='eval', pass_context=True)
@commands.check(user_is_me)
async def _eval(ctx, *, command):
    res = eval(command)
    if inspect.isawaitable(res):
        await bot.say(await res)
    else:
    	await bot.say(res)
		      
bot.run(os.environ['BOT_TOKEN'])
