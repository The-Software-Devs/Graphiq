import discord
from discord.ext import commands
import asyncio
import time
from discord import game
import inspect
import os
import random
import json
import datetime
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import urllib
import urllib.request
import requests as rq

from discord.utils import get

bot = commands.Bot(command_prefix = "b.")
bot.remove_command('help')

evn=bot.event
cms=bot.command(pass_context=True)

async def picker():
    mem_watching=['{} members']
    mem_watching=['graphiqdiscord.gitbook.io']
    mem_listening=['{} members']
    mem_playing=['Need upvotes to grow!']

    ser_watch=['{} servers']
    ser_listen=['b.help | v1.7']
    ser_play=['b.help | v1.7']
    helps=['!help | for help','!help for help commands']

    while True:
        kind=random.randint(1,2)
        if kind == 1:
            members=0
            for i in bot.servers:
                members+=len(i.members)
            num = random.choice([1, 2, 3])
            if num == 1:
                await bot.change_presence(game=discord.Game(name=random.choice(mem_playing).format(members), type=1))
            if num == 2:
                await bot.change_presence(game=discord.Game(name=random.choice(mem_listening).format(members), type=2))
            if num == 3:
                await bot.change_presence(game=discord.Game(name=random.choice(mem_watching).format(members), type=3))
            await asyncio.sleep(random.choice([10, 10, 10, 10, 10, 10]))
        
        
        if kind == 2:
            num = random.choice([1, 2, 3])
            if num == 1:
                await bot.change_presence(game=discord.Game(name=random.choice(ser_play).format(len(bot.servers)), type=1))
            if num == 2:
                await bot.change_presence(game=discord.Game(name=random.choice(ser_listen).format(len(bot.servers)), type=2))
            if num == 3:
                await bot.change_presence(game=discord.Game(name=random.choice(ser_watch).format(len(bot.servers)), type=3))
            await asyncio.sleep(random.choice([10, 10, 10, 10, 10, 10]))

        if kind == 3:
            await bot.change_presence(game=discord.Game(name=random.choice(ser_watch).format(len(bot.servers)), type=3))
            await asyncio.sleep(random.choice([10, 10, 10, 10, 10, 10]))

@bot.event
async def on_ready():
    bot.loop.create_task(picker())
    print("Change status for {} is ready!".format(bot.user.name))
	
@bot.command(pass_context=True)
async def check(ctx, user: discord.Member):
      """CHECKS ANOTHER USER'S CREDITS. Ex: s.check @kurusaki"""
      try:

          tax = 50
          checker = ctx.message.author.id  # pserson who is checking someone's credits
          target_id = user.id  # the person that is getting his/her credits checked
          target_name = user.name  # target's name
          target_row = wks.find(target_id).row  # target's row
          checker_row = wks.find(checker).row  # checker's row
          target_credits = wks.cell(target_row, 3).value  # target's value
          checker_credits = wks.cell(checker_row, 3).value
          checker_float = float(checker_credits)  # checker's credits in float
          target_float = float(target_credits)  # target's credits in float
          update_checker = wks.update_cell(
              checker_row, 3, checker_float-tax)  # taxing the checker
          msg = await bot.say("{} The user {} has a total of {} credits.\n{} credits have been removed from you as tax.".format(ctx.message.author.mention, target_name, target_credits, tax))

          #reacting to high credits
          if target_float > 1200:
              await bot.add_reaction(msg, emoji='💲')
          if target_float > 2300:
              await bot.add_reaction(msg, emoji='💸')
          if target_float > 3400:
              await bot.add_reaction(msg, emoji='🤑')
          if target_float > 4200:
              await bot.add_reaction(msg, emoji='💵')
          if target_float > 5300:
             await bot.add_reaction(msg, emoji='💰')
          try:
              # updating the user's  tax
               checker_tax_value = wks.cell(
                  checker_row, 7).value  # current tax value
              tax_float = float(checker_tax_value)  # tax value into float
              # updating the new tax value
              updating_tax = wks.update_cell(checker_row, 7, tax_float+tax)
          except:
              new_tax = wks.update_cell(checker_row, 7, tax)
              print("User had no current tax value, so it was added")

      except gspread.exceptions.CellNotFound:  # if user has no database in gspread
          tax = 35
          checker = ctx.message.author.id  # checker id
          checker_row = wks.find(checker).row  # checker's row
          # checker's credits value
          checker_credits = wks.cell(checker_row, 3).value
          checker_float = float(checker_credits)  # checker credits float
          await bot.say("User {} is not in database".format(target_name))
          await bot.say("Attempting to adding user to database")
          # adding value to no existing user
          adding_user = wks.append_row([target_name, target_id, 55.00])
          update_checker = wks.update_cell(
              checker_row, 3, checker_float-tax)  # taxing user
          await bot.say("{} now has 55.00 credits".format(target_name))
          await bot.say("{} credits has been removed from your account as tax.".format(tax))

          try:  # updating the user's tax
              checker_tax_value = wks.cell(
                  checker_row, 7).value  # checker's tax value
              if checker_tax_value == "":
                  new_tax = wks.update_cell(checker_row, 7, tax)
              else:  # ADD A NEW TAX VALUE IF IT IS BLANK
                  tax_float = float(checker_tax_value)
                  updating_tax = wks.update_cell(checker_row, 7, tax_float+tax)
          except:
              print("Unable to add the user{} to tax database ".format(
                  ctx.message.name))

	
@bot.command(pass_context=True)
async def userinfo(ctx, member: discord.Member = None):
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=member.colour, timestamp=ctx.message.timestamp)
    embed.set_author(name=member)
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Guild name:", value=member.display_name)
    embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
    embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
    embed.add_field(name="Top role:", value=member.top_role.mention)
    await bot.send_message(ctx.message.channel,embed=embed)

@bot.command(pass_context=True)
async def afks(con):
    amt=0
    for i in con.message.server.members:
        if i.is_afk == True:
            amt+=1
    await bot.send_message(con.message.channel,"**Currently `{}` AFK Members In `{}`**".format(amt,con.message.server.name))
 
@bot.command(pass_context=True)
async def weather(ctx):
    """GET THE WEATHER IN YOUR CITY. EX: s.weather austin"""
    city_state = ctx.message.content[10:]
    t = u"\u00b0"
    try:
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'.format(
            city_state, owm)
        ser = rq.get(url).text
        rq_json = json.loads(ser)
        temp = rq_json['main']['temp']
        max_temp = rq_json['main']['temp_max']
        min_temp = rq_json['main']['temp_min']
        dis = rq_json['weather'][0]['description']
        wind = rq_json['wind']['speed']
        await bot.say("**Temperature** **in** **{}** **is around** {}{}F\n**Minimum Temperature is**: {}{}F\n**Maximum Temperature is**: {}{}F\n**Mainly**: {}\n**Wind speed is around**: {} **MPH**".format(city_state, temp, t, min_temp, t, max_temp, t, dis, wind))
    except:
        await bot.say("Looks like something went wrong. Your spelling may be incorrect or the bot may just be able to process this command at the moment.")

@bot.command(pass_context=True)
async def ping( con):
    channel = con.message.channel
    t1 = time.perf_counter()
    await bot.send_typing(channel)
    t2 = time.perf_counter()
    embed = discord.Embed(title=None, description='<a:pingpong:552394473230041098> Pong! Your ping is: {}ms'.format(
        round((t2-t1)*1000)), color=0x2874A6)
    await bot.say(embed=embed)
 

@bot.command(pass_context=True)
async def on(con):
    emoji=discord.utils.get(bot.get_all_emojis(), name='United Kingdom | LondonDonaldJT')
    emb=discord.Embed(title='Emoji',description='This is an emoji {}'.format(emoji))
    await bot.say(embed=emb)
	
@bot.command(pass_context=True)
async def urban( con, *, msg):
    session = rq.Session()
    """USES URBAN DICT TO FIND DEFINITION OF WORDS. EX: s.urban neko"""
    link = 'http://api.urbandictionary.com/v0/define?term={}'.format(msg)
    rq_link = session.get(link).text
    rq_json = json.loads(rq_link)
    if rq_json['list'] == []:
        await bot.send_message(con.message.channel, "**No Results Found**")
    elif rq_json['list'] != []:
        await bot.send_message(con.message.channel, "**Word**: {}\n**Votes**: {}\n**Definitioin**: {}\n**Example**: {}".format(rq_json['list'][0]['word'], rq_json['list'][0]['thumbs_up'], rq_json['list'][0]['definition'], rq_json['list'][0]['example']))

@bot.event
async def on_command_error(error, ctx):
	if isinstance(error, commands.CommandNotFound):
		img = Image.open("error.png") #Replace infoimgimg.png with your background image.
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype("Modern_Sans_Light.otf", 80) #Make sure you insert a valid font from your folder.
		fontbig = ImageFont.truetype("Fitamint Script.ttf", 400) #Make sure you insert a valid font from your folder.
		#    (x,y)::↓ ↓ ↓ (text)::↓ ↓     (r,g,b)::↓ ↓ ↓
		draw.text((10, 10), "Looks like there was an error with the", (255, 255, 255), font=font)
		draw.text((10, 70), "command you given!", (255, 255, 255), font=font)
		draw.text((10, 140), "Are you sure this command exists?", (255, 255, 255), font=font)
		draw.text((10, 210), "See if the commands exists b.help.", (255, 255, 255), font=font)
		draw.text((10, 1100), "Graphiq. 2019", (255, 255, 255), font=font)
		img.save('error.png') #Change infoimg2.png if needed.
		await bot.send_file(ctx.message.channel,"error.png")
	
def user_is_me(ctx):
    return ctx.message.author.id == "341933833136111617"
	
@bot.command()
@commands.check(user_is_me)
async def logout():
    m1=await bot.say("<a:warning:552881993445015553> This can get you a ban from using the bot and very dangerous. This can shut down the bot!")
    time.sleep(6)
    await bot.edit_message(m1,new_content='<a:warning:552881993445015553>  You have disregarded the warning and the bot will be shutting down in...')
    time.sleep(5)
    await bot.edit_message(m1,new_content='<a:Graphiqloading:551796596350910475> 3')
    time.sleep(5)
    await bot.edit_message(m1,new_content='<a:Graphiqloading:551796596350910475> 2')
    time.sleep(5)
    await bot.edit_message(m1,new_content='<a:Graphiqloading:551796596350910475> 1')
    time.sleep(5)
    await bot.edit_message(m1,new_content='<a:checkmark:552893708387876884> Bot shutdown! <a:warning:552881993445015553>')
    await bot.logout()

@bot.command()
async def square(number):
    squared_value = int(number) * int(number)
    await bot.say(str(number) + " squared is " + str(squared_value))
	
	
@bot.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)

async def eightball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely'
	'Yes',
	'No',
    ]
    await bot.say(random.choice(possible_responses) + ", " + context.message.author.mention)
	
def user_is_me(ctx):
    return ctx.message.author.id == "341933833136111617"
	
@bot.command()
@commands.check(user_is_me)
async def servers():
  servers = list(bot.servers)
  await bot.say("Connected on " + str(len(bot.servers)) + " servers:")
  await bot.say('\n'.join(server.name for server in servers))
  await bot.say('\n'.join(server.id for server in servers))
	
@bot.command(pass_context=True,aliases=["Roles","ROLES","Role"])
async def userroles(ctx, member: discord.Member = None):
    roles = [role for role in member.roles]
    embed=discord.Embed(title="Users Roles",description="{}'s Roles are:".format(member.name))
    embed.add_field(name=f"({len(roles)})", value=" ".join([role.mention for role in roles]))
    await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def hug(ctx, *, member: discord.Member = None):
  #  Hug someone on the server <3
    try:
        if member is None:
            await bot.say(ctx.message.author.mention + " has been hugged!")
        else:
            if member.id == ctx.message.author.id:
                await bot.say(ctx.message.author.mention + " hugged his self! LOL")
            else:
                embed=discord.Embed(description=member.mention + " has been hugged by " + ctx.message.author.mention + "!")
                embed.set_image(url="https://media1.tenor.com/images/d7529f6003b20f3b21f1c992dffb8617/tenor.gif")
                await bot.say(embed=embed)
    except:
        pass

@bot.command(pass_context=True)
async def thanks(ctx, *, member: discord.Member = None):
  #  Hug someone on the server <3
    try:
        if member is None:
            await bot.say(ctx.message.author.mention + " has been thanked!")
        else:
            if member.id == ctx.message.author.id:
                await bot.say(ctx.message.author.mention + " thanked his self! LOL")
            else:
                embed=discord.Embed(description=member.mention + " has been thanked by " + ctx.message.author.mention + "!")
                embed.set_image(url="https://media1.tenor.com/images/cc619912fe89d1ff0d496b9d8fae70a4/tenor.gif")
                await bot.say(embed=embed)
    except:
        pass
	
@bot.command(pass_context=True)
async def yourwelcome(ctx, *, member: discord.Member = None):
  #  Hug someone on the server <3
    try:
        if member is None:
            await bot.say(ctx.message.author.mention + " has been welcomed!")
        else:
            if member.id == ctx.message.author.id:
                await bot.say(ctx.message.author.mention + " welcomed his self! LOL")
            else:
                embed=discord.Embed(description=member.mention + " has been ``your welcomed`` by " + ctx.message.author.mention + "!")
                embed.set_image(url="https://media1.tenor.com/images/15bafc0b414757acab81650a6ff21963/tenor.gif")
                await bot.say(embed=embed)
    except:
        pass
	
	
@bot.command(pass_context=True)
async def wow(ctx, *, member: discord.Member = None):
  #  Hug someone on the server <3
    try:
        if member is None:
            await bot.say(ctx.message.author.mention + " has been wowed!")
        else:
            if member.id == ctx.message.author.id:
                await bot.say(ctx.message.author.mention + " wowed his self! LOL")
            else:
                embed=discord.Embed(description=member.mention + " has been wowed by " + ctx.message.author.mention + "!")
                embed.set_image(url="https://media1.tenor.com/images/e99fe0258fde8ba4cf5956018f839c83/tenor.gif")
                await bot.say(embed=embed)
    except:
        pass
	
@bot.command(pass_context=True)
async def please(ctx, *, member: discord.Member = None):
  #  Hug someone on the server <3
    try:
        if member is None:
            await bot.say(ctx.message.author.mention + " has begged!")
        else:
            if member.id == ctx.message.author.id:
                await bot.say(ctx.message.author.mention + " begged his self! LOL")
            else:
                embed=discord.Embed(description=member.mention + " has begged and begged from  " + ctx.message.author.mention + "!")
                embed.set_image(url="https://media1.tenor.com/images/09556e93c9967bc494c022e13c551dc8/tenor.gif")
                await bot.say(embed=embed)
    except:
        pass
	
	
@bot.command(pass_context=True)
async def yesbro(ctx, *, member: discord.Member = None):
  #  Hug someone on the server <3
    try:
        if member is None:
            await bot.say(ctx.message.author.mention + " has became a ganster!")
        else:
            if member.id == ctx.message.author.id:
                await bot.say(ctx.message.author.mention + " got beat up by his own gang. LOL")
            else:
                embed=discord.Embed(description=member.mention + " has ganged up on " + ctx.message.author.mention + "!")
                embed.set_image(url="https://media1.tenor.com/images/3e20a7e3f4e1b29f2c638756fadfc2fa/tenor.gif")
                await bot.say(embed=embed)
    except:
        pass
	
	
@bot.command(pass_context=True)
async def fortnite(ctx, *, member: discord.Member = None):
  #  Hug someone on the server <3
    try:
        if member is None:
            await bot.say(ctx.message.author.mention + " has lost a victory royale!")
        else:
            if member.id == ctx.message.author.id:
                await bot.say(ctx.message.author.mention + " killed him/herself.")
            else:
                embed=discord.Embed(description=member.mention + " has lost a Victory Royale by " + ctx.message.author.mention + "!")
                embed.set_image(url="https://media1.tenor.com/images/9bb8f1a9272c2d29f77f442b90a5b111/tenor.gif")
                await bot.say(embed=embed)
    except:
        pass	
	
@bot.command(pass_context=True) #pass the context of user
@commands.has_permissions(manage_roles=True) #mkes it so that only people with this permission can use this command
async def addRole(con,user:discord.Member,*roles:discord.Role):
    roleNames=[] # the list to store the role obj
    addedRoles=[]
    errorRole=[]
    for i in roles: #for something in the roles parameter
        roleNames.append(i) #add the obj into roleNames
    for i in con.message.server.roles: #check to see if the ids of the roles are == to the ids of the server roles
        for x in roleNames:
            if i.name == x.name: #if match add the role
                try:
                    await bot.add_roles(user,i)
                    addedRoles.append("**{}**".format(i.name))
                except:
                    errorRole.append(i.name)


    #making the output message pretty, this can be added into embed to make look better if you want
    addedRoles=str(addedRoles)
    addedRoles=addedRoles.replace('[','')
    addedRoles=addedRoles.replace(']','')
    await bot.say("Roles {} added to {}".format(addedRoles,user.name))
	
	
@bot.command(pass_context=True)
async def kill(ctx, *, member: discord.Member = None):
  #  Hug someone on the server <3
    try:
        if member is None:
            await bot.say(ctx.message.author.mention + " has been killed!")
        else:
            if member.id == ctx.message.author.id:
                await bot.say(ctx.message.author.mention + " killed im/her self! R.I.P")
            else:
                embed=discord.Embed(description=member.mention + " has been killed by " + ctx.message.author.mention + "!")
                embed.set_image(url="https://media1.tenor.com/images/62e86b68157aa404cb69b13d1ec297a2/tenor.gif")
                await bot.say(embed=embed)
    except:
        pass
	
	
@bot.command(pass_context=True, no_pm=True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(description="<:cog:553328079272017932> Help Section <:cog:553328079272017932>", color=0xFFFF)
    embed.add_field(name="b.help_moderation ", value="Lists moderation commands. ||",inline=True)
    embed.add_field(name="b.help_fun", value="Lists fun commands. ||",inline=True)
    embed.add_field(name="b.help_admin", value="Lists Administrator commands.",inline=True)
    embed.add_field(name="b.help_credits", value="Lists all the help from Developers to staff.",inline=True)
    embed.set_footer(text="Requested by: " + author.name)
    await bot.send_message(author, embed=embed)
    embed = discord.Embed(description=" ", color=0xFFFF)
    m=await bot.say("<a:Graphiqloading:551796596350910475>")
    await asyncio.sleep(2)
    await bot.delete_message(m)
    em=discord.Embed()
    em.add_field(name="<a:checkmark:552893708387876884> Success!", value="I've sent you a list of my commands in your **Direct Messages**",inline=True)
    await bot.say(embed=em)
    channel = bot.get_channel('543488075809030145')
    embed = discord.Embed(title=f"User: {ctx.message.author.name} have used help command", description=f"User ID: {ctx.message.author.id}", color=0xff9393)
    await bot.send_message(channel, embed=embed)
	
@bot.command(pass_context=True, no_pm=True)
async def help_moderation(ctx):
    author = ctx.message.author
    embed = discord.Embed(description="<:moderation:553328786083414051> Moderation Help Section <:moderation:553328786083414051> ", color=0xFFFF)
    embed.add_field(name="b.report", value="Reports user/command",inline=True)
    embed.add_field(name="b.mute", value="Mutes a user",inline=True)
    embed.add_field(name="b.kick", value="Kicks a user from the server.",inline=True)
    embed.add_field(name="b.ban", value="Bans a user from the server.",inline=True)
    embed.add_field(name="b.help_setup", value="Set-up bot.",inline=True)
    embed.set_footer(text="Requested by: " + author.name)
    await bot.send_message(author, embed=embed)
    embed = discord.Embed(description=" ", color=0xFFFF)
    m=await bot.say("<a:Graphiqloading:551796596350910475>")
    await asyncio.sleep(2)
    await bot.delete_message(m)
    em=discord.Embed()
    embed.add_field(name="<a:checkmark:552893708387876884> Success!", value="I've sent you a list of my ``Moderation`` commands in your **Direct Messages**",inline=True)
    await bot.say(embed=embed)
    channel = bot.get_channel('543488075809030145')
    embed = discord.Embed(title=f"User: {ctx.message.author.name} have used **Moderation** help command", description=f"User ID: {ctx.message.author.id}", color=0xff9393)
    await bot.send_message(channel, embed=embed)
	
@bot.command(pass_context=True, no_pm=True)
async def help_admin(ctx):
    author = ctx.message.author
    embed = discord.Embed(description="<:admin:553329175549837352> Admin Help Section <:admin:553329175549837352>", color=0xFFFF)
    embed.add_field(name="b.report", value="Report user/commmand.",inline=True)
    embed.add_field(name="b.bans", value="Lists banned users in server.",inline=True)
    embed.add_field(name="b.clean", value="Cleans a message less than 98.",inline=True)
    embed.set_footer(text="Requested by: " + author.name)
    await bot.send_message(author, embed=embed)
    embed = discord.Embed(description=" ", color=0xFFFF)
    m=await bot.say("<a:Graphiqloading:551796596350910475>")
    await asyncio.sleep(2)
    await bot.delete_message(m)
    em=discord.Embed()
    embed.add_field(name="<a:checkmark:552893708387876884>", value="I've sent you a list of my ``Moderation`` commands in your **Direct Messages**",inline=True)
    await bot.say(embed=embed)
    channel = bot.get_channel('543488075809030145')
    embed = discord.Embed(title=f"User: {ctx.message.author.name} have used **admin** help command", description=f"User ID: {ctx.message.author.id}", color=0xff9393)
    await bot.send_message(channel, embed=embed)


@bot.command(pass_context=True, no_pm=True)
async def help_credits(ctx):
    author = ctx.message.author
    embed = discord.Embed(description="<:credits:553329710508146688> Credits to Developers and Staff :<:credits:553329710508146688>", color=0xFFFF)
    embed.add_field(name="Mxchael#7748", value="Bot Founder.",inline=True)
    embed.add_field(name="noobperson#2436", value="Bot Owner and Developer.",inline=True)
    embed.add_field(name="Ryan_Stanford#5219", value="Trainee Founder.",inline=True)
    embed.add_field(name="DankCoder | 程序员#9983", value="Trainee Founder.",inline=True)
    embed.add_field(name="Ƭunyo-Ƭєx#2015", value="Chairman and Developer.",inline=True)
    embed.add_field(name="lolbitr43#8135", value="Chairman.",inline=True)
    embed.add_field(name="JayHaggs#5655", value="Vice Chairman.",inline=True)
    embed.add_field(name="``Thank you to all of the staff for heping me on this bot.``", value=" - Mxchael#7748, Founder.",inline=True)
    embed.set_footer(text="Requested by: " + author.name)
    await bot.send_message(author, embed=embed)
    embed = discord.Embed(description=" ", color=0xFFFF)
    m=await bot.say("<a:Graphiqloading:551796596350910475>")
    await asyncio.sleep(2)
    await bot.delete_message(m)
    em=discord.Embed()
    embed.add_field(name="<a:checkmark:552893708387876884>", value="I've sent you a list of my ``Credits`` list in your **Direct Messages**",inline=True)
    await bot.say(embed=embed)
    channel = bot.get_channel('543488075809030145')
    embed = discord.Embed(title=f"User: {ctx.message.author.name} have used **credits** help command", description=f"User ID: {ctx.message.author.id}", color=0xff9393)
    await bot.send_message(channel, embed=embed)

@bot.command(pass_context=True, no_pm=True)
async def help_fun(ctx):
    author = ctx.message.author
    embed = discord.Embed(description="<:fun:553330200193007626> Fun Help Section <:fun:553330200193007626> ", color=0xFFFF)
    embed.add_field(name="b.hello", value="Says hello to you.",inline=True)
    embed.add_field(name="b.hug", value="Hugs a user.",inline=True)
    embed.add_field(name="b.kill", value="Kills a user.",inline=True)
    embed.add_field(name="b.please", value="Begs a user.",inline=True)
    embed.add_field(name="b.fortnite", value="Loose a Victory Royale.",inline=True)
    embed.add_field(name="b.thanks", value="Says thanks to a user.",inline=True)
    embed.add_field(name="b.yourwelcome", value="Says Your Welcome to a user.",inline=True)
    embed.add_field(name="b.eightball", value="User asks question and bot replies.",inline=True)
    embed.add_field(name="b.square", value="Square a number [Maths].",inline=True)
    embed.add_field(name="``More commands being added soon!``", value="**Remember**, the bot is still in development.",inline=True)
    embed.set_footer(text="Requested by: " + author.name)
    await bot.send_message(author, embed=embed)
    embed = discord.Embed(description=" ", color=0xFFFF)
    m=await bot.say("<a:Graphiqloading:551796596350910475>")
    await asyncio.sleep(2)
    await bot.delete_message(m)
    em=discord.Embed()
    embed.add_field(name="<a:checkmark:552893708387876884> Success!", value="I've sent you a list of my ``Fun`` commands in your **Direct Messages**",inline=True)
    await bot.say(embed=embed)
    channel = bot.get_channel('543488075809030145')
    embed = discord.Embed(title=f"User: {ctx.message.author.name} have used **Fun** help command", description=f"User ID: {ctx.message.author.id}", color=0xff9393)
    await bot.send_message(channel, embed=embed)
	
	
@bot.command(pass_context=True, no_pm=True)
async def help_setup(ctx):
    author = ctx.message.author
    embed = discord.Embed(description="<:setup:553330560160890890> Setup Bot's Permissions <:setup:553330560160890890>", color=0xFFFF)
    embed.add_field(name="- Add a rank for the bot", value="Make sure it has all of the permissions.",inline=True)
    embed.add_field(name="- New role called ``Verified``", value="Verify the user.",inline=True)
    embed.add_field(name="- Make sure it is above all of the user ranks.", value="To make sure if a admin is abusing the higher rank can kick.",inline=True)
    embed.add_field(name="- Make sure you join the **Support Server** for more info.", value="Command = .stats --> Support Server --> Link.",inline=True)
    embed.add_field(name="``Thank you for your contibrution.``", value="**Remember**, Put ``.setup_done`` for the verification.",inline=True)
    embed.set_footer(text="Requested by: " + author.name)
    await bot.send_message(author, embed=embed)
    embed = discord.Embed(description=" ", color=0xFFFF)
    m=await bot.say("<a:Graphiqloading:551796596350910475>")
    await asyncio.sleep(2)
    await bot.delete_message(m)
    em=discord.Embed()
    embed.add_field(name="<a:checkmark:552893708387876884> Success!", value="I've sent you a list of my ``Setup`` instructions in your **Direct Messages**",inline=True)
    await bot.say(embed=embed)
    channel = bot.get_channel('543488075809030145')
    embed = discord.Embed(title=f"User: {ctx.message.author.name} have used **Fun** help command", description=f"User ID: {ctx.message.author.id}", color=0xff9393)
    await bot.send_message(channel, embed=embed)

@bot.command(pass_context=True, no_pm=True)
async def setup_done(ctx):
    author = ctx.message.author
    embed = discord.Embed(description="<a:checkmark:552893708387876884> Setup Complete!", color=0xFFFF)
    embed.add_field(name="Setup Complete. The bot should be running normally now.", value="*:bulb: Make sure it has all of the permissions for the role otherwise the bot will not function correctly.*",inline=True)
    embed.set_footer(text="Requested by: " + author.name)
    await bot.send_message(author, embed=embed)
    embed = discord.Embed(description=" ", color=0xFFFF)
    m=await bot.say("<a:Graphiqloading:551796596350910475>")
    await asyncio.sleep(2)
    await bot.delete_message(m)
    em=discord.Embed()
    await bot.say("<a:checkmark:552893708387876884> Check your dms!")
    embed.add_field(name=":white_check_mark: Success!", value="I've gave you my report in your **Direct Messages**",inline=True)
    await bot.say(embed=embed)

	
@bot.command(pass_context=True)
async def bug(ctx, *, reportmsg):
    channel = bot.get_channel('543488075809030145')
    msg = embed = discord.Embed(title=f"User: {ctx.message.author.name}", description=f"Bug reports: {reportmsg}", color=0xFFFF)
    await bot.send_message(channel, embed=embed)
    text = embed = discord.Embed(title="Your bot bug reports has been submitted", description=f"{ctx.message.author.name}'s message: {reportmsg} ", color=0xFFFF)
    await bot.delete_message(ctx.message)
    await bot.say(embed=embed)
    channel = bot.get_channel('543488075809030145')
    embed = discord.Embed(title=f"User: {ctx.message.author.name} have used bug command", description=f"User ID: {ctx.message.author.id}", color=0xff9393)
    await bot.send_message(channel, embed=embed)
	
@bot.command(pass_context=True)
async def idea(ctx, *, reportmsg):
    channel = bot.get_channel('543488075809030145')
    msg = embed = discord.Embed(title=f"User: {ctx.message.author.name}", description=f"Idea: {reportmsg}", color=0xFFFF)
    await bot.send_message(channel, embed=embed)
    embed = discord.Embed(title="Your idea has been submitted", description=f"{ctx.message.author.name}'s message: {reportmsg} ", color=0xFFFF)
    await bot.delete_message(ctx.message)
    await bot.say(embed=embed)
    channel = bot.get_channel('543488075809030145')
    embed = discord.Embed(title=f"User: {ctx.message.author.name} have used idea command", description=f"User ID: {ctx.message.author.id}", color=0xff9393)
    await bot.send_message(channel, embed=embed)
	
@bot.command(pass_context = True)
async def bans(ctx):
    if ctx.message.author.server_permissions.ban_members == True:
        x = await bot.get_bans(ctx.message.server)
        x = '\n'.join([y.name for y in x])
        embed = discord.Embed(title = "Ban list", description = x, color = 0xFFFFF)
        return await bot.say(embed = embed)
        channel = bot.get_channel('543488075809030145')
        embed = discord.Embed(title=f"User: {ctx.message.author.name} have used bans command", description=f"User ID: {ctx.message.author.id}", color=0xff9393)
        await bot.send_message(channel, embed=embed)
    else:
    	await bot.send_message(ctx.message.channel, "Sorry {}, You don't have requirement permission to use this command `ban members`.".format(ctx.message.author.mention))
	
@bot.command(name="clean", pass_context=True)
async def _clean(ctx, amount=100):
    if ctx.message.author.server_permissions.manage_messages == True:
        channel = ctx.message.channel
        messages = [ ]
        async for message in bot.logs_from(channel, limit=int(amount) + 1):
            messages.append(message)
        await bot.delete_messages(messages)
        msg = await bot.say(f"{amount} messages has been deleted.")
        await asyncio.sleep(5)
        await bot.delete_message(msg)
        channel = bot.get_channel('543488075809030145')
        embed = discord.Embed(title=f"User: {ctx.message.author.name} have used clean command", description=f"User ID: {ctx.message.author.id}", color=0xff9393)
        await bot.send_message(channel, embed=embed)
    else:
    	await bot.send_message(ctx.message.channel, "Sorry {}, You don't have requirement permission to use this command `manage messages`.".format(ctx.message.author.mention))
	
@bot.command(name="mute", pass_context=True)
async def _mute(ctx, user: discord.Member = None, *, arg = None):
    if ctx.message.author.server_permissions.manage_messages == True:
        if user is None:
            await bot.say(":x: Error 302. ``.mute``.")
            return False
        if arg is None:
            await bot.say("Please provide a reason to mute **{}**".format(user.name))
            return False
        reason = arg
        author = ctx.message.author
        role = discord.utils.get(ctx.message.server.roles, name="Muted")
        await bot.add_roles(user, role)
        embed = discord.Embed(title="Mute", description=" ", color=0xFFA500)
        embed.add_field(name="User: ", value="<@{}>".format(user.id), inline=False)
        embed.add_field(name="Moderator: ", value="{}".format(author.mention), inline=False)
        embed.add_field(name="Reason: ", value="{}\n".format(arg), inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/524655977832775710/541446963887996939/Fade_image.png")	
        await bot.say(embed=embed)
    else:
    	await bot.send_message(ctx.message.channel, "Sorry {}, You don't have requirement permission to use this command `manage messages`.".format(ctx.message.author.mention))

@bot.command(name="unmute", pass_context=True)
async def _unmute(ctx, user: discord.Member = None, *, arg = None):
    if ctx.message.author.server_permissions.manage_messages == True:
        if user is None:
            await bot.say(":x: Error 302.")
            return False
        if arg is None:
            await bot.say("Please provide a reason to unmute {}".format(user.name))
            return False
        reason = arg
        author = ctx.message.author
        role = discord.utils.get(ctx.message.server.roles, name="Muted")
        await bot.remove_roles(user, role)
        embed = discord.Embed(title="Unmute", description=" ", color=0x00ff00)
        embed.add_field(name="User: ", value="<@{}>".format(user.id), inline=False)
        embed.add_field(name="Moderator: ", value="{}".format(author.mention), inline=False)
        embed.add_field(name="Reason: ", value="{}\n".format(arg), inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/524655977832775710/541446963887996939/Fade_image.png")	
        await bot.say(embed=embed)
    else:
    	await bot.send_message(ctx.message.channel, "Sorry {}, You don't have requirement permission to use this command `manage_messages`.".format(ctx.message.author.mention))

@bot.command(name="kick", pass_context=True)
async def _kick(ctx, user: discord.Member = None, *, arg = None):
    if ctx.message.author.server_permissions.kick_members == True:
        if user is None:
            await bot.say(":x: Error 302.")
            return False
        if arg is None:
            await bot.say("Please provide a reason to kick {}".format(user.name))
            return False
        reason = arg
        author = ctx.message.author
        await bot.kick(user)
        embed = discord.Embed(title="Kick", description=" ", color=0x00ff00)
        embed.add_field(name="User: ", value="<@{}>".format(user.id), inline=False)
        embed.add_field(name="Moderator: ", value="{}".format(author.mention), inline=False)
        embed.add_field(name="Reason: ", value="{}\n".format(arg), inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/524655977832775710/541446963887996939/Fade_image.png")
        await bot.say(embed=embed)
    else:
    	await bot.send_message(ctx.message.channel, "Sorry {}, You don't have requirement permission to use this command `kick members`.".format(ctx.message.author.mention))
  
@bot.command(name="ban", pass_context=True)
async def _ban(ctx, user: discord.Member = None, *, arg = None):
    if ctx.message.author.server_permissions.ban_members == True:
        if user is None:
            await bot.say(":x: Error 302.")
            return False
        if arg is None:
            await bot.say("Please provide a reason to ban {}".format(user.name))
            return False
        reason = arg
        author = ctx.message.author
        await bot.ban(user)
        embed = discord.Embed(title="Ban", description=" ", color=0xFF0000)
        embed.add_field(name="User: ", value="<@{}>".format(user.id), inline=False)
        embed.add_field(name="Moderator: ", value="{}".format(author.mention), inline=False)
        embed.add_field(name="Reason: ", value="{}\n".format(arg), inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/524655977832775710/541446963887996939/Fade_image.png")
        await bot.say(embed=embed)
    else:
    	await bot.send_message(ctx.message.channel, "Sorry {}, You don't have requirement permission to use this command `ban members`.".format(ctx.message.author.mention))

	
@bot.command(pass_context=True)
async def unban(con,user:int):
    if con.message.author.server_permissions.ban_members == True:
        try:
            who=await bot.get_user_info(user)
            await bot.unban(con.message.server,who)
            await bot.say("The user you wanted to ban has successfully been unbanned.")
        except:
            await bot.say("Oh No, Something went wrong!!")
    else:
    	await bot.send_message(con.message.channel, "Sorry {}, You don't have requirement permission to use this command `ban members`.".format(con.message.author.mention))
	
@bot.command(pass_context=True)
async def stats(ctx):
	author = ctx.message.author
	servers = list(bot.servers)
	embed = discord.Embed(description=" ", color=0xFFFF)
	embed.add_field(name="Servers:", value=f"{str(len(servers))}")
	embed.add_field(name="Users:", value=f"{str(len(set(bot.get_all_members())))}")
	embed.add_field(name="Invite", value=f"[Link](https://discordapp.com/api/oauth2/authorize?client_id=529463184910712872&permissions=0&scope=bot)")
	embed.add_field(name="Support server", value=f"[Link](https://discord.gg/cZuA3sw)")
	embed.add_field(name="Discord Server List", value=f"[Link](https://discordbots.org/bot/529463184910712872#)")
	embed.add_field(name="Memory", value="Free: 10.40GB / Total: 20.80GB",inline=True)
	embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/534386687652921344/543179854544371712/Screenshot_26.png")
	embed.set_footer(text=" | {}".format(bot.user.name), icon_url="https://cdn.discordapp.com/attachments/536467416390041627/543179199268126731/Screenshot_26.png")
	await bot.say(embed=embed)
	channel = bot.get_channel('543488075809030145')
	embed = discord.Embed(title=f"User: {ctx.message.author.name} have used stats command", description=f"User ID: {ctx.message.author.id}", color=0xff9393)
	embed.set_image(url="https://cdn.discordapp.com/attachments/524655977832775710/541446963887996939/Fade_image.png")
	await bot.send_message(channel, embed=embed)
	
@bot.command(pass_context=True)
async def sponsors(ctx):
	author = ctx.message.author
	servers = list(bot.servers)
	embed = discord.Embed(description=":muscle: Our Sponsors! :muscle: ", color=0xFFFF)
	embed.add_field(name="RobuxIsland", value=f"[Link](https://discord.gg/FyGgBy8)")
	embed.add_field(name="GamingLounge", value=f"[Link](https://discord.gg/mx9rSy)")
	embed.add_field(name="City Of London", value=f"[Link](https://discord.gg/B67wz7)")
	embed.add_field(name="Graphic-Topia", value=f"[Link](https://discord.gg/SMWs72)")
	embed.add_field(name="[FREE AD HERE]", value=f"[Link](https://discordapp.com/)")
	embed.add_field(name="[PAID AD HERE]", value=f"[Link](https://discordapp.com/)")
	embed.add_field(name="[PAID AD HERE]", value=f"[Link](https://discordapp.com/)")
	embed.add_field(name="[PAID AD HERE]", value=f"[Link](https://discordapp.com/)")
	embed.add_field(name="[PAID AD HERE]", value=f"[Link](https://discordapp.com/)")
	embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/540965469788700743/546360912680976404/Sponsor-Icon-300x300Red2.png")
	embed.set_footer(text=" | {} | Want to add your server here? DM Mxchael#7748! TIP: The bot should be in the server otherwise your request will be declined.".format(bot.user.name), icon_url="https://cdn.discordapp.com/attachments/546356904369192971/546357447477035029/Sponsor-Icon-300x300Red2.png")
	await bot.say(embed=embed)
	channel = bot.get_channel('543488075809030145')
	embed = discord.Embed(title=f"User: {ctx.message.author.name} have used stats command", description=f"User ID: {ctx.message.author.id}", color=0xff9393)
	embed.set_image(url="https://cdn.discordapp.com/attachments/524655977832775710/541446963887996939/Fade_image.png")
	await bot.send_message(channel, embed=embed)
	
@bot.command(pass_context=True)
async def test(ctx):
	author = ctx.message.author
	servers = list(bot.servers)
	embed = discord.Embed(description="Test", color=0xFFFF)
	embed.add_field(name=" ", value=f"[Link](https://discord.gg/FyGgBy8)")
	embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/540965469788700743/546360912680976404/Sponsor-Icon-300x300Red2.png")
	embed.set_footer(text=" | {}".format(bot.user.name), icon_url="https://cdn.discordapp.com/attachments/546356904369192971/546357447477035029/Sponsor-Icon-300x300Red2.png")
	await bot.say(embed=embed)
	channel = bot.get_channel('543488075809030145')
	embed = discord.Embed(title=f"User: {ctx.message.author.name} have used test command", description=f"User ID: {ctx.message.author.id}", color=0xff9393)
	embed.set_image(url="https://cdn.discordapp.com/attachments/524655977832775710/541446963887996939/Fade_image.png")
	await bot.send_message(channel, embed=embed)
	
@bot.command(pass_context=True)
async def info(ctx):
    '''Displays Info About The Server!'''

    server = ctx.message.server
    roles = [x.name for x in server.role_hierarchy]
    role_length = len(roles)

    roles = ', '.join(roles)
    channelz = len(server.channels)
    time = str(server.created_at); time = time.split(' '); time= time[0]
    join = discord.Embed(description= '%s '%(str(server)),title = 'Server Name', color=0x00D5FF)
    join.set_thumbnail(url = server.icon_url)
    join.add_field(name = 'Owner', value = str(server.owner) + '\n' + server.owner.id)
    join.add_field(name = 'ID', value = str(server.id))
    join.add_field(name = 'Member Count', value = str(server.member_count))
    join.add_field(name = 'Text/Voice Channels', value = str(channelz))
    join.add_field(name = '__Roles (%s)__'%str(role_length), value = roles)
    join.set_footer(text ='Created: %s'%time)
    join.set_image(url="https://cdn.discordapp.com/attachments/524655977832775710/541446963887996939/Fade_image.png")

    return await bot.say(embed = join)
    channel = bot.get_channel('532949494036168706')
    embed = discord.Embed(title=f"User: {ctx.message.author.name} have used info command", description=f"User ID: {ctx.message.author.id}", color=0xff9393)
    embed.set_image(url="https://cdn.discordapp.com/attachments/524655977832775710/541446963887996939/Fade_image.png")	
    await bot.send_message(channel, embed=embed)
	
@bot.command(name="report", pass_context=True)
async def _report(ctx, user: discord.Member = None, *, arg = None):
    if ctx.message.author.server_permissions.send_messages == True:
        log_channel = discord.utils.get(ctx.message.server.channels, name = 'mod-log')
        if user is None:
            await bot.say(":x: Error 302. Please mention a member")
            return False
        if arg is None:
            await bot.say("please provide a reason for reporting {}".format(user.name))
            return False
        reason = arg
        author = ctx.message.author
        server = ctx.message.server
        channel = ctx.message.channel
        em = discord.Embed(title=f"{user} has been reported",description="", color=0x00ff00)
        em.add_field(name="Reason:", value=reason,inline=True)
        em.add_field(name="Moderator:", value=author,inline=True)
        em.add_field(name="In server:", value=server,inline=True)
        em.add_field(name="In Channel:", value=channel,inline=True)
        em.set_footer(text=f"{datetime.datetime.now()}")
        try:
            await bot.send_message(log_channel, embed=em)
        except:
            await bot.say("There doesn't seem to be a channel called `mod-log` in this server! Please create it and try again")
    else:
        await bot.send_message(ctx.message.channel, "Sorry {}, You don't have requirement permission to use this command `manage messages`.".format(ctx.message.author.mention))
	
@bot.command(name="warn", pass_context=True)
async def _warn(ctx, user: discord.Member = None, *, arg = None):
    if ctx.message.author.server_permissions.manage_messages == True:
        if user is None:
            await bot.say(":x: Error 302.")
            return False
        if arg is None:
            await bot.say("please provide a reason to {}".format(user.name))
            return False
        reason = arg
        author = ctx.message.author
        server = ctx.message.server
        embed = discord.Embed(title="Warn", description=" ", color=0x00ff00)
        embed.add_field(name="User: ", value="<@{}>".format(user.id), inline=False)
        embed.add_field(name="Moderator: ", value="{}".format(author.mention), inline=False)
        embed.add_field(name="Reason: ", value="{}\n".format(arg), inline=False)
        await bot.say(embed=embed)
        em = discord.Embed(description=" ", color=0x00ff00)
        em.add_field(name="you have been warned for: ", value=reason)
        em.add_field(name="from:", value=server)
        await bot.send_message(user, embed=em)
    else:
    	await bot.send_message(ctx.message.channel, "Sorry {}, You don't have requirement permission to use this command `manage messages`.".format(ctx.message.author.mention))
	
@bot.command(pass_context=True)
async def puppy(ctx, *, member: discord.Member = None):
  #  Hug someone on the server <3
    try:
        if member is None:
            await bot.say(ctx.message.author.mention + " has been adored! ")
        else:
            if member.id == ctx.message.author.id:
                await bot.say(ctx.message.author.mention + " hugged him self with cuteness :heart:")
            else:
                embed=discord.Embed(description=member.mention + " has been adored by " + ctx.message.author.mention + "!")
                embed.set_image(url="https://media1.tenor.com/images/245862f2c9e21194eb2a491309198491/tenor.gif")
                await bot.say(embed=embed)
    except:
        pass

	
@bot.command(pass_context=True)
async def broadcast(ctx, *, msg):
    if ctx.message.author.id == "341933833136111617":
        for server in bot.servers:
            for channel in server.channels:
                await bot.send_message(channel, msg)
    else:
        pass
		
@bot.command(name='eval', pass_context=True)
async def _eval(ctx, *, command):
    if ctx.message.author.id == "457214181268127747" or "341933833136111617" or "305093302561144833":
        res = eval(command)
        if inspect.isawaitable(res):
            await bot.say(await res)
        else:
            await bot.send_typing(ctx.message.channel)
            await asyncio.sleep(3)
            await bot.say(res)
    else:
        await bot.send_typing(ctx.message.channel)
        await asyncio.sleep(1)
        await bot.send_message(ctx.message.channel, "Sorry {} You have no permission to use this command only the bot owners can use this.".format(ctx.message.author.mention))


@bot.command(pass_context=True)
async def bothelp(ctx):
    m1=await bot.say('Getting the bots information...Please Wait. http://gph.is/2gEPAHj')
    await asyncio.sleep(10)
    await bot.edit_message(m1,new_content='Dont know how to use the bot? Use ``b.help``. Use ``b.stats`` for us in Discord Bot List and make sure to join our Support Server for more help within the bot.')

@bot.command(pass_context=True)
async def restart(ctx):
    m1=await bot.say('<a:Daxarloading:545749821089120258> Restarting the bot...')
    await asyncio.sleep(4)
    await bot.edit_message(m1,new_content='<a:Daxarloading:545749821089120258> Restarting Bot...')
    await asyncio.sleep(4)
    await bot.edit_message(m1,new_content='<a:Daxarloading:545749821089120258> Updating Commands...')
    await asyncio.sleep(4)
    await bot.edit_message(m1,new_content=':white_check_mark: Bot Restarted Sucessfully!')

@bot.event
async def on_message(message):
	if message.content.startswith('Hello'):
		embed=discord.Embed(description=f"Hello {message.author.mention}")
		embed.set_image(url="https://cdn.discordapp.com/attachments/524655977832775710/541446963887996939/Fade_image.png")    
		await bot.send_message(message.channel, embed=embed)
	await bot.process_commands(message)
	
@bot.event
async def on_message(message):
	if message.content.startswith('b.rank'):
		embed=discord.Embed(description=f"Hello {message.author.mention} The rank command hasn't been set-up yet. Please try again later.")
		embed.set_image(url="https://media1.tenor.com/images/84075aec90edf35265cb2713a4cef6d1/tenor.gif?itemid=5012696")    
		await bot.send_message(message.channel, embed=embed)
	await bot.process_commands(message)
	
	
@bot.command(pass_context=True)
async def test1(ctx, user: discord.Member):
    img = Image.open("infoimgimg.png") #Replace infoimgimg.png with your background image.
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Modern_Sans_Light.otf", 100) #Make sure you insert a valid font from your folder.
    fontbig = ImageFont.truetype("Fitamint Script.ttf", 400) #Make sure you insert a valid font from your folder.
    #    (x,y)::↓ ↓ ↓ (text)::↓ ↓     (r,g,b)::↓ ↓ ↓
    draw.text((200, 0), "Information:", (255, 255, 255), font=fontbig)
    draw.text((50, 500), "Username: {}".format(user.name), (255, 255, 255), font=font)
    draw.text((50, 700), "ID:  {}".format(user.id), (255, 255, 255), font=font)
    draw.text((50, 900), "User Status:{}".format(user.status), (255, 255, 255), font=font)
    draw.text((50, 1100), "Account created: {}".format(user.created_at), (255, 255, 255), font=font)
    draw.text((50, 1300), "Nickname:{}".format(user.display_name), (255, 255, 255), font=font)
    draw.text((50, 1500), "Users' Top Role:{}".format(user.top_role), (255, 255, 255), font=font)
    draw.text((50, 1700), "User Joined:{}".format(user.joined_at), (255, 255, 255), font=font)
    img.save('infoimgimg.png') #Change infoimg2.png if needed.
    await bot.upload("infoimgimg.png")
    await bot.say('<a:warning:552881993445015553> The bot needs to restart. Sorry about this. We will get Graphiq running as soon as possible.')
    await bot.logout()
	
bot.run(os.environ['BOT_TOKEN'])
