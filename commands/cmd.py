from datetime import datetime

import discord
from discord.ext import commands

from lib.global_chat import request_global

bot = commands.Bot(command_prefix='')

botcolor = 0x00ff06

bot.remove_command('help')


class CommandClass(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.counter = 0

    @bot.command()
    async def info(self, ctx):
        if not ctx.author.bot:
            server_id = str(ctx.guild.id)
            channel_id = request_global('single', server_id)
            channel = self.bot.get_channel(int(channel_id))
            servers = list(self.bot.guilds)
            members = sum(len(s.members) for s in self.bot.guilds)
            embed = discord.Embed(title='Global Network Botinfo', color=ctx.author.color)
            embed.add_field(name='Botusers', value=str(members), inline=True)
            embed.add_field(name='Botservers', value=str(len(servers)), inline=True)
            embed.add_field(name='Your chatcolor:', value=ctx.author.color, inline=False)
            embed.add_field(name='Your chatname:', value=ctx.author.name, inline=True)
            embed.add_field(name='Your chatserver:', value=ctx.author.guild.name, inline=True)
            embed.add_field(name='Your Globalchannel:', value=channel.name, inline=True)
            embed.set_footer(text='Botinfo asked by {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            embed.set_thumbnail(url=ctx.author.guild.icon_url)
            await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(CommandClass(bot))
