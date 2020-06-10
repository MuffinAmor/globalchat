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
		
bot = commands.Bot(command_prefix='ng!')

botcolor = 0x00ff06

bot.remove_command('help')

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
		

		
		
    @bot.command()
    async def help(self, ctx):
        if ctx.author.bot==False:
            with open('rank.json', encoding='utf-8') as r:
                rank = json.load(r)		
            embed=discord.Embed(
                color=ctx.author.color)
            embed.set_author(name='Global Chat Help Menu')
            embed.add_field(name='❓', value='Open the Member Help Menu', inline='False')
            embed.add_field(name='📁', value='Open Server Admin Commands', inline='False')
            for a in rank['dev']:
                if str(ctx.author.id) in a['id']:         
                    embed.add_field(name='🖱', value='Open Chat Developer Commands', inline='False')
            for a in rank['lmod']:
                if str(ctx.author.id) in a['id']:      
                    embed.add_field(name='🗡', value='Open Leading Chat Moderator Commands', inline='False')	
            for a in rank['mod']:
                if str(ctx.author.id) in a['id']:         
                    embed.add_field(name='🛡', value='Open Chat Moderator Commands', inline='False')
            for a in rank['manager']:
                if str(ctx.author.id) in a['id']:         
                    embed.add_field(name='🌟', value='Open VIP Manager Commands', inline='False')
            embed.add_field(name='🔙', value='Go back to this site', inline='False')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/522437022095245313/546359964101509151/Neko_Logo.png')			
            embed.set_footer(text='Do you need help? ng!support')
            embed.timestamp = datetime.utcnow()
            msg = await ctx.channel.send(embed=embed)
            await msg.add_reaction("❓")
            await msg.add_reaction("📁")
            for a in rank['dev']:
                if str(ctx.author.id) in a['id']: 					
                    await msg.add_reaction("🖱")	
            for a in rank['lmod']:
                if str(ctx.author.id) in a['id']: 					
                    await msg.add_reaction("🗡")	
            for a in rank['mod']:
                if str(ctx.author.id) in a['id']:            
                    await msg.add_reaction("🛡")
            for a in rank['manager']:
                if str(ctx.author.id) in a['id']:            
                    await msg.add_reaction("🌟")
            await msg.add_reaction("🔙")
		
			
			
    
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        with open('rank.json', encoding='utf-8') as r:
            rank = json.load(r)
        if reaction.message.author.id == 631149351112146957:
            if user.bot == False:
                if reaction.emoji == "❓":
                    embed=discord.Embed(
                        color=user.color)
                    embed.set_author(name='Global Chat Help Menu')
                    embed.add_field(name='ng!info', value='Give you some Bot infos', inline='False')
                    embed.add_field(name='ng!support', value='Send a Link for our Support Server where you find help', inline='False')
                    embed.add_field(name='ng!botinv', value='Shows you the Botinvite', inline='False')
                    embed.add_field(name='ng!globalinfo', value='Shows you the Rules and Global Chat Infos', inline='False')
                    embed.add_field(name='ng!money', value='Shows you your current Level', inline='False')
                    embed.add_field(name='ng!slots *number*', value='Play with your money and win!', inline='False')
                    embed.add_field(name='🔙', value='Go back to navigation site', inline='False')
                    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/522437022095245313/546359964101509151/Neko_Logo.png')			
                    embed.set_footer(text='Do you need help? ng!support')
                    await reaction.message.edit(embed=embed)
                    await reaction.message.remove_reaction("❓", user)
                if reaction.emoji == "📁":
                    embed=discord.Embed(
                        color=user.color)
                    embed.set_author(name='Server Admin Help Menu')
                    embed.add_field(name='ng!setchannel *channelname*', value='Set the Globalchannel in the tagged channel', inline='False')
                    embed.add_field(name='ng!clearchannel', value='Disable the Globalchannel in your server', inline='False')
                    embed.add_field(name='ng!leave', value='The Bot leave your server', inline='False')
                    embed.set_footer(text='Do you need help? ng!support')
                    embed.timestamp = datetime.utcnow()						
                    embed.add_field(name='🔙', value='Go back to navigation site', inline='False')
                    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/522437022095245313/546359964101509151/Neko_Logo.png')			
                    embed.set_footer(text='Do you need help? ng!support')
                    await reaction.message.edit(embed=embed)
                    await reaction.message.remove_reaction("📁", user)
                if reaction.emoji == "🖱":
                    for a in rank['dev']:
                        if str(user.id) in a['id']: 
                            embed=discord.Embed(
                                color=user.color)
                            embed.set_author(name='Chat Developer Help Menu')
                            embed.add_field(name='ng!findserver [id]', value='Give you the Informations about the ID servers. The Bot need a member of this servers', inline='False')
                            embed.add_field(name='ng!globalusercheck [id]', value='Check the mutual servers with this Bot', inline='False')
                            embed.add_field(name='ng!goodnight', value='send Neko sleep :zzz:', inline='False')
                            embed.add_field(name='ng!addrank *id* *[dev, lmod, partner, vipm]*', value='Give the User the Rank', inline='False')
                            embed.add_field(name='ng!removerank *id* *[dev, lmod, partner, vipm]*', value='Remove the User the Rank', inline='False')
                            embed.add_field(name='ng!leave', value='The bot leaves the message server :warning:', inline='False')
                            embed.add_field(name='ng!servers', value='list you a list with all server that the bot support', inline='False')
                            embed.add_field(name='🔙', value='Go back to navigation site', inline='False')
                            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/522437022095245313/546359964101509151/Neko_Logo.png')			
                            embed.set_footer(text='Do you need help? ng!support')
                            await reaction.message.edit(embed=embed)
                            await reaction.message.remove_reaction("🖱", user)
                if reaction.emoji == "🗡":
                    for a in rank['lmod']:
                        if str(user.id) in a['id']:                   
                            embed=discord.Embed(title="Leading Chat Moderator Commands",
                                color=user.color)
                            embed.add_field(name='ng!unban *userid*', value='Unban a user from the Globalchat', inline='False')
                            embed.add_field(name='🔙', value='Go back to navigation site', inline='False')
                            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/522437022095245313/546359964101509151/Neko_Logo.png')			
                            embed.set_footer(text='Do you need help? ng!support')
                            await reaction.message.edit(embed=embed)
                            await reaction.message.remove_reaction("🗡", user)
                if reaction.emoji == "🛡":
                    for a in rank['mod']:
                        if str(user.id) in a['id']: 
                            embed=discord.Embed(title="Chat Moderator Commands",
                                color=user.color)
                            embed.add_field(name='ng!ban *userid*', value='Ban a user from the Globalchat', inline='False')
                            embed.add_field(name='ng!abw *word*', value='Add a word to the Blacklist', inline='False')
                            #embed.add_field(name='ng!mute *id* *time*', value='Mute the User for a amount of time. Default: 30 min', inline='False')   
                            #embed.add_field(name='ng!unmute *id*', value='Unmute the User', inline='False')   
                            #embed.add_field(name='ng!infomute *id*', value='Gives you infos about the Muted Users', inline='False')   
                            embed.add_field(name='ng!dm *userid* *msg*', value='Sends the ID user a message from the Bot with your name', inline='False')
                            embed.add_field(name='ng!checkban *userid*', value='Check if a user is banned', inline='False')
                            embed.add_field(name='🔙', value='Go back to navigation site', inline='False')
                            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/522437022095245313/546359964101509151/Neko_Logo.png')			
                            embed.set_footer(text='Do you need help? ng!support')
                            await reaction.message.edit(embed=embed)
                            await reaction.message.remove_reaction("🛡", user)
                if reaction.emoji == "🌟":
                    for a in rank['manager']:
                        if str(user.id) in a['id']: 
                            embed=discord.Embed(title="VIP Manager Commands",
                                color=user.color)
                            embed.add_field(name='ng!addvip *id* *[vips, vip]*', value='Add a VIP server or user', inline='False')
                            embed.add_field(name='ng!removevip *id* *[vips, vip]*', value='Remove a VIP server or user', inline='False')   
                            embed.add_field(name='🔙', value='Go back to navigation site', inline='False')
                            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/522437022095245313/546359964101509151/Neko_Logo.png')			
                            embed.set_footer(text='Do you need help? ng!support')
                            await reaction.message.edit(embed=embed)
                            await reaction.message.remove_reaction("🌟", user)
                if reaction.emoji == "🔙":
                    embed=discord.Embed(
                        color=user.color)
                    embed.set_author(name='Global Chat Help Menu')
                    embed.add_field(name='❓', value='Open the Member Help Menu', inline='False')
                    embed.add_field(name='📁', value='Open Server Admin Commands', inline='False')
                    for a in rank['dev']:
                        if str(user.id) in a['id']:         
                            embed.add_field(name='🖱', value='Open Chat Developer Commands', inline='False')
                    for a in rank['lmod']:
                        if str(user.id) in a['id']:      
                            embed.add_field(name='🗡', value='Open Leading Chat Moderator Commands', inline='False')	
                    for a in rank['mod']:
                        if str(user.id) in a['id']:         
                            embed.add_field(name='🛡', value='Open Chat Moderator Commands', inline='False')
                    for a in rank['manager']:
                        if str(user.id) in a['id']:         
                            embed.add_field(name='🌟', value='Open VIP Manager Commands', inline='False')
                    embed.add_field(name='🔙', value='Go back to this site', inline='False')
                    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/522437022095245313/546359964101509151/Neko_Logo.png')			
                    embed.set_footer(text='Do you need help? ng!support')
                    embed.timestamp = datetime.utcnow()
                    await reaction.message.edit(embed=embed)
                    await reaction.message.remove_reaction("🔙", user)

                
def setup(bot):
    bot.add_cog(help(bot))