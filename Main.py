import discord
from discord.ext import commands
import asyncio
import time
from discord import game
import inspect
import os
import random

bot = commands.Bot(command_prefix = ".")
bot.remove_command('help')

async def status():
    while True:
        r=random.choice([1,2,3])
        if r == 1:
await bot.change_presence(game=discord.Game(name=random.choice(['Name of game','League of Legends',"Blade and soul",'Overwatch','No no no!']),type=1)) # type 1 is gaming 2 and 3 is listening or watching
        if r ==2 :
await bot.change_presence(game=discord.Game(name=random.choice(['Name of game','League of Legends',"Blade and soul",'Overwatch','No no no!']),type=1))
        if r == 3:
await bot.change_presence(game=discord.Game(name=random.choice(['Name of game','League of Legends',"Blade and soul",'Overwatch','No no no!']),type=1))
        
        await asyncio.sleep(random.choice([1234,442,123])) #the sleep time is in seconds



#these methods can be used to run the function outside of a function
asyncio.get_event_loop().create_task(status()) #for python version > 3.6 < 3.7

#running async function inside function
async def run():
    await status() #method one 
    bot.loop.create_task(status()) #method 2, this only works when using discord API  since they have a build in way of running it

#the same methods can be used to run the run() fuction as others outside function

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
                await bot.say(member.mention + " has been hugged by " + ctx.message.author.mention + "!")

    except:
        await bot.say("There is an error, either with the bot or a problem with the command")
	
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
  #  Kill someone on the server <3
    try:
        if member is None:
            await bot.say(ctx.message.author.mention + " has been killed!")
        else:
            if member.id == ctx.message.author.id:
                await bot.say(ctx.message.author.mention + "  Commited Suicide. R.I.P")
            else:
                await bot.say(member.mention + " has been killed by " + ctx.message.author.mention + "!")

    except:
        await bot.say("There is an error, either with the bot or a problem with the command")
	

	
@bot.command(pass_context=True, no_pm=True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(description=":mag: Help Section :mag_right:", color=0xFFFF)
    embed.add_field(name=".help_moderation ", value="Lists moderation commands. ||",inline=True)
    embed.add_field(name="help_fun", value="Lists fun commands. ||",inline=True)
    embed.add_field(name=".help_admin", value="Lists Administrator commands.",inline=True)
    embed.add_field(name=".help_credits", value="Lists all the help from Developers to staff.",inline=True)
    embed.set_footer(text="Requested by: " + author.name)
    await bot.send_message(author, embed=embed)
    embed = discord.Embed(description=" ", color=0xFFFF)
    embed.add_field(name=":white_check_mark: Success!", value="I've sent you a list of my commands in your **Direct Messages**",inline=True)
    await bot.say(embed=embed)
    channel = bot.get_channel('543488075809030145')
    embed = discord.Embed(title=f"User: {ctx.message.author.name} have used help command", description=f"User ID: {ctx.message.author.id}", color=0xff9393)
    await bot.send_message(channel, embed=embed)
	
@bot.command(pass_context=True, no_pm=True)
async def help_moderation(ctx):
    author = ctx.message.author
    embed = discord.Embed(description=":lock: Moderation Help Section :lock: ", color=0xFFFF)
    embed.add_field(name=".report", value="Reports user/command",inline=True)
    embed.add_field(name=".mute", value="Mutes a user",inline=True)
    embed.add_field(name=".kick", value="Kicks a user from the server.",inline=True)
    embed.add_field(name=".ban", value="Bans a user from the server.",inline=True)
    embed.add_field(name=".help_setup", value="Set-up bot.",inline=True)
    embed.set_footer(text="Requested by: " + author.name)
    await bot.send_message(author, embed=embed)
    embed = discord.Embed(description=" ", color=0xFFFF)
    embed.add_field(name=":white_check_mark: Success!", value="I've sent you a list of my ``Moderation`` commands in your **Direct Messages**",inline=True)
    await bot.say(embed=embed)
    channel = bot.get_channel('543488075809030145')
    embed = discord.Embed(title=f"User: {ctx.message.author.name} have used **Moderation** help command", description=f"User ID: {ctx.message.author.id}", color=0xff9393)
    await bot.send_message(channel, embed=embed)
	
@bot.command(pass_context=True, no_pm=True)
async def help_admin(ctx):
    author = ctx.message.author
    embed = discord.Embed(description=":lock: Moderation Help Section :lock: ", color=0xFFFF)
    embed.add_field(name=".report", value="Report user/commmand.",inline=True)
    embed.add_field(name=".bans", value="Lists banned users in server.",inline=True)
    embed.add_field(name=".clean", value="Cleans a message less than 98.",inline=True)
    embed.set_footer(text="Requested by: " + author.name)
    await bot.send_message(author, embed=embed)
    embed = discord.Embed(description=" ", color=0xFFFF)
    embed.add_field(name=":white_check_mark: Success!", value="I've sent you a list of my ``Moderation`` commands in your **Direct Messages**",inline=True)
    await bot.say(embed=embed)
    channel = bot.get_channel('543488075809030145')
    embed = discord.Embed(title=f"User: {ctx.message.author.name} have used **admin** help command", description=f"User ID: {ctx.message.author.id}", color=0xff9393)
    await bot.send_message(channel, embed=embed)

@bot.command(pass_context=True, no_pm=True)
async def help_credits(ctx):
    author = ctx.message.author
    embed = discord.Embed(description=":clap: Credits to Developers and Staff :clap:  ", color=0xFFFF)
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
    embed.add_field(name=":white_check_mark: Success!", value="I've sent you a list of my ``Credits`` list in your **Direct Messages**",inline=True)
    await bot.say(embed=embed)
    channel = bot.get_channel('543488075809030145')
    embed = discord.Embed(title=f"User: {ctx.message.author.name} have used **credits** help command", description=f"User ID: {ctx.message.author.id}", color=0xff9393)
    await bot.send_message(channel, embed=embed)

@bot.command(pass_context=True, no_pm=True)
async def help_fun(ctx):
    author = ctx.message.author
    embed = discord.Embed(description=":rofl: Fun Help Section :rofl: ", color=0xFFFF)
    embed.add_field(name=".hello", value="Says hello to you.",inline=True)
    embed.add_field(name=".hug", value="Hugs a user.",inline=True)
    embed.add_field(name=".kill", value="Kills a user.",inline=True)
    embed.add_field(name="``More commands being added soon!``", value="**Remember**, the bot is still in development.",inline=True)
    embed.set_footer(text="Requested by: " + author.name)
    await bot.send_message(author, embed=embed)
    embed = discord.Embed(description=" ", color=0xFFFF)
    embed.add_field(name=":white_check_mark: Success!", value="I've sent you a list of my ``Fun`` commands in your **Direct Messages**",inline=True)
    await bot.say(embed=embed)
    channel = bot.get_channel('543488075809030145')
    embed = discord.Embed(title=f"User: {ctx.message.author.name} have used **Fun** help command", description=f"User ID: {ctx.message.author.id}", color=0xff9393)
    await bot.send_message(channel, embed=embed)
	
@bot.command(pass_context=True, no_pm=True)
async def help_setup(ctx):
    author = ctx.message.author
    embed = discord.Embed(description=":robot Setup Bot's Permissions", color=0xFFFF)
    embed.add_field(name="- Add a rank for the bot", value="Make sure it has all of the permissions.",inline=True)
    embed.add_field(name="- Make sure it is above all of the user ranks.", value="To make sure if a admin is abusing the higher rank can kick.",inline=True)
    embed.add_field(name="- Make sure you join the **Support Server** for more info.", value="Command = .stats --> Support Server --> Link.",inline=True)
    embed.add_field(name="``Thank you for your contibrution.``", value="**Remember**, Put ``.setup_done`` for the verification.",inline=True)
    embed.set_footer(text="Requested by: " + author.name)
    await bot.send_message(author, embed=embed)
    embed = discord.Embed(description=" ", color=0xFFFF)
    embed.add_field(name=":white_check_mark: Success!", value="I've sent you a list of my ``Fun`` commands in your **Direct Messages**",inline=True)
    await bot.say(embed=embed)
    channel = bot.get_channel('543488075809030145')
    embed = discord.Embed(title=f"User: {ctx.message.author.name} have used **Fun** help command", description=f"User ID: {ctx.message.author.id}", color=0xff9393)
    await bot.send_message(channel, embed=embed)

@bot.event
async def on_message(message):
	if message.content.startswith('.setup_done'):
		embed=discord.Embed(description=f"Looks like your ready to go {message.author.mention} Enjoy the bot!")
		embed.set_image(url="https://cdn.discordapp.com/attachments/524655977832775710/541446963887996939/Fade_image.png")    
		await bot.send_message(message.channel, embed=embed)
	await bot.process_commands(message)
	
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
async def report(ctx,user:discord.Member=None,*,reason):
    channel = bot.get_channel("532949494036168706")
    channel2 = bot.get_channel("542401839694348298")
    await bot.send_message(channel,f"{user} has been reported for: **{reason}**")
    await bot.send_message(channel2,f"{user} has been reported for: **{reason}**")
	
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
	embed.add_field(name="Support server", value=f"[Link](https://discord.gg/c3tQZ43)")
	embed.add_field(name="Memory", value="Free: 10.20GB / Total: 20.80GB",inline=True)
	embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/534386687652921344/543179854544371712/Screenshot_26.png")
	embed.set_footer(text=" | {}".format(bot.user.name), icon_url="https://cdn.discordapp.com/attachments/536467416390041627/543179199268126731/Screenshot_26.png")
	await bot.say(embed=embed)
	channel = bot.get_channel('543488075809030145')
	embed = discord.Embed(title=f"User: {ctx.message.author.name} have used stats command", description=f"User ID: {ctx.message.author.id}", color=0xff9393)
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
async def broadcast(ctx, *, msg):
    if ctx.message.author.id == "341933833136111617":
        for server in bot.servers:
            for channel in server.channels:
                await bot.send_message(channel, msg)
    else:
        pass
		
@bot.command(name='eval', pass_context=True)
async def _eval(ctx, *, command):
    if ctx.message.author.id == "493075860975386646" or "341933833136111617" or "305093302561144833":
        res = eval(command)
        if inspect.isawaitable(res):
            await bot.say(await res)
        else:
            await bot.delete_message(ctx.message)
            await bot.send_typing(ctx.message.channel)
            await asyncio.sleep(5)
            await bot.say(res)
    else:
        await bot.send_typing(ctx.message.channel)
        await asyncio.sleep(10)
        await bot.send_message(ctx.message.channel, "Sorry {} You have no permission to use this command only the bot owners can use this.".format(ctx.message.author.mention))

	
@bot.event
async def on_message(message):
	if message.content.startswith('.noob'):
		embed=discord.Embed(description=f"Wys g, u more of teh nub den me {message.author.mention}")
		embed.set_image(url="https://cdn.discordapp.com/attachments/524655977832775710/541446963887996939/Fade_image.png")    
		await bot.send_message(message.channel, embed=embed)
	await bot.process_commands(message)
	

@bot.event
async def on_message(message):
	if message.content.startswith('.credits'):
		embed=discord.Embed(description=f"Bot Owner & Founder: Mxchael & RJ_RBLX05		| Vice Chairman: JayHaggs		 | Bot Developers: NoobPerson, Tunyo-Tex. Thank you for using my bot {message.author.mention}")
		embed.set_image(url="https://cdn.discordapp.com/attachments/524655977832775710/541446963887996939/Fade_image.png")    
		await bot.send_message(message.channel, embed=embed)
	await bot.process_commands(message)
	

@bot.event
async def on_message(message):
	if message.content.startswith('.hello'):
		embed=discord.Embed(description=f"Hello {message.author.mention}")
		embed.set_image(url="https://cdn.discordapp.com/attachments/524655977832775710/541446963887996939/Fade_image.png")    
		await bot.send_message(message.channel, embed=embed)
	await bot.process_commands(message)
	
	
	
bot.run(os.environ['BOT_TOKEN'])
