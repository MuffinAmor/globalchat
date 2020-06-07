from check import is_vale
import discord
from discord.ext import commands 
import asyncio
from datetime import datetime
import sys
import json
import os
 

os.chdir(r'/home/niko/bot/rankdata')

if os.path.isfile("serverlist.json"):	   
    with open('serverlist.json', encoding='utf8') as f:
        slist = json.load(f)
else:
    slist = {}
    slist['servers'] = []
    with open('serverlist.json', 'w+') as f:
        json.dump(slist, f, indent=4)			
			
bot = commands.Bot(command_prefix='ng!')

botcolor = 0xffffff

bot.remove_command('help')

pass_list = (319708364051316750)


class servers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @bot.command(pass_context = True)
    @is_vale()  
    async def gatherservers(self, ctx):	
        slist = {}
        slist['servers'] = []
        for server in self.bot.guilds:
            Bot = list(member.bot for member in server.members if member.bot is True) 
            user = list(member.bot for member in server.members if member.bot is False)
            member = list(member for member in server.members)
            disboard = list(member.bot for member in server.members if member.id ==302050872383242240)
            dbl = list(member.bot for member in server.members if member.id ==422087909634736160)
            discord_me = list(member.bot for member in server.members if member.id ==476259371912003597)
            for current_servers in slist['servers']:
                if current_servers['id'] == server.id:
                    pass
            if str(len(disboard))=="1":
                List1 = "Yes"
            else:
                List1 = "No"
            if str(len(dbl))=="1":
                List2 = "Yes"
            else:
                List2 = "No"
            if str(len(discord_me))=="1":
                List3 = "Yes"
            else:
                List3 = "No"
            if server.owner == None:
                slist['servers'].append({
                'name':server.name,
                'id':str(server.id),
                'Server Region':str(server.region), 
                'Usercount': str(len(member)),
                'Botcount': str(len(Bot)), 
                'Humancount': str(len(user)),
                'Serverowner': "None",
                'Sicherheitslevel': str(server.verification_level), 
                'Last Update': str(datetime.utcnow()),
                'Disboard': List1, 
                'DBL': List2,
                'Discord.me': List3
                })
            else:
                slist['servers'].append({
                'name':server.name,
                'id':str(server.id),
                'Server Region':str(server.region),
                'Usercount': str(len(member)),
                'Botcount': str(len(Bot)), 
                'Humancount': str(len(user)),
                'Serverowner': server.owner.name,
                'Sicherheitslevel': str(server.verification_level), 
                'Last Update': str(datetime.utcnow()),
                'Disboard': List1, 
                'DBL': List2,
                'Discord.me': List3
                })
        await asyncio.sleep(1)
        with open('serverlist.json', 'w+') as f:
            json.dump(slist, f, indent=4)
        msg = await ctx.channel.send("Gather Servers sucessfully")

 
		
		



def setup(bot):
    bot.add_cog(servers(bot))