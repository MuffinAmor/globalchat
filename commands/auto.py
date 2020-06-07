import discord
from discord.ext import commands 
import asyncio
from datetime import datetime
import json
import os
import aiohttp

os.chdir(r'/home/niko/bot/rankdata')

bot = commands.Bot(command_prefix='ng!')

if os.path.isfile("chat.json"):	  
    with open('chat.json', encoding='utf-8') as w:
        gc = json.load(w)
else:
    gc = {}
    gc['global'] = []
    with open('chat.json', 'w') as f:
        json.dump(gc, f, indent=4)
		
botcolor = 0x00ffff

class auto(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)
        self.counter = 0000
########################################################################################################################
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        else:
            server = self.bot.get_guild(382290709249785857)
            try:
                inv = await server.invites()
            except:
                pass
            for invites in inv:
                if invites:
                    invite2 = invites.url
                    break
            else:
                invite2 = "https://discord.gg"
            channel = self.bot.get_channel(631241590987292692) 
            self.counter =+ 1
            await channel.send("*{}* keeps a error ```{}```".format(ctx.message.content, error))
            embed=discord.Embed(title="Ops, there is an error!", description="Error report Nr. {} after reset.".format(self.counter),
                color=botcolor)
            embed.add_field(name='Server:', value='{}'.format(ctx.message.guild), inline=True)
            embed.add_field(name='Command:', value='{}'.format(ctx.message.content), inline=False)
            embed.add_field(name='Error:', value="```python\n{}```".format(error), inline=False)
            embed.add_field(name='Problems?', value='Take a Picture of this message and contact us [here]({}).'.format(invite2), inline=True)
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            embed.set_footer(text='Error Message', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            await ctx.channel.send(embed=embed)		
#########################################################################################################################
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        if guild.id == 631057446701367310:
            return
        channel = self.bot.get_channel(631250327940759584)
        server_info1 = (datetime.now() - guild.created_at).days
        Bot = list(member.bot for member in guild.members if member.bot is True) 
        user = list(member.bot for member in guild.members if member.bot is False)
        embed=discord.Embed(
            color=botcolor)
        embed.add_field(name='<:Neko_Logo:549531102117625866>__Server Join__<:Neko_Logo:549531102117625866>', value='** **', inline=False)
        embed.add_field(name='Name:', value='{}'.format(guild.name), inline=True)
        embed.add_field(name='Server ID:', value='{}'.format(guild.id), inline=True)
        embed.add_field(name='Region:', value='{}'.format(guild.region), inline=True)
        embed.add_field(name='Membercount:', value='{} members'.format(guild.member_count), inline=True)
        embed.add_field(name='Botcount:', value='{} Bots'.format(str(len(Bot))), inline=True) 
        embed.add_field(name='Humancount:', value='{} users'.format(str(len(user))), inline=True)
        embed.add_field(name='Large Server:', value='{} (250+ member)'.format(guild.large), inline=True)
        embed.add_field(name='Serverowner:', value='{}'.format(guild.owner), inline=True)
        embed.add_field(name='Verifylevel:', value='{} '.format(guild.verification_level), inline=True)
        embed.add_field(name='Created at:', value='{}'.format("{} ({} days ago!)".format(guild.created_at.strftime("%d. %b. %Y %H:%M"), server_info1)), inline=  False)
        embed.set_thumbnail(url="{0}".format(guild.icon_url))
        embed.set_footer(text='New Serverjoin', icon_url=guild.icon_url)
        embed.timestamp = datetime.utcnow()
        await channel.send(embed=embed)
        for a in gc['global']:
            channelid = ' '.join(a['channelid'])
            numid = int(channelid)
            channel = self.bot.get_channel(numid)
            if channel:
                async with self.session.get("https://nekos.life/api/neko") as resp:
                    nekos = await resp.json()
                embed = discord.Embed(title="Serverjoin: ***{0}***".format(guild.name), color=0xff0000)
                embed.set_image(url=nekos['neko'])
                embed.set_footer(text='https://nekos.life')
                embed.timestamp = datetime.utcnow()
                await channel.send(embed=embed)
		
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        if guild.id == 631057446701367310:
            return
        channel1 = self.bot.get_channel(631250327940759584)
        embed = discord.Embed(title="",description="Lucy leaved *{0}*".format(guild.name), 
        color=discord.Color.blurple(),
        timestamp=datetime.utcnow())
        embed.set_thumbnail(url="{0}".format(guild.icon_url))
        embed.set_footer(text='This message was requested by Neko' )
        await channel1.send(embed=embed)
        for a in gc['global']:
            channelid = ' '.join(a['channelid'])
            numid = int(channelid)
            channel = self.bot.get_channel(numid)
            if channel:
                try:
                    embed = discord.Embed(title="Serverleave: ***{0}***".format(guild.name), color=0xff0000)
                    embed.set_image(url="https://cdn.discordapp.com/attachments/560579412333166612/616322928367239209/goodbye.jpg")
                    embed.set_footer(text='Leaved Server')
                    embed.timestamp = datetime.utcnow()
                    await channel.send(embed=embed)
                except:
                    pass
#        for a in gc['global']:
#            if str(guild.id) == a['id']:
#                del a['name']
#                del a['id'] 
#                del a['enable']
#                del a['channelid']
#                del a['channelname']
#                gc['global'].remove({})
#                with open('chat.json','w+') as w:
#                    json.dump(gc,w, indent=4)		
def setup(bot):
    bot.add_cog(auto(bot))