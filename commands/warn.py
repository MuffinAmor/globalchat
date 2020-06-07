from check import is_mod
from check import is_lmod
import discord
from discord.ext import commands
from datetime import datetime
import asyncio
import json
import os



os.chdir(r'/home/niko/bot/rankdata')

if os.path.isfile("reports.json"):
    with open('reports.json', encoding='utf-8') as f:
        report = json.load(f)
else:
    report = {}
    report['users'] = []
    with open('reports.json','w+') as f:
        json.dump(report , f, indent=4)	

bot = commands.Bot(command_prefix='ng!')

botcolor = 0xfffe00

bot.remove_command('help')

class warn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
		
    @bot.command(pass_context = True)
    @is_mod()
    @commands.cooldown(3, 60, commands.BucketType.user)
    async def warn(self, ctx,  user:discord.User,  *reason:str):
        if not reason:
            msg = await ctx.send("Please provide a reason")
            return
        reason = ' '.join(reason)
        for current_user in report['users']:
            if current_user['id'] == str(user.id):
                current_user['reasons'].append(reason)
                break
        else:
            report['users'].append({
            'id':str(user.id),
            'reasons': [reason,]
            })
        with open('reports.json','w+') as f:
            json.dump(report,f, indent=4)
        neko_log = self.bot.get_channel(631251123751354379)
        embed = discord.Embed(description='{0} has been reported.'.format(user), color=botcolor)
        await ctx.send(embed=embed)
        for current_user in report['users']:
            if str(user.id) == current_user['id']:
                embed1 = discord.Embed(title="Warning".format(user.name), color=0xff0000)
                embed1.add_field(name="Author", value=ctx.message.author, inline=True)
                embed1.add_field(name="Author ID", value=ctx.message.author.id, inline=True)
                embed1.add_field(name="Warned User:", value="{} | {}".format(user.name, user.mention), inline=True)
                embed1.add_field(name="User ID", value=user.id, inline=True)
                embed1.add_field(name="Warned for:", value=reason, inline=True)
                embed1.add_field(name="Server", value=ctx.guild, inline=True)
                embed1.add_field(name="Warnings", value="{0} has been reported {1} times for:\n {2}".format(user.mention, len(current_user['reasons']),', '.join(current_user['reasons']) ), inline=False)
                embed1.set_thumbnail(url=user.avatar_url)
                msg = await neko_log.send(embed=embed1)
                break
        else:
            embed2 = discord.Embed(title="Warning".format(user.name),color=0xff0000)
            embed2.add_field(name="Author", value=ctx.message.author, inline=True)
            embed2.add_field(name="Author ID", value=ctx.message.author.id, inline=True)
            embed1.add_field(name="Warned User:", value="{} | {}".format(user.name, user.mention), inline=True)
            embed2.add_field(name="User ID", value=user.id, inline=True)
            embed2.add_field(name="Warned for:", value=reason, inline=True)
            embed2.add_field(name="Server", value=ctx.guild, inline=True)
            embed2.add_field(name="Warnings", value="{0} has never been reported".format(user.mention), inline=False)
            embed2.set_thumbnail(url=user.avatar_url)
            msg = await neko_log.send(embed=embed2)
			
    @bot.command(pass_context = True)
    @is_lmod()
    @commands.cooldown(3, 60, commands.BucketType.user)
    async def delwarns(self, ctx, user:discord.User):
        for current_user in report['users']:
            if current_user['id'] == str(user.id):
                current_user['reasons'].clear()
                current_user['reasons'].append("")
                break
        else:
            msg = ctx.send("Ops, i have no dates about this user")
        with open('reports.json','w+') as f:
            json.dump(report, f, indent=4)	
            msg = await ctx.send("The Warnings from {0} has been deleted".format(user.name))
########################################################################################################################
    @bot.command(pass_context = True)
    @is_mod()
    async def warnings(self, ctx, user:discord.User):
        for current_user in report['users']:
            if str(user.id) == current_user['id']:
                await ctx.send("{0} has been reported {1} times for:\n {2}".format(user.mention, len(current_user['reasons']),', '.join(current_user['reasons']) ))
                break
        else:
            await ctx.send("{0} has never been reported".format(user.name)) 
		
########################################################################################################################
    @bot.command(pass_context=True)
    async def finduser(self, ctx, Id:int):
        hi = self.bot.get_user(Id)
        for find in report['users']:
            if str(hi.id) == find['id']:
                embed = discord.Embed(title='__Discord ID finder__',
                                      description="Username: {0}\n"
                                                  "User ID: {1}\n" 
                                                  "Created at: {2}\n"
                                                  "{3} warnings for: {4}" .format(hi, Id, hi.created_at, len(find['reasons']), ', '.join(find['reasons'])),
                    color=botcolor)
                embed.set_thumbnail(url=hi.avatar_url)	
                embed.set_footer(text='Message was requested by {}'.format(ctx.message.author))
                embed.timestamp = datetime.utcnow()
                msg = await ctx.send(embed=embed)
                break  
        else:
                embed = discord.Embed(title='__Discord ID finder__', description='Username: {0}\n' 'User ID: {1}\n' 'Created at: {2}\n' 'No warnings'.format(hi, Id, hi.created_at), color=botcolor)
                embed.set_thumbnail(url=hi.avatar_url)	
                embed.set_footer(text='Message was requested by {}'.format(ctx.message.author))
                embed.timestamp = datetime.utcnow()
                msg = await ctx.send(embed=embed)
                   	
def setup(bot):
    bot.add_cog(warn(bot))