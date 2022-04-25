from datetime import datetime

import discord
from discord.ext import commands

from lib.general import add_user
from lib.general import is_rank
from lib.general import list_rank
from lib.general import remove_user

bot = commands.Bot(command_prefix='ng!')

botcolor = 0x00ff06

bot.remove_command('help')


class rank(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @is_rank('developer')
    async def addrank(self, ctx, id, *i):
        rank = ''.join(i)
        if not ctx.message.author.bot:
            await ctx.send(add_user(str(id), str(rank)))

    @commands.command()
    @is_rank('developer')
    async def removerank(self, ctx, id, *i):
        rank = ''.join(i)
        if not ctx.message.author.bot:
            await ctx.send(remove_user(str(id), str(rank)))

    @commands.command()
    async def rankuser(self, ctx, rank):
        if not ctx.author.bot:
            lmao = ""
            l = list_rank(rank)
            for i in l:
                member = self.bot.get_user(int(i))
                if member == None:
                    lmao += i
                else:
                    lmao += "{} | {}\n".format(member, member.id)
            if lmao == "":
                lmao = "Unbesetzt"
            embed = discord.Embed(title=rank, description=lmao, color=ctx.author.color)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text=rank, icon_url=ctx.message.author.avatar_url)
            await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(rank(bot))
