import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import os
from discord import Game
import time

client = discord.Client()
client = commands.Bot(command_prefix = ".")
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="163 servers | 591,925 users",
url="https://twitch.tv/celabrat", type=1))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message_edit(before, after):
    fmt = '**{0.author}** edited their message: :arrow_up: \n{1.content}'
    await client.send_message(after.channel, fmt.format(after, before))

@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('.welcome'):
        msg = 'Thanks for having me in your server {0.author.mention}!'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('.ping'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))

    if message.content.startswith("inviteme"):
        userID = message.author.id
        msg = "https://discordapp.com/api/oauth2/authorize?client_id=529463184910712872&permissions=0&scope=bot {0.author.mention}".format((message))
        await client.send_message(message.channel, msg)

    if message.content.startswith('.adminme'):
        userID = message.author.id
        await client.send_message(message.channel, ":x: You do not have the permission to do that <@%s>" % (userID))
    
    if message.content.startswith('.login'):
        if message.author.id == "341933833136111617": #Replace <User ID> with the ID of the user you want to be able to execute this command!
            args = message.content.split(" ")
            await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
        else:
            await client.send_message(message.channel, "You do not have permission to log into this service!")
    
    if message.content.startswith('.amiadmin'):
        if "<Role ID>" in [role.id for role in message.author.roles]: #Replace <Role ID> with the ID of the role you want to be able to execute this command
            await client.send_message(message.channel, "You are an administrator!")
        else:
            await client.send_message(message.channel, "You are not an administrator!")
	

@bot.command(pass_context=True, no_pm=True)
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
    
client.run(os.environ['BOT_TOKEN'])
