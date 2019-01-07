import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import os
from discord import Game
import time

Client  = discord.client
client = commands.Bot(command_prefix = ".")
client = discord.Client()

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

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

@client.event
async def on_message(message):
    if message.content.upper().startswith('.PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))

    if message.content.startswith("INVITEME"):
        userID = message.author.id
        msg = "https://discordapp.com/api/oauth2/authorize?client_id=529463184910712872&permissions=0&scope=bot {0.author.mention}".format((message))
        await client.send_message(message.channel, msg)

@client.event
async def on_message(message):
    if message.content.upper().startswith('.ADMINME'):
        userID = message.author.id
        await client.send_message(message.channel, ":x: You do not have the permission to do that <@%s>" % (userID))
    if message.content.upper().startswith('.LOGIN'):
        if message.author.id == "341933833136111617": #Replace <User ID> with the ID of the user you want to be able to execute this command!
            args = message.content.split(" ")
            await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
        else:
            await client.send_message(message.channel, "You do not have permission to log into this service!")
    if message.content.upper().startswith('.AMIADMIN'):
        if "<Role ID>" in [role.id for role in message.author.roles]: #Replace <Role ID> with the ID of the role you want to be able to execute this command
            await client.send_message(message.channel, "You are an administrator!")
        else:
            await client.send_message(message.channel, "You are not an administrator! Please ensure that i have the full permissions and above all of the higher ranks.")

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="102 servers | 456,769 users",
url="https://twitch.tv/celabrat", type=1))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(os.environ['BOT_TOKEN'])
