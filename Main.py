import discord
from discord.ext import commands
import asyncio
import time
from discord import game
import inspect
import os

bot = commands.Bot(command_prefix = ".")
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="{} servers | .help".format(len(bot.servers)), type = 3))

@bot.event
async def on_message(message):
	if message.content.startswith('.hello'):
		embed=discord.Embed(description=f"Hello, {message.author.mention}")
		embed.set_image(url="https://cdn.discordapp.com/attachments/524655977832775710/541446963887996939/Fade_image.png")    
		await bot.send_message(message.channel, embed=embed)
	await bot.process_commands(message)
	
@bot.event
async def on_message(message):
	if message.content.startswith('.credits'):
		embed=discord.Embed(description=f"Bot Owner & Founder: Mxchael 		|| Bot Developers: NoobPerson, Tunyo-Tex., {message.author.mention}")
		embed.set_image(url="https://cdn.discordapp.com/attachments/524655977832775710/541446963887996939/Fade_image.png")    
		await bot.send_message(message.channel, embed=embed)
	await bot.process_commands(message)

	
@bot.command(pass_context=True, no_pm=True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(description="Help Section", color=0xFFFF)
    embed.add_field(name=".hello", value="Make the bot say hello to you.",inline=True)
    embed.add_field(name=".bug", value="Only use this command if the bot is acting weird on specific command.",inline=True)
    embed.add_field(name=".idea", value="Send your idea about new commands the bot don't have.",inline=True)
    embed.add_field(name=".mute", value=".mute @user <reason>",inline=True)
    embed.add_field(name=".unmute", value=".unmute @user <reason>",inline=True)
    embed.add_field(name=".kick", value=".kick @user <reason>",inline=True)
    embed.add_field(name=".ban", value=".ban @user <reason>",inline=True)
    embed.add_field(name=".unban", value=".unban <user id>",inline=True)
    embed.add_field(name=".info", value="get info about server",inline=True)
    embed.add_field(name=".removewarns me", value="Removes your warn.",inline=True)
    embed.set_footer(text="Requested by: " + author.name)
    await bot.send_message(author, embed=embed)
    embed = discord.Embed(description=" ", color=0xFFFF)
    embed.add_field(name=":white_check_mark: Success!", value="(I've sent you a list of my commands in your **Direct Messages**",inline=True)
    await bot.say(embed=embed)
    channel = bot.get_channel('532949494036168706')
    embed = discord.Embed(title=f"User: {ctx.message.author.name} have used help command", description=f"User ID: {ctx.message.author.id}", color=0xff9393)
    await bot.send_message(channel, embed=embed)

@bot.command(pass_context=True)
async def bug(ctx, *, reportmsg):
    channel = bot.get_channel('532949494036168706')
    msg = embed = discord.Embed(title=f"User: {ctx.message.author.name}", description=f"Bug reports: {reportmsg}", color=0xFFFF)
    await bot.send_message(channel, embed=embed)
    text = embed = discord.Embed(title="Your bot bug reports has been submitted", description=f"{ctx.message.author.name}'s message: {reportmsg} ", color=0xFFFF)
    await bot.delete_message(ctx.message)
    await bot.say(embed=embed)
    channel = bot.get_channel('532949494036168706')
    embed = discord.Embed(title=f"User: {ctx.message.author.name} have used bug command", description=f"User ID: {ctx.message.author.id}", color=0xff9393)
    await bot.send_message(channel, embed=embed)
    
@bot.command(pass_context=True)
async def idea(ctx, *, reportmsg):
    channel = bot.get_channel('532949494036168706')
    msg = embed = discord.Embed(title=f"User: {ctx.message.author.name}", description=f"Idea: {reportmsg}", color=0xFFFF)
    await bot.send_message(channel, embed=embed)
    embed = discord.Embed(title="Your idea has been submitted", description=f"{ctx.message.author.name}'s message: {reportmsg} ", color=0xFFFF)
    await bot.delete_message(ctx.message)
    await bot.say(embed=embed)
    channel = bot.get_channel('532949494036168706')
    embed = discord.Embed(title=f"User: {ctx.message.author.name} have used idea command", description=f"User ID: {ctx.message.author.id}", color=0xff9393)
    await bot.send_message(channel, embed=embed)
	
@bot.command(pass_context = True)
async def bans(ctx):
    if ctx.message.author.server_permissions.ban_members == True:
        x = await bot.get_bans(ctx.message.server)
        x = '\n'.join([y.name for y in x])
        embed = discord.Embed(title = "Ban list", description = x, color = 0xFFFFF)
        return await bot.say(embed = embed)
        channel = bot.get_channel('532949494036168706')
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
        channel = bot.get_channel('532949494036168706')
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
	embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/529463184910712872/d815415e8d6030181078ec7bf7c914a0.png?size=1024")
	embed.set_footer(text=" | {}".format(bot.user.name), icon_url="https://cdn.discordapp.com/avatars/529463184910712872/d815415e8d6030181078ec7bf7c914a0.png?size=1024")
	await bot.say(embed=embed)
	channel = bot.get_channel('532949494036168706')
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
	
	

@bot.command(name="report", pass_context=True)
async def _warn(ctx, user: discord.Member = None, *, arg = None):
    if ctx.message.author.server_permissions.send_messages == True:
        if user is None:
            await bot.say(":x: Error 302. Please provide a user.")
            return False
        if arg is None:
            await bot.say("Please Provide A  User To Report {}".format(user.name))
            return False
        reason = arg
        author = ctx.message.author
        server = ctx.message.server
        embed = discord.Embed(title="Report Card Submitted!", description=" ", color=0x00ff00)
        embed.add_field(name="User: ", value="<@{}>".format(user.id), inline=False)
        embed.add_field(name="Reporter: ", value="{}".format(author.mention), inline=False)
        embed.add_field(name="Reason: ", value="{}\n".format(arg), inline=False)
	channel = bot.get_channel('532949494036168706')
        await bot.say(embed=embed)
        em = discord.Embed(description=" ", color=0x00ff00)
        em.add_field(name="You have been reported for: ", value=reason)
        await bot.send_message(user, embed=em)
    else:
    	await bot.send_message(ctx.message.channel, "Sorry {}, You don't have requirement permission to use this command `manage messages`.".format(ctx.message.author.mention))
	
@bot.command(name='eval', pass_context=True)
async def _eval(ctx, *, command):
    if ctx.message.author.id == "493075860975386646" or "341933833136111617" or "459738312412889098":
        res = eval(command)
        if inspect.isawaitable(res):
            await bot.say(await res)
        else:
            await bot.delete_message(ctx.message)
            await bot.say(res)
    else:
    	await bot.send_message(ctx.message.channel, "Sorry {} You have no permission to use this command only the bot owners can use this.".format(ctx.message.author.mention))
		
@bot.command(name="servers")
async def _servers(ctx):
    if ctx.message.author.id == "493075860975386646" or "341933833136111617" or "459738312412889098":
        servers = list(bot.servers)
        await bot.say("Connected on " + str(len(bot.servers)) + " servers:")
        await bot.say('\n'.join(server.name for server in servers))
    else:
    	await bot.send_message(ctx.message.channel, "Sorry {} you can't use this command".format(ctx.message.author.mention))
	
@bot.command(pass_context=True)
async def broadcast(ctx, *, msg):
    if ctx.message.author.id == "341933833136111617":
        for server in bot.servers:
            for channel in server.channels:
                await bot.send_message(channel, msg)
    else:
        pass
		


bot.run(os.environ['BOT_TOKEN'])
