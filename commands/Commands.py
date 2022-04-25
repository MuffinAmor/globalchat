import discord
from discord import slash_command, Option
from discord.ext import commands

from lib.CacheHandler import config


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="info", description="Gibt dir Infos über einen Raum")
    async def info(self, ctx, room_name: Option(str, Options.room_named) = None):
        if not ctx.author.bot:
            target_room = room_name or RoomIdResolve(RankCheckIn(ctx.author.id).is_owner()).get_name()
            if target_room in room():
                room_data = room()[target_room]
                room_owner_data = room_data["owner"]
                room_owner = ""
                user = self.bot.get_user(room_owner_data)
                if user:
                    room_owner += user.name
                else:
                    room_owner += str(room_owner_data)
                room_roles = room_data["roles"]
                room_channels = len(room_data['channel']["data"])
                room_mods = ""
                for i in room_data["mods"]:
                    user = self.bot.get_user(i)
                    if user:
                        room_mods += f"{user.name}\n"
                    else:
                        room_mods += f"{i}" + "\n"
                if not room_mods:
                    room_mods = "Nobody"
                embed = discord.Embed(title=f"Infos über: {target_room}", color=discord.Color(config()["color"]))
                embed.add_field(name="Administrator:", value=room_owner, inline=False)
                embed.add_field(name="Moderatoren", value=room_mods, inline=False)
                if room_data["topic"]:
                    embed.add_field(name="Thema des Chatraums", value=room_data["topic"], inline=False)
                if room_data["language"]:
                    embed.add_field(name="Sprache", value=room_data["language"], inline=False)
                if room_data["description"]:
                    embed.add_field(name="Beschreibung", value=room_data["description"], inline=False)
                embed.add_field(name="Verknüpfte Kanäle", value=room_channels, inline=False)
                await ctx.respond(embed=embed)
            else:
                await ctx.respond("Entweder habe ich keine Daten gefunden oder du administrierst"
                                  " keinen Chatraum.")

    @slash_command(name="botinfo", description="Infos über den Bot")
    async def botinfo(self, ctx):
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
            channel_info = ChannelChecker(channel.id).return_for_system_cache()
            if channel_info:
                embed.add_field(name="Chatraum:", value=channel_info)
            await ctx.respond(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def say(self, ctx, *msg: str):
        await ctx.message.delete()
        await ctx.send(' '.join(msg))


def setup(bot):
    bot.add_cog(Commands(bot))
