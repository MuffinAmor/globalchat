import discord.ui
from discord import slash_command
from discord.ext import commands

from Menu.HelpDrop import DropdownView
from Menu.Options import HelpMenuContent as HM
from lib.CacheHandler import config


class HelpMenu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="help", description="Gibt das Hilfe Menu aus")
    async def help(self, ctx):
        view = DropdownView()
        embed = discord.Embed(title="Command Übersicht", color=discord.Color(config()["color"]))
        embed.add_field(name="📄 Allgemeine Commands", value=HM.normal_desc, inline=False)
        embed.add_field(name=' \u200b', value=' \u200b', inline=False)
        embed.add_field(name="🛠 Setup Commands", value=HM.setup_desc)
        embed.add_field(name="💻 Administrations Commands", value=HM.admin_desc)
        embed.add_field(name=' \u200b', value=' \u200b', inline=False)
        embed.add_field(name="🛡 Moderations Commands", value=HM.mod_desc)
        embed.add_field(name="🔬 Anime Commands", value=HM.anime_desc)
        await ctx.respond(embed=embed, view=view)


def setup(bot):
    bot.add_cog(HelpMenu(bot))
