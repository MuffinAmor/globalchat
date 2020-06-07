from check import get_xp
from check import get_lvl
from check import user_add_credits
from check import get_credits
from check import user_remove_credits
from check import get_time
import discord
from discord.ext import commands
import asyncio
import time
import sys
import random
from datetime import datetime
from urllib.error import HTTPError
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
    with open('chat.json', 'w') as f:
        json.dump(gc, f, indent=4)


if os.path.isfile("wordblocker.json"):	 	
    with open('wordblocker.json', encoding='utf-8') as m:
        blocked = json.load(m)
else:
    blocked = {}
    blocked['global'] = []
    with open('wordblocker.json', 'w') as f:
        json.dump(blocked, f, indent=4)
	


	
		
reddit = praw.Reddit(client_id='CFfgp9jESrgbLA',
                     client_secret='HZhSLIsgRMlgP379vA_7YNHQdaU',
                     user_agent='windows:com:Neko Public:reddit.3.22.0(by /u/<MuffinAmor88919>)')		
		
bot = commands.Bot(command_prefix='ng!')

botcolor = 0x00ff06

bot.remove_command('help')

class chat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
########################################################################################################################
        with open('users.json', 'r') as f:
            self.users = json.load(f)

    @commands.Cog.listener()
    @commands.cooldown(3, 30, commands.BucketType.user)
    async def on_message(self, message):
        with open('rank.json', encoding='utf-8') as r:
            rank = json.load(r)
        with open('wordblocker.json', encoding='utf-8') as m:
            blocked = json.load(m)
        if message.author.bot==False:
            start = time.time()		
            server = message.guild
            msg = message.content
            author_id = str(message.author.id)
            liste = ""
            for a in rank['dev']:
                if str(message.author.id) in a['id']:
                    dev = "yes"
                    break
            else:
                dev = ""

            for b in rank['lmod']:
                if str(message.author.id) in b['id']:
                    lmod = "yes"
                    break
            else:
                lmod = ""

            for c in rank['mod']:
                if str(message.author.id) in c['id']:
                    mod = "yes"
                    break
            else:
                mod = ""

            for d in rank['pmod']:
                if str(message.author.id) in d['id']:
                    pmod = "yes"
                else:
                    pmod = ""
 
            for e in rank['partner']:
                if str(message.guild.id) in e['id']:
                    partner = "yes"
                    break
            else:
                partner = ""  

            for f in rank['banned']:
                if str(message.author.id) in f['id']:
                    blocks = "yes"
                    break
            else:
                blocks = ""

            for i in blocked['global']:
                wordlist = list(i['words'])
                for word in wordlist:
                    if word in message.content:
                        blacklist = "yes"
                        break
                else:
                    blacklist = "lol"
                break
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
                name = message.author.name
                avatar = message.author.avatar_url
                guild = message.author.guild
                uid = message.author.id
                color = message.author.color
                spam = await message.channel.history().get(author__id=message.author.id)
                sek = time.time()
                try:
                    ins = self.bot.get_guild(382290709249785857)
                    inv = await ins.invites()
                    for invites in inv:
                        invite = invites.url
                        break
                except:
                    invite = "No access to Invite"
                try:
                    inv = await message.guild.invites()
                    for invites in inv:
                        invite2 = invites.url
                        break
                except:
                    invite2 = "No access to Invite"
                vote = "https://top.gg/bot/631149351112146957/vote"
                binv = "https://discordapp.com/api/oauth2/authorize?client_id=631149405965385759&permissions=388305&redirect_uri=https%3A%2F%2Fdiscord.gg&scope=bot"
                if not author_id in self.users:
                    self.users[author_id] = {}
                    self.users[author_id]['time'] = 1
                    with open('users.json', 'w') as f:
                        json.dump(self.users, f, indent=4)
                i = sek - get_time(author_id)
                try:
                    if dev == "yes":
                        for a in gc['global']:
                            id = ' '.join(a['channelid'])
                            channel = self.bot.get_channel(int(id))
                            if channel:
                                try:
                                    self.users[author_id]['time'] = time.time()
                                    with open('users.json', 'w') as f:
                                        json.dump(self.users, f, indent=4)
                                    embed=discord.Embed(
                                        color=color)
                                    embed.add_field(name='<:Neko_Logo:549531102117625866>Developer | {0}<:Neko_Logo:549531102117625866>'.format(name), value="{}\n\n[Support]({}) | [Bot Invite]({}) | [Vote](https://top.gg/bot/631149351112146957/vote)".format(msg, invite, binv), inline=False)
                                    embed.timestamp = datetime.utcnow()
                                    embed.set_footer(text='Network Developer', icon_url=avatar)
                                    embed.set_thumbnail(url=avatar)
                                    await channel.send(embed=embed)
                                except HTTPError as e:
                                    if e.code == 403:   
                                        try:
                                            await channel.send("DEV | {}\n>>>{}".format(name, msg)) 
                                        except:
                                            pass
                                except Exception as error:
                                    try:
                                        e = self.bot.get_channel(617779357829562368)
                                        embed=discord.Embed(
                                            color=message.author.color)
                                        embed.add_field(name='Fail message from **{}**'.format(a['name']), value="```python\n{}```".format(error), inline=False)
                                        embed.timestamp = datetime.utcnow()
                                        embed.set_thumbnail(url=self.bot.user.avatar_url)
                                        embed.set_footer(text=a['id'], icon_url=avatar)
                                        await e.send(embed=embed)
                                    except:
                                        pass
                    elif round(i * 1000) < 3000: 
                        try:
                            await message.delete()
                        except Exception as error:
                            pass
                        embed=discord.Embed(title='🚫Spam Alert🚫', description="Hello {},\nPlease be gentle and calm down with your message speed.".format(message.author.mention), color=0xff0000)
                        embed.timestamp = datetime.utcnow()
                        embed.set_footer(text=message.author.id, icon_url=avatar)
                        sysmsg = await message.channel.send(embed=embed)  
                    elif blocks == "yes":
                        try:
                            await message.delete()
                        except Exception as error:
                            pass
                        embed=discord.Embed(title='🚫System Alert🚫', description="Hello {},\nYou are blocked from the Network channel.\nYou can contact the Bot Staff Team to appeal the ban".format(message.author.mention), color=0xff0000)
                        embed.timestamp = datetime.utcnow()
                        embed.set_footer(text=message.author.id, icon_url=avatar)
                        sysmsg = await message.channel.send(embed=embed)
                    elif blacklist == "yes":
                        try:
                            await message.delete() 
                        except Exception as error:
                            pass
                        embed=discord.Embed(title='🚫System Alert🚫', description="Hello {},\nA word in your message is blocked from the Global chat.\nYour message is not send".format(message.author.mention), color=0xff0000)
                        embed.timestamp = datetime.utcnow()  
                        embed.set_footer(text=message.author.id, icon_url=avatar)
                        sysmsg = await message.channel.send(embed=embed)
                    elif lmod == "yes":
                        for a in gc['global']:
                            id = ' '.join(a['channelid'])
                            channel = self.bot.get_channel(int(id))
                            if channel:
                                try:
                                    self.users[author_id]['time'] = time.time()
                                    with open('users.json', 'w') as f:
                                        json.dump(self.users, f, indent=4)
                                    embed=discord.Embed(title='🛡 LMOD | {0} 🛡'.format(name), description="{}\n\n[Support]({}) | [Server Invite]({}) | [Vote]({})".format(msg, invite, invite2, vote), color=color)
                                    embed.timestamp = datetime.utcnow()
                                    embed.set_footer(text="Global Chat Moderator", icon_url=avatar)
                                    embed.set_thumbnail(url=avatar)
                                    await channel.send(embed=embed)
                                except HTTPError as e:
                                    if e.code == 403:   
                                        try:
                                            await channel.send("LMOD | {}\n>>>{}".format(name, msg)) 
                                        except:
                                            pass
                                except Exception as error:
                                    pass
                    elif mod == "yes":
                        for a in gc['global']:
                            id = ' '.join(a['channelid'])
                            channel = self.bot.get_channel(int(id))
                            if channel:
                                try:
                                    self.users[author_id]['time'] = time.time()
                                    with open('users.json', 'w') as f:
                                        json.dump(self.users, f, indent=4)
                                    embed=discord.Embed(title='🛡 Moderator | {0} 🛡'.format(name), description="{}\n\n[Support]({}) | [Server Invite]({}) | [Vote]({})".format(msg, invite, invite2, vote), color=0x18bd51)
                                    embed.timestamp = datetime.utcnow()
                                    embed.set_footer(text="Global Chat Moderator", icon_url=avatar)
                                    embed.set_thumbnail(url=avatar)
                                    await channel.send(embed=embed)
                                except HTTPError as e:
                                    if e.code == 403:   
                                        try:
                                            await channel.send("MOD | {}\n>>>{}".format(name, msg)) 
                                        except:
                                            pass
                                except Exception as error:
                                    print(error)                
                    elif pmod == "yes":
                        for a in gc['global']:
                            id = ' '.join(a['channelid'])
                            channel = self.bot.get_channel(int(id))
                            if channel:
                                try:
                                    self.users[author_id]['time'] = time.time()
                                    with open('users.json', 'w') as f:
                                        json.dump(self.users, f, indent=4)
                                    embed=discord.Embed(title='🛡 PMOD | {0} 🛡'.format(name), description="{}\n\n[Support]({}) | [Server Invite]({}) | [Vote]({})".format(msg[0:1500], invite, invite2, vote), color=0x18bd51)
                                    embed.timestamp = datetime.utcnow()
                                    embed.set_footer(text="Global Chat Moderator", icon_url=avatar)
                                    embed.set_thumbnail(url=avatar)
                                    await channel.send(embed=embed)
                                except HTTPError as e:
                                    if e.code == 403:   
                                        try:
                                            await channel.send("PMOD | {}\n>>>{}".format(name, msg)) 
                                        except:
                                            pass
                                except Exception as error:
                                    pass
                    elif partner == "yes":
                        for a in gc['global']:
                            id = ' '.join(a['channelid'])
                            channel = self.bot.get_channel(int(id))
                            if channel:
                                try:
                                    self.users[author_id]['time'] = time.time()
                                    with open('users.json', 'w') as f:
                                        json.dump(self.users, f, indent=4)
                                    embed=discord.Embed(color=0xce2727) 
                                    embed.add_field(name='💎 {0} 💎| {1}'.format(guild, name), value="{}\n\n[Server Invite]({}) | [Vote]({})".format(msg[0:1000], invite2, vote), inline=False)
                                    embed.timestamp = datetime.utcnow()
                                    embed.set_footer(text=uid, icon_url=avatar)
                                    embed.set_thumbnail(url=avatar)
                                    await channel.send(embed=embed)
                                except HTTPError as e:
                                    if e.code == 403:   
                                        try:
                                            await channel.send("Partner: {} | {}\n>>>{}".format(guild, name, msg)) 
                                        except:
                                            pass
                                except Exception as error:
                                    pass
                    else:
                        for a in gc['global']:
                            id = ' '.join(a['channelid'])
                            channel = self.bot.get_channel(int(id))
                            if channel:
                                try:
                                    self.users[author_id]['time'] = time.time()
                                    with open('users.json', 'w') as f:
                                        json.dump(self.users, f, indent=4)
                                    embed=discord.Embed(title='{0} | {1}'.format(guild, name), description="{}\n\n[Supportserver]({}) | [Vote]({})".format(msg[0:500], invite, vote), color=color) 
                                    embed.timestamp = datetime.utcnow()
                                    embed.set_footer(text=uid, icon_url=avatar)
                                    embed.set_thumbnail(url=avatar)
                                    await channel.send(embed=embed)
                                    await asyncio.sleep(0.5)
                                except HTTPError as e:
                                    if e.code == 403:   
                                        try:
                                            await channel.send("{} | {}\n>>>{}".format(guild, name, msg)) 
                                        except:
                                            pass
                                except Exception as error:
                                    pass
                    try:
                        await message.delete()
                    except Exception as e:
                        print(e)
                    duration = time.time() - start
                    du = round(duration * 1000)
                    c = self.bot.get_channel(608971311234154497)
                    try:
                        await c.edit(topic="Chatresponse: {} ms | Last Message from: {}".format(du, message.author.name))
                    except Exception as error:
                        print(error)
                except Exception as error:
                    print(error)
                print("{}>>    {}".format(message.author.id, msg))
                if dev == "yes":
                    money = 100 
                    user_add_credits(str(message.author.id), money)
                elif lmod == "yes":
                    money = 80
                    user_add_credits(str(message.author.id), money)
                elif mod == "yes":
                    money = 60
                    user_add_credits(str(message.author.id), money)
                elif pmod == "yes":
                    money = 45
                    user_add_credits(str(message.author.id), money)
                elif partner == "yes":
                    money = 40
                    user_add_credits(str(message.author.id), money) 
                else:
                    money = 10
                    user_add_credits(str(message.author.id), money)  	
                try:
                    await asyncio.sleep(7)
                    await sysmsg.delete()
                except:
                    pass				
###############################################################################################################

    @commands.command(pass_context = True)
    @commands.has_permissions(administrator=True)
    async def setchannel(self, ctx, setchannel:discord.TextChannel=None):
        if ctx.message.author.bot==False:
            guild = ctx.message.guild
            channel = setchannel or ctx.message.channel
            channel_id = str(channel.id)
            for current_global in gc['global']:
                if current_global['id'] == guild.id:
                    current_global['channelid'].clear()
                    current_global['channelid'].append(channel_id)
                    break
            else:
                gc['global'].append({
                'name':guild.name,
                'id':guild.id,
                'channelid': [channel_id]
                })
            with open('chat.json','w+') as w:
                json.dump(gc,w, indent=4)
                embed = discord.Embed(title="Welcome in the Lucy Network", description='The Channel {} has been set as Globalchat'.format(channel.mention), color=ctx.author.color)
                embed.add_field(name='Happy to chat with you', value='Hello and Welcome. Have a great time with us', inline='False')
                embed.set_thumbnail(url=ctx.guild.icon_url)
                embed.set_footer(text=ctx.guild.id, icon_url=ctx.guild.icon_url)
                embed.timestamp = datetime.utcnow()
                await ctx.channel.send(embed=embed)



    @commands.command(pass_context = True)
    @commands.has_permissions(administrator=True)
    async def clearchannel(self, ctx):
        if ctx.message.author.bot==False:
            guild = ctx.message.guild
            active = 'False'
            for current_global in gc['global']:
                if current_global['id'] == guild.id:
                    current_global['channelid'].clear()
                    current_global['channelid'].append("0000000000000000")
                    break
            with open('chat.json','w+') as w:
                json.dump(gc,w, indent=4)
                msg = await ctx.channel.send("The Globalchannel has been resetted")
##########################################################################################################################
def setup(bot):
    bot.add_cog(chat(bot))
