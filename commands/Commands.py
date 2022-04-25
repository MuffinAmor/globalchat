import discord
from discord import slash_command, Option
from discord.ext import commands

from lib.CacheHandler import config, message_cache, channels
from lib.Things import ChannelHandler


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_guild_permissions(manage_channels=True)
    @slash_command(name="set_channel", description="Setze deinen Globalen Channel")
    async def set_channel(self, ctx, channel: discord.TextChannel = None):
        if not ctx.author.bot:
            channel = channel or ctx.channel
            ChannelHandler(ctx.guild.id, channel).set_channel()
            channels.cache_clear()
            await ctx.respond(f"{channel.name} wurde erfolgreich als Globalchannel gesetzt.")

    @commands.has_guild_permissions(manage_channels=True)
    @slash_command(name="remove_channel", description="Entferne den Globalchat von einem Server.")
    async def remove_channel(self, ctx):
        if not ctx.author.bot:
            ChannelHandler(ctx.guild.id).remove_channel()
            channels.cache_clear()
            await ctx.respond(f"Der Globalchat wurde entfernt.")

    @slash_command(name="botinfo", description="Infos über den Bot")
    async def botinfo(self, ctx):
        if not ctx.author.bot:
            l = list(permi for permi, value in ctx.guild.me.guild_permissions if str(value) == 'True')
            i = '\n📍 '.join(l)
            if "administrator" in i:
                i = "administrator"
            embed = discord.Embed(title="{}'s info".format(self.bot.user.name), color=discord.Color(config()["color"]))
            embed.add_field(name="Name", value=self.bot.user, inline=True)
            embed.add_field(name="Server", value=len(self.bot.guilds))
            embed.add_field(name='Bot Berechtigung:', value='📍 {0}'.format(i), inline=False)
            embed.set_thumbnail(url=self.bot.user.avatar)
            await ctx.respond(embed=embed)

    @slash_command(name="invite", description="Erstelle dir einen Einladungslink für den Bot")
    async def invite(self, ctx):
        if not ctx.author.bot:
            permissions = discord.Permissions(137439341633)
            dinge = discord.utils.oauth_url(self.bot.user.id, permissions=permissions,
                                            scopes=("bot", "applications.commands"),
                                            disable_guild_select=False)
            embed = discord.Embed(title=f"Hier ist ein Einladungs Link für {self.bot.user.name}",
                                  description=f"[Klick mich!]({dinge})", color=discord.Color(config()["color"]))
            await ctx.respond(embed=embed)

    @slash_command(name="channelinfo", description="Lasse dir Infos über einen Channel geben.")
    async def channelinfo(self, ctx, channel: discord.TextChannel):
        if not ctx.author.bot:
            embed = discord.Embed(title="Channel Info", color=discord.Color(config()["color"]))
            embed.add_field(name="Name", value=channel.name, inline=False)
            embed.add_field(name='Channel ID:', value=channel.id, inline=False)
            embed.add_field(name='Topic:', value=channel.topic, inline=False)
            if ctx.guild.icon:
                embed.set_thumbnail(url=ctx.guild.icon.url)
            channel_info = channel.id in channels()
            if channel_info:
                embed.add_field(name="Globalchat", value="Ja")
            await ctx.respond(embed=embed)

    @slash_command(name="message_info", description="Lasse dir Infos Ã¼ber eine Nachricht ausgeben.")
    async def message_info(self, ctx, token: Option(str, "Token der Nachricht")):
        if not ctx.author.bot:
            message = message_cache
            if token in message:
                stuff = message[token]
                embed = discord.Embed(title=f"Infos Ã¼ber {token}",
                                      color=discord.Color(config()["color"]))
                embed.add_field(name="Author Name", value=stuff["author_name"], inline=False)
                embed.add_field(name="Author Name", value=stuff["author_id"], inline=False)
                embed.add_field(name="Geschrieben am:", value=stuff["timestamp"], inline=False)
                await ctx.reply(embed=embed)
            else:
                await ctx.reply("Diesen Token finde ich leider nicht.\n"
                                "Wahrscheinlich liegt dieser nicht mehr im Cache.")


def setup(bot):
    bot.add_cog(Commands(bot))
