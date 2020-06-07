from check import is_dev
import discord
from discord.ext import commands
import asyncio
import sys
import random
from datetime import datetime
import json
import os

os.chdir(r'/home/niko/bot/rankdata') 
		
if os.path.isfile("target.json"):	 	
    with open('target.json', encoding='utf-8') as r:
        mt = json.load(r)
else:
    mt = {}
    mt['user'] = []
    with open('target.json', 'w') as r:
        json.dump(mt, r, indent=4)

bot = commands.Bot(command_prefix='ts!')

botcolor = 0xffffff

bot.remove_command('help')

class partner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
		
    @commands.command()		
    async def target(self, ctx, id:int, channel:discord.TextChannel):
        if ctx.author.bot == True:
            return
        member = self.bot.get_user(id)
        for i in mt['user']:
            if str(id) in i['id']:
                await ctx.send("The Target has been already setted {}".format(member))
                if str(channel.id) in i['channel']:
                    i['channel'].clear()
                    i['channel'].append(str(channel.id))
                    await ctx.send("The Target has been already setted in the channel {}".format(channel.name))
        else:
            if ctx.author.bot == False:
                mt['user'].append({
                'id': [str(id), ], 
                'channel' : [str(channel.id)]
                })
                await ctx.send("The Target has been setted {}in the channel {}".format(member, channel.name))
        with open('target.json', 'w') as f:
            json.dump(mt, f, indent=4)
			
    @commands.command()
    @is_dev()	
    async def removetarget(self, ctx, id:int):
        member = self.bot.get_user(id)
        for i in mt['user']:
            if str(id) in i['id']:
                i['id'].clear()
                i['id'].append("none")
                i['channel'].clear()
                i['channel'].append("none")
                await ctx.send("The Target {} has been removed".format(member))
            if str(id) in i['id']:
                await ctx.send("The Target {} is not in the Databse".format(member))
        with open('target.json', 'w') as f:
            json.dump(mt, f, indent=4)
			
    @commands.command()		
    @is_dev()
    async def check(self, ctx): 
        if ctx.author.bot == True:
            return	
        channel = ""
        for i in mt['user']:
            for a in i['id']:
                channel = self.bot.get_user(int(a)) 
                channel += "{}\n".format(str(channel.name))
        embed = discord.Embed(title="Setted Targets", description=channel, color=ctx.author.color)
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)
		
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot==False:  
            for i in mt['user']:
                if str(message.author.id) in i['id']:
                    channel = ''.join(i['channel'])
                    id = int(channel)
                    c = self.bot.get_channel(id) 
                    if c:
                        embed=discord.Embed(title='Target User: {}'.format(message.author.name), description="**Server:**\n{} | {}\n**Channel:**\n{}\n**Message:**\n{}".format(message.guild, message.guild.id, message.channel, message.content), color=message.author.top_role.color) 
                        embed.timestamp = datetime.utcnow()
                        embed.set_footer(text='Target', icon_url=message.author.avatar_url)
                        embed.set_thumbnail(url=message.author.avatar_url)
                        await c.send(embed=embed)

		
		
def setup(bot):
    bot.add_cog(partner(bot))