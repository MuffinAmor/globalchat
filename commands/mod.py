from check import is_dev
from check import is_lmod
from check import is_mod
from check import is_vipm
from check import is_vale
import discord
from discord.ext import commands
import asyncio
import sys
import random
from datetime import datetime
from urllib.error import HTTPError
import json
import os
import praw

os.chdir(r'/home/niko/bot/rankdata')

if os.path.isfile("wordblocker.json"):	 	
    with open('wordblocker.json', encoding='utf-8') as r:
        blocked = json.load(r)
else:
    blocked = {}
    blocked['global'] = [] 
    blocked['global'].append({
    'word': ["discord.gg"]
    })
    with open('wordblocker.json', 'w') as r:
        json.dump(mt, r, indent=4)
		
bot = commands.Bot(command_prefix='ng!')

botcolor = 0x00ff06

bot.remove_command('help')

class mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @is_mod()
    async def dm(self, ctx, userid:int, *args:str):
        user = self.bot.get_user(userid)
        msg = ' '.join(args)
        if not userid:
            await ctx.send("Please provide a userid")
        if not args:
            await ctx.send("Please provide a reason")
        embed=discord.Embed(title="Moderator message from ***{0}***".format(ctx.author.name),
            color=ctx.author.color)
        embed.add_field(name='CSC message', value=msg, inline='False')
        embed.set_thumbnail(url=user.avatar_url)			
        embed.set_footer(text='Mod message')
        embed.timestamp = datetime.utcnow()
        await user.send(embed=embed)
        channel = self.bot.get_channel(631250581922775094)
        await channel.send(embed=embed)
        await ctx.author.send("The message has been send to {}".format(user.name))
        await ctx.send("Sending succesfully")


    @commands.command()
    @is_mod()
    async def ban(self, ctx, user_id:int):
        with open('rank.json', encoding='utf-8') as r:
            rank = json.load(r)
        if ctx.message.author.bot==False:
            for c in rank['banned']:
                if str(id) in c['id']:
                    try:
                        user = self.bot.get_user(user_id)
                    except:
                        user = user_id
                    embed = discord.Embed(description='The User **{0}** is allready in the Databank as Banned'.format(user), color=botcolor)
                    embed.timestamp = datetime.utcnow()
                    await ctx.channel.send(embed=embed)
                    break                        
                if not str(ctx.guild.id) in c['id']:
                    c['id'].append(str(user_id))
                    try:
                        user = self.bot.get_user(user_id)
                    except:
                        user = user_id
                    embed = discord.Embed(description='The User {0} has been added to Banned'.format(user), color=botcolor)
                    embed.timestamp = datetime.utcnow()
                    await ctx.channel.send(embed=embed)
                    break
            with open('rank.json', 'w') as r:
                json.dump(rank, r, indent=4)
            try:
                member = self.bot.get_user(user_id)
            except:
                member = user_id
            channel = self.bot.get_channel(631250810336182273)
            embed = discord.Embed(title="Userban: ***{0}***".format(member), color=0xff0000)
            embed.set_image(url="https://cdn.discordapp.com/attachments/560579412333166612/573892323923198002/unknown.png")
            embed.set_footer(text='Banned by {0}'.format(ctx.author.name))
            embed.timestamp = datetime.utcnow()
            await channel.send(embed=embed)
            embed1 = discord.Embed(description='{0} has been banned.'.format(member), color=botcolor)
            embed1.set_image(url="https://cdn.discordapp.com/attachments/560579412333166612/573892323923198002/unknown.png")
            embed.set_footer(text='Banned by {0}'.format(ctx.author.name))
            embed.timestamp = datetime.utcnow()
            await ctx.channel.send(embed=embed1)


    @commands.command()
    @is_lmod()
    async def unban(self, ctx, user_id:int):
        with open('rank.json', encoding='utf-8') as r:
            rank = json.load(r)
        if ctx.message.author.bot==False:
            for c in rank['banned']:
                if not str(id) in c['id']:
                    try:
                        user = self.bot.get_user(user_id)
                    except:
                        user = user_id
                    embed = discord.Embed(description='The User **{0}** is not in the Databank as Banned'.format(user), color=botcolor)
                    embed.timestamp = datetime.utcnow()
                    await ctx.channel.send(embed=embed)
                    break                        
                if str(ctx.guild.id) in c['id']:
                    c['id'].remove(str(user_id))
                    try:
                        user = self.bot.get_user(user_id)
                    except:
                        user = user_id
                    embed = discord.Embed(description='The User {0} has been unbanned'.format(user), color=botcolor)
                    embed.timestamp = datetime.utcnow()
                    await ctx.channel.send(embed=embed)
                    break
            with open('rank.json', 'w') as r:
                json.dump(rank, r, indent=4)

    @commands.command()
    @is_mod()
    async def checkban(self, ctx, user_id:int):
        with open('rank.json', encoding='utf-8') as r:
            rank = json.load(r)
        if ctx.message.author.bot==False:
            for c in rank['banned']:
                if str(id) in c['id']:
                    try:
                        user = self.bot.get_user(user_id)
                    except:
                        user = user_id
                    embed = discord.Embed(description='The User **{0}** is banned'.format(user), color=botcolor)
                    embed.timestamp = datetime.utcnow()
                    await ctx.channel.send(embed=embed)
                    break                        
                if not str(ctx.guild.id) in c['id']:
                    try:
                        user = self.bot.get_user(user_id)
                    except:
                        user = user_id
                    embed = discord.Embed(description='The User {0} is not banned'.format(user), color=botcolor)
                    embed.timestamp = datetime.utcnow()
                    await ctx.channel.send(embed=embed)
                    break











			
    @commands.command()
    @is_mod()
    async def abw(self, ctx, *word:str):
        if ctx.message.author.bot==False:
            if not word:
                msg = await ctx.channel.send("Please provide a word")
                await asyncio.sleep(10)
                await msg.delete()
                return
            bw = ' '.join(word)
            liste = ""
            for i in blocked['global']:
                liste += ' '.join(i['words'])
            if bw in liste:
                await ctx.send("This Word is allready in the Wordblocker")
            if not bw in liste:
                for i in blocked['global']:
                    i['words'].append(bw)
                await ctx.channel.send("The Word **{0}** has been added to the Wordblacklist".format(bw))
                channel = self.bot.get_channel(622414142246092841) 
                embed = discord.Embed(title="Wordblacklist Update",description='The Word **{0}** has been added to the Wordblacklist by **{1}**'.format(bw, ctx.message.author.name),color=botcolor)
                embed.timestamp = datetime.utcnow()
                embed.set_footer(text='Wordblacklist Update', icon_url=ctx.author.avatar_url)
                embed.set_thumbnail(url=self.bot.user.avatar_url)
                await channel.send(embed=embed)	
            with open('wordblocker.json','w+') as m:
                json.dump(blocked,m, indent=4)
	
    @commands.command()
    @is_mod()
    async def rbw(self, ctx, *word:str):
        if ctx.message.author.bot==False:
            if not word:
                msg = await ctx.channel.send("Please provide a word")
                await asyncio.sleep(10)
                await msg.delete()
                return
            bw = ' '.join(word)
            liste = ""
            for i in blocked['global']:
                liste += ' '.join(i['words'])
            if not bw in liste:
                await ctx.send("This Word is not in the Wordblocker")
            if bw in liste:
                for i in blocked['global']:
                    i['words'].remove(bw)
                await ctx.channel.send("The Word **{0}** has been removed from the Wordblacklist".format(bw))
                channel = self.bot.get_channel(622414142246092841) 
                embed = discord.Embed(title="Wordblacklist Update",description='The Word **{0}** has been removed from the Wordblacklist by **{1}**'.format(bw, ctx.message.author.name),color=botcolor)
                embed.timestamp = datetime.utcnow()
                embed.set_footer(text='Wordblacklist Update', icon_url=ctx.author.avatar_url)
                embed.set_thumbnail(url=self.bot.user.avatar_url)
                await channel.send(embed=embed)	
            with open('wordblocker.json','w+') as m:
                json.dump(blocked,m, indent=4)

	
    @commands.command()
    @is_mod()
    async def wbl(self, ctx):
        if ctx.message.author.bot==False:
            liste = ""
            for i in blocked['global']:
                liste += '\n'.join(i['words'])
            embed = discord.Embed(title="Wordblacklist", description=liste, color=botcolor)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            try:
                await ctx.author.send(embed=embed)
                await ctx.send("You have recieve a mail")
            except:
                await ctx.send("Ops, it looks like you have close your Direct messages.\nPlease open it, to recieve the List")



 
def setup(bot):
    bot.add_cog(mod(bot))