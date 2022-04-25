import discord
from discord import SlashCommandGroup
from discord.ext import commands

from lib.BlackList import BlacklistHandling
from lib.CacheHandler import blacklist as bl
from lib.CheckThings import is_moderator as is_mod


class ModerationCommands(commands.Cog):
    mod = SlashCommandGroup("mod", "Moderations Kommandos", guild_ids=[754413698277441566])

    def __init__(self, bot):
        self.bot = bot

    @is_mod()
    @mod.command(name="ban", description="Banne einen Nutzer")
    async def ban(self, ctx, user: discord.User):
        pass

    @is_mod()
    @mod.command(name="unban", description="Entbanne einen Nutzer")
    async def unban(self, ctx, user: discord.User):
        pass

    @is_mod()
    @mod.command(name="add_word", description="Füge ein Wort der Blacklist hinzu")
    async def add_word(self, ctx, word: str):
        if not ctx.author.bot:
            response = BlacklistHandling(word.lower()).add_word()
            if response == "a":
                bl.cache_clear()
                await ctx.respond(f"Das Wort {word.lower()} wurde auf die Blacklist hinzugefügt.", ephermal=True)
            else:
                await ctx.respond(f"Das Wort befindet sich bereits auf der Blacklist.", ephermal=True)

    @is_mod()
    @mod.command(name="remove_word", description="Entferne ein Wort von der Blacklist")
    async def remove_word(self, ctx, word: str):
        if not ctx.author.bot:
            response = BlacklistHandling(word.lower()).remove_word()
            if response == "a":
                bl.cache_clear()
                await ctx.respond(f"Das Wort {word.lower()} wurde von der Blacklist genommen.", ephermal=True)
            else:
                await ctx.respond(f"Das Wort befindet sich nicht auf der Blacklist.", ephermal=True)

    @is_mod()
    @mod.command(name="blacklist", description="Lasse dir die Liste zusenden")
    async def blacklist(self, ctx):
        pass

    @is_mod()
    @mod.command(name="identify", description="Warum wurde der Text geblockt?")
    async def identify(self, ctx, *text: str):
        pass


def setup(bot):
    bot.add_cog(ModerationCommands(bot))
