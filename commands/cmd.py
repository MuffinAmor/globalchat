from check import is_dev
from check import is_lmod
from check import is_mod
from check import is_vipm
from check import is_vip
from check import is_vale
from check import get_xp
from check import get_lvl
from check import user_add_credits
from check import get_credits
from check import user_remove_credits
import discord
from discord.ext import commands
import asyncio
import random
from datetime import datetime
import json
import os
import praw

os.chdir(r'/home/niko/bot/rankdata')
if os.path.isfile("chat.json"):	  
    with open('chat.json', encoding='utf-8') as w:
        gc = json.load(w)
else:
    gc = {}
    gc['global'] = []
    with open('chat.json', 'w') as w:
        json.dump(gc, w, indent=4)

reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='')
					 
bot = commands.Bot(command_prefix='ng!')

botcolor = 0x00ff06

bot.remove_command('help')

class cmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.counter = 0
########################################################################################################################
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot == False:
            for a in gc['global']:
                channelid = ' '.join(a['channelid'])
                numid = int(channelid)
                channel = self.bot.get_channel(numid)
                if channel == None:
                   pass
                else:
                    if message.channel.id == channel.id:
                        send = "yes"
                        break
                    elif not message.channel == channel:
                        send = "None"
                    else:
                        print("lol")
            if send == "yes":
                self.counter =+ 1
                if self.counter == 50:
                    memes_submissions = reddit.subreddit('animememes').hot()
                    post_to_pick = random.randint(1, 100)
                    for i in range(0, post_to_pick):
                        submission = next(x for x in memes_submissions if not x.stickied)
                    embed = discord.Embed(title=submission.title, color=botcolor)
                    embed.set_image(url=submission.url)
                    embed.set_footer(text='reddit.com')
                    embed.timestamp = datetime.utcnow()
                    for server in self.bot.guilds:
                        for current_global in gc['global']:
                            if str(server.id) in str(current_global['id']):
                                channelid = ' '.join(current_global['channelid'])		
                                numid2 = int(channelid)	
                                channel = self.bot.get_channel(numid2)		
                                if channel:
                                    try:
                                        await channel.send(embed=embed)
                                    except:
                                        pass   
                    self.counter =- 0 

    @commands.command()
    @is_dev()
    async def news(self, ctx, *new:str):
        if ctx.author.bot==False: 
            msg = ' '.join(new)
            for s in self.bot.guilds:
                for a in gc['global']:
                    channelid = ' '.join(a['channelid'])
                    numid = int(channelid)
                    channel = self.bot.get_channel(numid)
                    if s.id == a['id']:
                        try:
                            embed=discord.Embed(title="NEWSFLASH", description=msg, color=0xff0000)
                            embed.timestamp = datetime.utcnow()
                            embed.set_footer(text="Newsflash", icon_url=ctx.message.author.avatar_url)
                            embed.set_thumbnail(url="https://discordapp.com/channels/560579302740197376/560579412333166612/618161680106520583")
                            await channel.send(embed=embed)
                            await asyncio.sleep(0.5)
                        except Exception as error:
                            print(error)
                            if error.code == 50013:
                                try:
                                    await channel.send("NEWSFLASH\n>>>{}".format(ctx.message.author.name, level, msg)) 
                                except:
                                    pass
                            else:
                                try:
                                    e = self.bot.get_channel(617779357829562368)
                                    embed=discord.Embed(
                                        color=message.author.color)
                                    embed.add_field(name='Fail message from **{0}**'.format(s), value="```python\n{}```".format(error), inline=False)
                                    embed.timestamp = datetime.utcnow()
                                    embed.set_thumbnail(url=s.icon_url)
                                    embed.set_footer(text=s.id, icon_url=message.author.avatar_url)
                                    await e.send(embed=embed)   
                                except:
                                    pass 


    @bot.command(, aliases=["invite"])
    async def botinv(self, ctx):
        if ctx.author.bot==False: 
            embed =discord.Embed(color=ctx.author.top_role.color)
            embed.add_field(name="<:Neko_Logo:549531102117625866>Lucy Invite Link<:Neko_Logo:549531102117625866>", value="[Do you like invite me? Click me!](https://discordapp.com/oauth2/authorize?client_id=631149351112146957&permissions=1074097361&redirect_uri=https%3A%2F%2Fdiscord.gg%2FUkAtVuB&scope=bot)")
            embed.set_footer(text='Message was requested by {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            msg = await ctx.channel.send(embed=embed)
					
    @bot.command(pass_context = True)
    async def support(self, ctx):
        if ctx.author.bot==False:
            channel = self.bot.get_channel(638414867656736770)
            invitelinknew = await channel.create_invite(xkcd = True, max_age=600, reason="support")
            embed =discord.Embed(color=ctx.author.top_role.color)
            embed.add_field(name="<:Neko_Logo:549531102117625866>Support Server Invite Link<:Neko_Logo:549531102117625866>", value="[Do you need help? Click me!]({})".format(invitelinknew))
            embed.set_footer(text='Message was requested by {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            msg = await ctx.channel.send(embed=embed)
            			
    @bot.command(pass_context = True)	
    @commands.has_permissions(administrator=True)	
    async def leave(self, ctx):
        if ctx.author.bot==False:
            await ctx.message.delete()
            await ctx.guild.leave()
			
    @bot.command()
    @commands.cooldown(3, 60, commands.BucketType.user)
    async def globalinfo(self, ctx):				
        if ctx.author.bot==False: 			
                embed1=discord.Embed(title='Welcome {0} in the Global Network!'.format(ctx.message.author.guild), color=ctx.message.author.color)
                embed1.add_field(name='What is the Global Network?', value='The Global Network is a Channel in your server, in there you can write with other Users from others servers, without Server changing.', inline=False)
                embed1.add_field(name='How works this?', value='Thats easy. You need only to write a message in the channel and the Bot send it in the Network!\n**!!!Attention: You __can´t__ callback a message!!!**', inline=True)
                embed1.add_field(name='Can i change my chat color?', value='Sure, you write with your current rolecolor from the Server where you send the message!', inline=True)
                embed1.add_field(name='Whats my chatname?', value='Your chatname is your account Name', inline=True)
                embed1.add_field(name='What can i do when i need help?', value='write ng!support and join our great Support Server', inline=True)
                embed1.add_field(name='Are there Rules?', value='Yes, Serverinvites, here and everyone mentions and links get blocked from the Network.\n Other side, the Networkdeveloper block users who be rouge and make other users angry.\nSo please stay friendly.', inline=True)
                embed1.set_footer(text='Server joined: {}'.format(ctx.message.author.guild), icon_url=ctx.message.guild.icon_url)
                embed1.timestamp = datetime.utcnow()
                embed1.set_thumbnail(url=ctx.message.author.guild.icon_url)
                await ctx.channel.send(embed=embed1)
	
    @bot.command()
    async def info(self, ctx):				
        if ctx.author.bot==False:   
            for current_global in gc['global']:
                if not ctx.guild.id == current_global['id']:
                    channelname = "---------"  
                if ctx.guild.id == current_global['id']:
                    channelid = ' '.join(current_global['channelid'])
                    numid1 = int(channelid)
                    channelname = self.bot.get_channel(numid1)		
                    break
            servers = list(self.bot.guilds)
            member = sum(len(s.members) for s in self.bot.guilds)	
            embed=discord.Embed(title='Neko Global Network Botinfo', color=ctx.author.color)
            embed.add_field(name='Botusers', value=member, inline=True)
            embed.add_field(name='Botservers', value=str(len(servers)), inline=True)
            embed.add_field(name='Your chatcolor:', value=ctx.author.color, inline=False)
            embed.add_field(name='Your chatname:', value=ctx.author.name, inline=True)
            embed.add_field(name='Your chatserver:', value=ctx.author.guild.name, inline=True)
            embed.add_field(name='Your Globalchannel:', value=channelname, inline=True)
            embed.set_footer(text='Botinfo asked by {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            embed.set_thumbnail(url=ctx.author.guild.icon_url)
            await ctx.channel.send(embed=embed)

				
    @bot.command()
    @is_vip()
    @commands.cooldown(5, 600, commands.BucketType.user)
    async def globalanime(self, ctx):
        if ctx.author.bot==False:  
            memes_submissions = reddit.subreddit('animememes').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)
            embed = discord.Embed(title=submission.title, color=botcolor)
            embed.set_image(url=submission.url)
            embed.set_footer(text='reddit.com')
            embed.timestamp = datetime.utcnow()
            for server in self.bot.guilds:
                for current_global in gc['global']:
                    if str(server.id) in str(current_global['id']):
                        channelid = ' '.join(current_global['channelid'])		
                        numid2 = int(channelid)	
                        channel = self.bot.get_channel(numid2)		
                        if channel:
                            try:
                                await channel.send(embed=embed)
                            except:
                                pass


    
    @bot.command(pass_context = True, aliases=['rank'])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def money(self, ctx, member: discord.Member = None):
        with open('users.json', 'r') as f:
            self.users = json.load(f)
        if ctx.message.author.bot==False:
            return
        try:
            member = member or ctx.author
            autohr_id = str(member.id) or str(ctx.author.id)
            embed = discord.Embed(title="{}'s Credits".format(member.name), color=member.color, timestamp=datetime.now())
            embed.add_field(name='Credits', value=get_credits(str(member.id)), inline = 'False')
            await ctx.channel.send(embed=embed)
        except KeyError:
            embed = discord.Embed(color=member.color, timestamp=datetime.now())
            embed.add_field(name='{} is not in the Database'.format(member.name), value='** **')
            await ctx.channel.send(embed=embed)


    #@bot.command(pass_context = True, aliases=['glb'])
    #async def topten(self, ctx):
    #    with open('users.json', 'r') as f:
    #        self.users = json.load(f)
    #    if ctx.message.author.bot==False:
    #        return
    #    try:
    #        high_score_list = sorted(self.users, key=lambda x : self.users[x].get('exp', 0), reverse=True)
    #        message = ''
    #        count = 00
    #        for number, user in enumerate(high_score_list):
    #            member = self.bot.get_user(int(user))
    #            if number == 10:
    #                break
    #            else:
    #                if member == None:
    #                    pass
    #                if not member == None:
    #                    message += '{0}. {1}\n   Level {2} with {3}exp\n\n'.format(number + 1, member.name, self.users[user].get('level', 0), self.users[user].get('exp', 0))
    #                    count =+ 1
    #        embed = discord.Embed(title="Global Leaderboard", color=ctx.author.color)
    #        embed.add_field(name='Top 10 Chatters', value=message)
    #        embed.timestamp = datetime.utcnow()
    #        embed.set_footer(text='{}'.format(ctx.author.name), icon_url=ctx.author.avatar_url)
    #        await ctx.channel.send(embed=embed)
    #    except KeyError:
    #        embed = discord.Embed(color=member.color, timestamp=datetime.now())
    #        embed.add_field(name='{} is not in the Database'.format(member.name), value='** **')
    #        await ctx.channel.send(embed=embed)
	#
    #@bot.command(pass_context = True, aliases=['slb'])
    #async def leaderboard(self, ctx):
    #    with open('users.json', 'r') as f:
    #        self.users = json.load(f)
    #    if ctx.message.author.bot==False:
    #        return
    #    try:
    #        high_score_list = sorted(self.users, key=lambda x : self.users[x].get('exp', 0), reverse=True)
    #        message = ''
    #        count = 00
    #        gm = '' 
    #        for nutzer in ctx.guild.members:
    #            gm += nutzer.name
    #        for number, user in enumerate(high_score_list):
    #            member = self.bot.get_user(int(user))
    #            if number == 10:
    #                break
    #            else:
    #                if not member == None:
    #                    if member.name in gm:
    #                        if member == None:
    #                            pass
    #                        if not member == None:
    #                            message += '{0}. {1}\n   Level {2} with {3}exp\n\n'.format(number + 1, member.mention, self.users[user].get('level', 0), self.users[user].get('exp', 0))
    #                            count =+ 1
    #        embed = discord.Embed(title="Server Leaderboard", color=ctx.author.color)
    #        embed.add_field(name='Top 10 Chatters', value=message)
    #        embed.timestamp = datetime.utcnow()
    #        embed.set_footer(text='{}'.format(ctx.author.name), icon_url=ctx.author.avatar_url)
    #        await ctx.channel.send(embed=embed)
    #    except KeyError:
    #        embed = discord.Embed(color=member.color, timestamp=datetime.now())
    #        embed.add_field(name='{} is not in the Database'.format(member.name), value='** **')
    #        await ctx.channel.send(embed=embed)
			
			
			


def setup(bot):
    bot.add_cog(cmd(bot))