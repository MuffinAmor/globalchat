from check import is_dev
from check import is_vale
import discord
from discord.ext import commands 
import asyncio
from datetime import datetime
import json
import os

os.chdir(r'/home/niko/bot/rankdata')

if os.path.isfile("wordblocker.json"):	 	
    with open('wordblocker.json', encoding='utf-8') as m:
        blocked = json.load(m)
else:
    blocked = {}
    blocked['global'] = []
    with open('wordblocker.json', 'w') as f:
        json.dump(blocked, f, indent=4)

bot = commands.Bot(command_prefix='ng!')

botcolor = 0xffffff

bot.remove_command('help')


class owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @is_dev()
    async def rankuser(self, ctx):
        if ctx.author.bot==False: 
            with open('rank.json', encoding='utf-8') as r:
                rank = json.load(r)
            dev = ""
            lmod = ""
            mod = ""
            pmod = ""
            partner = ""
            vips = ""
            vip = ""
            vipm = ""
            banned = ""
            devcount = "d"
            lmodcount = "l"
            modcount = "m"
            pmodcount = "p"
            vipmcount = "v"
            partnercount = "a"
            vipscount = "s"
            vipcount = "v"
            bannedcount = "b"
            for i in rank['dev']:
                for a in i['id']:
                    id = int(a)
                    user = self.bot.get_user(id)
                    if user == None:
                        i['id'].remove(a)
                    else:
                        dev += "{}. {} | {}\n".format(len(devcount), user.name, user.id)
                    devcount += "d" 
            for i in rank['lmod']:
                for b  in i['id']:
                    id = int(b)
                    user = self.bot.get_user(id)
                    if user == None:
                        i['id'].remove(b)
                    else:
                        lmod+= "{}. {} | {}\n".format(len(lmodcount), user.name, user.id)
                        lmodcount += "l"
            for i in rank['mod']:
                for c in i['id']:	
                    id = int(c)
                    user = self.bot.get_user(id)
                    if user == None:
                        i['id'].remove(c)
                    else:
                        mod+= "{}. {} | {}\n".format(len(modcount), user.name, user.id) 
                        modcount += "m"
            for i in rank['pmod']:
                for d in i['id']:	
                    id = int(d)
                    user = self.bot.get_user(id)
                    if user == None:
                        i['id'].remove(d)
                    elif d in mod:
                        i['id'].remove(d)
                    else:
                        pmod+= "{}. {} | {}\n".format(len(pmodcount), user.name, user.id)
                        pmodcount += "p"
            for i in rank['manager']:
                for a in i['id']:
                    id = int(a)
                    user = self.bot.get_user(id)
                    if user == None:
                        i['id'].remove(a)
                    else:
                        vipm += "{}. {} | {}\n".format(len(vipmcount), user.name, user.id)
                    vipmcount += "v" 						
            for i in rank['partner']:
                for e in i['id']:	
                    id = int(e)
                    server = self.bot.get_guild(id)
                    if server == None:
                        i['id'].remove(e)
                    else:
                        partner+= "{}. {} | {}\n".format(len(partnercount), server, server.id)
                        partnercount += "a"
            for i in rank['vips']:
                for f in i['id']:	
                    id = int(f)
                    server = self.bot.get_guild(id)
                    if server == None:
                        i['id'].remove(f)
                    elif f in partner:
                        i['id'].remove(f)
                    else:
                        vips+= "{}. {} | {}\n".format(len(vipscount), server, server.id)
                        vipscount += "s"
            for i in rank['vip']:
                for g in i['id']:	
                    id = int(g)
                    user = self.bot.get_user(id)
                    if user == None:
                        i['id'].remove(g)
                    else:
                        vip+= "{}. {} | {}\n".format(len(vipcount), user.name, user.id)	
                        vipcount += "v"
            for i in rank['banned']:
                for h in i['id']:	
                    id = int(h)
                    user = self.bot.get_user(id)
                    if user == None:
                        banned+= "{}. {}\n".format(len(bannedcount), h)
                        bannedcount += "b"
                    else:
                        banned+= "{}. {} | {}\n".format(len(bannedcount), user.name, user.id)
                        bannedcount += "b"
            with open('rank.json', 'w') as r:
                json.dump(rank, r, indent=4)
            embed=discord.Embed(title="DEVs", description=dev, color=ctx.author.color)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text="DEV Users", icon_url=ctx.message.author.avatar_url)
            await ctx.channel.send(embed=embed)
            embed=discord.Embed(title="LMODs", description=lmod, color=ctx.author.color)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text="LMOD Users", icon_url=ctx.message.author.avatar_url)
            await ctx.channel.send(embed=embed)
            embed=discord.Embed(title="MODs", description=mod, color=ctx.author.color)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text="MOD Users", icon_url=ctx.message.author.avatar_url)
            await ctx.channel.send(embed=embed)
            embed=discord.Embed(title="PMODs", description=pmod, color=ctx.author.color)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text="PMOD Users", icon_url=ctx.message.author.avatar_url)
            await ctx.channel.send(embed=embed)
            embed=discord.Embed(title="VIP Manager", description=vipm, color=ctx.author.color)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text="VIP Manager", icon_url=ctx.message.author.avatar_url)
            await ctx.channel.send(embed=embed)
            embed=discord.Embed(title="PARTNER Server", description=partner, color=ctx.author.color)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text="PARTNER Server", icon_url=ctx.message.author.avatar_url)
            await ctx.channel.send(embed=embed)
            embed=discord.Embed(title="VIP Server", description=vips, color=ctx.author.color)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text="VIP Server", icon_url=ctx.message.author.avatar_url)
            await ctx.channel.send(embed=embed)
            embed=discord.Embed(title="VIPs", description=vip, color=ctx.author.color)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text="VIP User", icon_url=ctx.message.author.avatar_url)
            await ctx.channel.send(embed=embed)
            embed=discord.Embed(title="BANNED", description=banned, color=ctx.author.color)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text="BANNED User", icon_url=ctx.message.author.avatar_url)
            await ctx.channel.send(embed=embed)		

		
    @commands.command()
    @is_vale()
    async def clean(self, ctx):
        with open('chat.json', encoding='utf-8') as w:
            gc = json.load(w)
        servers = list(a.id for a in self.bot.guilds)
        for i in gc['global']:
            if i['id'] in servers:
                try:
                    del i['enable']
                except:
                    pass
                try:
                    del i['channelname']
                except:
                    pass
                with open('chat.json','w+') as w:
                    json.dump(gc,w, indent=4)				
            if not i['id'] in servers:
                try:
                    del i['name']
                except:
                    pass
                try:
                    del i['channelid']
                except:
                    pass
                try:
                    del i['channelname'] 
                except:
                    pass
                try:
                    del i['enable']
                except:
                    pass
                try:
                    del i['id']
                except:
                    pass
                gc['global'].remove({})
                with open('chat.json','w+') as w:
                    json.dump(gc,w, indent=4)
            print(i)
        await ctx.send("fin")
########################################################################################################################
    @bot.command(pass_context = True)	
    @is_dev()		
    async def remoteleave(self, ctx, id:int):
        if ctx.author.bot==False: 
            server = self.bot.get_guild(id)
            await ctx.message.delete()
            await ctx.channel.send("I leave the server {0}".format(server.name))
            await server.leave()
		  
    @bot.command(pass_context=True)
    @is_dev()
    async def findserver(self, ctx, serverID:int):
        if ctx.author.bot==False: 
            server = self.bot.get_guild(serverID)
            gen = discord.utils.get(server.text_channels, name="general")
            if gen:
                try:
                    server = self.bot.get_server(serverID)
                    channel = discord.utils.get(server.text_channels, name="general")
                    invitelinknew = await channel.create_invite(xkcd = True, max_uses = 100)
                    embed=discord.Embed(
                        color=botcolor)
                    embed.add_field(name='__Server Stats__', value='** **', inline='False')
                    embed.add_field(name='Servername:', value='{0.name}'.format(server), inline='True')
                    embed.add_field(name='Server ID:', value='{}'.format(server.id), inline='True')
                    embed.add_field(name='Membercount:', value='{0.member_count} members'.format(server), inline='False')
                    embed.add_field(name='Serverowner:', value='{}'.format(server.owner.mention), inline='False')
                    embed.add_field(name='Created at:', value='{}'.format(server.created_at))
                    embed.add_field(name="Discord Invite Link", value=invitelinknew)
                    embed.set_thumbnail(url=server.icon_url)	
                    author = ctx.author
                    embed.set_footer(text='Message was requested by {}'.format(author))
                    embed.timestamp = datetime.utcnow()
                    await ctx.channel.send(embed=embed)
                except:
                    server = self.bot.get_guild(serverID)
                    embed=discord.Embed(
                        color=botcolor)
                    embed.add_field(name='__Server Stats__', value='** **', inline='False')
                    embed.add_field(name='Servername:', value='{0.name}'.format(server), inline='True')
                    embed.add_field(name='Server ID:', value='{}'.format(server.id), inline='True')
                    embed.add_field(name='Membercount:', value='{0.member_count} members'.format(server), inline='False')
                    embed.add_field(name='Serverowner:', value='{}'.format(server.owner.mention), inline='False')
                    embed.add_field(name='Created at:', value='{}'.format(server.created_at))
                    embed.set_thumbnail(url=server.icon_url)	
                    author = ctx.message.author
                    embed.set_footer(text='Message was requested by {}'.format(author))
                    embed.timestamp = datetime.utcnow()
                    await ctx.channel.send(embed=embed)
            else:
                server = self.bot.get_guild(serverID)
                embed=discord.Embed(
                    color=botcolor)
                embed.add_field(name='__Server Stats__', value='** **', inline='False')
                embed.add_field(name='Servername:', value='{0.name}'.format(server), inline='True')
                embed.add_field(name='Server ID:', value='{}'.format(server.id), inline='True')
                embed.add_field(name='Membercount:', value='{0.member_count} members'.format(server), inline='False')
                embed.add_field(name='Serverowner:', value='{}'.format(server.owner.mention), inline='False')
                embed.add_field(name='Created at:', value='{}'.format(server.created_at))
                embed.set_thumbnail(url=server.icon_url)	
                author = ctx.message.author
                embed.set_footer(text='Message was requested by {}'.format(author))
                embed.timestamp = datetime.utcnow()
                await ctx.channel.send(embed=embed)	   
			
    @bot.command(pass_context=True) 
    @is_dev()
    async def getinvite(self, ctx, id:int):
        if ctx.author.bot==False: 
            server = self.bot.get_guild(id)
            inv = await server.invites()
            for invites in inv:
                embed = discord.Embed(title="Invite Info", description="", color=botcolor)
                embed.add_field(name="Creator:", value=invites.inviter, inline=True)
                embed.add_field(name="Channel:", value=invites.channel.mention, inline=True)
                embed.add_field(name="Uses", value=invites.uses, inline=False)
                embed.add_field(name="Invite", value=invites, inline=False)
                embed.set_thumbnail(url=server.icon_url)
                embed.timestamp = datetime.utcnow()
                msg = await ctx.channel.send(embed=embed)
                await msg.add_reaction("🆗")
                await msg.add_reaction("❌")
                await asyncio.sleep(0.5)
                def pred(m):
                    return m.author == ctx.message.author and m.channel == ctx.message.channel
                msg = await self.bot.wait_for('n', check=pred)
	 		
    @bot.command(pass_context=True)
    @is_dev()
    async def globalidcheck(self, ctx, userId:int):
        embed = discord.Embed(title="Mutual Servers:", description="", color=botcolor)
        embed.add_field(name="User", value='** **', inline=True)
        embed.add_field(name="User ID", value='** **', inline=True)
        embed.add_field(name="Server", value='** **', inline=False)
        embed.add_field(name="Server ID", value='** **', inline=False)
        embed.set_thumbnail(url=ctx.message.guild.icon_url)
        embed.timestamp = datetime.utcnow()
        msg = await ctx.channel.send(embed=embed)
        await asyncio.sleep(0.5)
        servers = list(self.bot.guilds)
        for server in self.bot.guilds:
            for member in server.members:
                if member.id == userId:	
                    embed = discord.Embed(title="Mutual Servers:", description="", color=botcolor)
                    embed.add_field(name="User", value=member.name, inline=True)
                    embed.add_field(name="User ID", value=member.id, inline=True)
                    embed.add_field(name="Server", value=server.name, inline=False)
                    embed.add_field(name="Server ID", value=server.id, inline=True)
                    embed.set_thumbnail(url=server.icon_url)
                    embed.timestamp = datetime.utcnow()
                    await msg.edit(embed=embed)
                    def pred(m):
                        return m.author == ctx.message.author and m.channel == ctx.message.channel
                    message = await self.bot.wait_for('message', check=pred)
                    await message.delete()
        else:
                    await msg.delete()
                    msg = await ctx.channel.send("Nope. No more mutual Servers with this user")
                    await asyncio.sleep(60)
                    await msg.delete()
	
 
#########################################################################################################################
    @commands.Cog.listener()
    async def on_guild_remove(self, guild): 
        guilds = list(self.bot.guilds)
        home = self.bot.get_guild(382290709249785857)
        member = sum(len(s.members) for s in self.bot.guilds)
        channel1 = self.bot.get_channel(608971363788652544)
        channel4 = self.bot.get_channel(608971366233931776)
        await channel1.edit(name="Totalusers : {}".format(member))
        await channel4.edit(name="Server: {}".format(str(len(guilds))))
#########################################################################################################################
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        guilds = list(self.bot.guilds)
        home = self.bot.get_guild(382290709249785857)
        member = sum(len(s.members) for s in self.bot.guilds)
        channel1 = self.bot.get_channel(608971363788652544)
        channel4 = self.bot.get_channel(608971366233931776)
        await channel1.edit(name="Totalusers : {}".format(member))
        await channel4.edit(name="Server: {}".format(str(len(guilds))))
#########################################################################################################################
    @commands.Cog.listener()
    async def on_member_join(self, member):
        guilds = list(self.bot.guilds)
        home = self.bot.get_guild(382290709249785857)
        member = sum(len(s.members) for s in self.bot.guilds)
        channel1 = self.bot.get_channel(608971363788652544)
        channel4 = self.bot.get_channel(608971366233931776)
        await channel1.edit(name="Totalusers : {}".format(member))
        await channel4.edit(name="Server: {}".format(str(len(guilds))))
#########################################################################################################################
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        guilds = list(self.bot.guilds)
        home = self.bot.get_guild(382290709249785857)
        member = sum(len(s.members) for s in self.bot.guilds)
        channel1 = self.bot.get_channel(608971363788652544)
        channel4 = self.bot.get_channel(608971366233931776)
        await channel1.edit(name="Totalusers : {}".format(member))
        await channel4.edit(name="Server: {}".format(str(len(guilds))))

    @commands.command()
    async def statsetup(self, ctx):		
        guilds = list(self.bot.guilds)
        member = sum(len(s.members) for s in self.bot.guilds)
        channel1 = self.bot.get_channel(608971363788652544)
        channel4 = self.bot.get_channel(608971366233931776)
        await channel1.edit(name="Totalusers : {}".format(member))
        await channel4.edit(name="Server: {}".format(str(len(guilds))))
		
def setup(bot):
    bot.add_cog(owner(bot))
