from datetime import datetime

import aiohttp
import discord
from discord.ext import commands

from lib.global_chat import delete_global
from lib.serverban import request_server

bot = commands.Bot(command_prefix='')

botcolor = 0x00ffff


class auto(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        else:
            server = self.bot.get_guild(000)
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
            channel = self.bot.get_channel(000)
            await channel.send("*{}* keeps a error ```{}```".format(ctx.message.content, error))
            embed = discord.Embed(title="Ops, there is an error!",
                                  color=botcolor)
            embed.add_field(name='Server:', value='{}'.format(ctx.message.guild), inline=True)
            embed.add_field(name='Command:', value='{}'.format(ctx.message.content), inline=False)
            embed.add_field(name='Error:', value="```python\n{}```".format(error), inline=False)
            embed.add_field(name='Problems?',
                            value='Take a Picture of this message and contact us [here]({}).'.format(invite2),
                            inline=True)
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            embed.set_footer(text='Error Message', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            await ctx.channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        delete_global(str(guild.id))

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        server = request_server('single', str(guild.id))
        if server is True:
            await guild.leave()


def setup(bot):
    bot.add_cog(auto(bot))
