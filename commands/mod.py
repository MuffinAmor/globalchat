import asyncio
from datetime import datetime

import discord
from discord.ext import commands

from lib.general import add_user
from lib.general import remove_user
from lib.pics import request_pic_msg, remove_pic
from lib.serverban import add_server, remove_server, request_server
from lib.wordblocker import addword
from lib.wordblocker import blacklist
from lib.wordblocker import removeword

bot = commands.Bot(command_prefix='')

botcolor = 0x00ff06

bot.remove_command('help')


class mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def dm(self, ctx, userid: int, *args: str):
        user = self.bot.get_user(userid)
        msg = ' '.join(args)
        if not userid:
            await ctx.send("Please provide a userid")
        if not args:
            await ctx.send("Please provide a reason")
        embed = discord.Embed(title="Moderator message.", color=ctx.author.color)
        embed.add_field(name='CSC message', value=msg, inline=False)
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_footer(text='Mod message')
        embed.timestamp = datetime.utcnow()
        await user.send(embed=embed)
        await ctx.author.send("The message has been send to {}".format(user.name))
        await ctx.send("Sending succesfully")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, user_id: int):
        if not ctx.message.author.bot:
            await ctx.send(add_user(str(user_id), 'banned'))

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, user_id: int):
        if not ctx.message.author.bot:
            await ctx.send(remove_user(str(user_id), 'banned'))

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def abw(self, ctx, *word: str):
        if not ctx.message.author.bot:
            if not word:
                msg = await ctx.channel.send("Please provide a word")
                await asyncio.sleep(10)
                await msg.delete()
                return
            bw = ' '.join(word)
            await ctx.send(addword(bw))

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def rbw(self, ctx, *word: str):
        if not ctx.message.author.bot:
            if not word:
                msg = await ctx.channel.send("Please provide a word")
                await asyncio.sleep(10)
                await msg.delete()
                return
            bw = ' '.join(word)
            await ctx.send(removeword(bw))

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban_server(self, ctx, guild: int, *args: str):
        if not ctx.message.author.bot:
            reason = ' '.join(args)
            if not guild:
                await ctx.send("Bitte gebe die ID des Servers an, den du bannen willst.")
            elif reason == "":
                await ctx.send("Bitte gebe einen Grund zum bannen des Servers an.")
            else:
                await ctx.send(add_server(str(guild), reason))
                server = self.bot.get_guild(guild)
                if server:
                    await server.leave()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban_server(self, ctx, guild: int):
        if not ctx.message.author.bot:
            if not guild:
                await ctx.send("Bitte gebe die ID des Servers an, den du entbannen willst.")
            else:
                remove_server(str(guild))
                await ctx.send("Der Server wurde erfolgreich entfernt.")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def show_all_banned(self, ctx):
        if not ctx.author.bot:
            await ctx.send(request_server("all"))

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def wbl(self, ctx):
        if not ctx.message.author.bot:
            words = '\n'.join(blacklist())
            try:
                await ctx.author.send(words)
                await ctx.send("You have recieve a mail")
            except:
                await ctx.send(
                    "Ops, it looks like you have close your Direct messages.\n"
                    "Please open it, to recieve the List")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def del_pic(self, ctx, *args):
        token = ' '.join(args)
        msgs = request_pic_msg(token)
        msg = await ctx.send("Deleting in process...")
        if token == "":
            await msg.edit("Please insert the Picture Token, which you can find under the Picture.")
        elif msgs:
            for i in msgs:
                channel = self.bot.get_channel(int(i))
                if channel:
                    message = await channel.fetch_message(msgs[i])
                    if message:
                        try:
                            await message.delete()
                        except:
                            await ctx.send(
                                "I can't delete the Picture in {} .".format(channel.name))
                            pass
                    else:
                        await ctx.send(
                            "I can't delete the Picture in {} .".format(channel.name))
                else:
                    await ctx.send(
                        "I can't delete the Picture in {} .".format(channel.name))
            remove_pic(token)
            await msg.edit(content="The Picture with the Token {} has been deleted sucessfully".format(token))
        else:
            await msg.edit(content="A Picture with this Token is not found.")


def setup(bot):
    bot.add_cog(mod(bot))
