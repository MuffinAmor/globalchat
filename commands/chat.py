import time
from datetime import datetime

import discord
from discord.ext import commands

from lib.general import get_token
from lib.general import has_rank
from lib.global_chat import get_time, set_time, set_global, request_global, delete_global
from lib.pics import add_pic
from lib.wordblocker import blocked

bot = commands.Bot(command_prefix='')

botcolor = 0x00ff06

bot.remove_command('help')


class chat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            server_id = str(message.guild.id)
            chat_id = request_global("single", server_id)
            if chat_id:
                if str(chat_id) == str(message.channel.id):
                    await self.send_message(message)

    async def send_message(self, message):
        token = get_token(12)
        server = message.guild
        msg = message.content
        author_id = str(message.author.id)
        data = {}
        name = message.author.name
        avatar = message.author.avatar_url
        savatar = message.guild.icon_url
        guild = message.author.guild
        uid = str(message.author.id)
        color = message.author.color
        sek = time.time()
        server = message.guild
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
        if blocked(msg) or blocked(message.author.name):
            try:
                await message.delete()
            except Exception as e:
                print(e)
            embed = discord.Embed(title='🚫System Alert🚫',
                                  description="Hello {},\n"
                                              "A word in your message or your name is blocked "
                                              "from the Global chat.\n"
                                              "Your message is not send".format(
                                      message.author.mention), color=0xff0000)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text=message.author.id, icon_url=message.guild.icon_url)
            await message.channel.send(embed=embed)
            return
        binv = ""
        sinv = ""
        i = sek - float(get_time(author_id))
        if has_rank(str(author_id), 'banned'):
            try:
                await message.delete()
            except:
                pass
            embed = discord.Embed(title='🚫You are banned🚫',
                                  description="Hello {},\nYou are banned from this Chatroom.".format(
                                      message.author.mention), color=0xff0000)

            embed.set_footer(text=uid, icon_url=self.bot.user.avatar_url)
            await message.channel.send(embed=embed, delete_after=5)
            return
        elif round(i) < 3:
            try:
                print(round(i))
                await message.delete()
            except:
                pass
            embed = discord.Embed(title='🚫Spam Alert🚫',
                                  description="Hello {},\nPlease be gentle and calm down with your message speed.".format(
                                      message.author.mention), color=0xff0000)

            embed.set_footer(text=uid, icon_url=self.bot.user.avatar_url)
            await message.channel.send(embed=embed, delete_after=5)
            return
        elif len(message.attachments) != 0:
            ends = [".jpg", ".jpeg", ".jfif", ".png", ".gif", ".mp4", ".m4v", ".mov", ".mp3"]
            for pic in message.attachments:
                for end in ends:
                    if pic.filename.endswith(end):
                        embed = discord.Embed(title='{} | {}'.format(server, name),
                                              color=color)
                        embed.set_image(url=pic.url)

                        embed.set_footer(text="{} | {}\n".format(uid, token), icon_url=savatar)
        elif has_rank(uid, 'vip'):
            set_time(uid)
            embed = discord.Embed(title='VIP | {0}'.format(name),
                                  description="{}\n\n[Bot Invite]({}) | [Support]({}) | [Server]({})".format(
                                      msg, binv, sinv, invite2), color=0xffffff)
            embed.set_footer(text="{} | {}".format(guild, uid), icon_url=savatar)
            embed.set_thumbnail(url=avatar)
        else:
            set_time(uid)
            embed = discord.Embed(title='{0}'.format(name),
                                  description="{}\n\n[Bot Invite]({}) | [Support]({})".format(
                                      msg, binv, sinv), color=0xffffff)
            embed.set_footer(text="{} | {}".format(guild, uid), icon_url=savatar)
            embed.set_thumbnail(url=avatar)
        chat_list = request_global('list')
        for i in chat_list:
            channel = self.bot.get_channel(int(i))
            if channel:
                if len(message.attachments) != 0:
                    try:
                        msg = await channel.send(embed=embed)
                        data[str(i)] = str(msg.id)
                    except Exception as e:
                        pass
                else:
                    try:
                        await channel.send(embed=embed)
                    except Exception as e:
                        pass
        if data:
            add_pic(token, 'global', str(message.author.id), str(time.time()), data)
        await message.delete()
        print("{}>>    {}".format(message.author.id, msg))

    ###############################################################################################################

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setchannel(self, ctx, setchannel: discord.TextChannel = None):
        if not ctx.message.author.bot:
            server_id = str(ctx.guild.id)
            channel = setchannel or ctx.message.channel
            channel_id = str(channel.id)
            set_global(server_id, channel_id)
            embed = discord.Embed(title="Welcome",
                                  description='The Channel {} has been set as Globalchat'.format(
                                      channel.mention),
                                  color=ctx.author.color)
            embed.add_field(name='Happy to chat with you', value='Hello and Welcome. Have a great time with us',
                            inline=False)
            embed.set_thumbnail(url=ctx.guild.icon_url)
            embed.set_footer(text=ctx.guild.id, icon_url=ctx.guild.icon_url)

            await ctx.channel.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clearchannel(self, ctx):
        server_id = str(ctx.guild.id)
        delete_global(server_id)
        await ctx.channel.send("The Globalchannel has been resetted")


##########################################################################################################################
def setup(bot):
    bot.add_cog(chat(bot))
