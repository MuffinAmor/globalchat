import discord
from discord import SlashCommandGroup
from discord.ext import commands

from lib.BlackList import BlacklistHandling
from lib.CacheHandler import blacklist as bl, config, full_rank_check
from lib.CheckThings import is_moderator as is_mod
from lib.RankHandler import EditRanks


class ModerationCommands(commands.Cog):
    mod = SlashCommandGroup("mod", "Moderations Kommandos", guild_ids=[754413698277441566])

    def __init__(self, bot):
        self.bot = bot

    @is_mod()
    @mod.command(name="ban", description="Banne einen Nutzer")
    async def ban(self, ctx, user: discord.User):
        if not ctx.author.bot:
            respond = EditRanks(user.id).ban_user()
            if respond == "a":
                await ctx.respond("Der Nutzer ist bereits gebannt.")
            elif respond == "b":
                await ctx.repsond("Dieser Nutzer ist leider nicht registriert.")
            else:
                full_rank_check.cache_clear()
                await ctx.respond(f"Der Nutzer {user} wurde erfolgreich gebannt.", ephemeral=True)

    @is_mod()
    @mod.command(name="unban", description="Entbanne einen Nutzer")
    async def unban(self, ctx, user: discord.User):
        if not ctx.author.bot:
            respond = EditRanks(user.id).unban_user()
            if respond == "a":
                await ctx.respond("Der Nutzer ist nicht gebannt.")
            elif respond == "b":
                await ctx.repsond("Dieser Nutzer ist leider nicht registriert.")
            else:
                full_rank_check.cache_clear()
                await ctx.respond(f"Der Nutzer {user} wurde erfolgreich entbannt.", ephemeral=True)

    @is_mod()
    @mod.command(name="add_word", description="Füge ein Wort der Blacklist hinzu")
    async def add_word(self, ctx, word: str):
        if not ctx.author.bot:
            response = BlacklistHandling(word.lower()).add_word()
            if response == "a":
                bl.cache_clear()
                await ctx.respond(f"Das Wort {word.lower()} wurde auf die Blacklist hinzugefügt.", ephemeral=True)
            else:
                await ctx.respond(f"Das Wort befindet sich bereits auf der Blacklist.", ephemeral=True)

    @is_mod()
    @mod.command(name="remove_word", description="Entferne ein Wort von der Blacklist")
    async def remove_word(self, ctx, word: str):
        if not ctx.author.bot:
            response = BlacklistHandling(word.lower()).remove_word()
            if response == "a":
                bl.cache_clear()
                await ctx.respond(f"Das Wort {word.lower()} wurde von der Blacklist genommen.", ephemeral=True)
            else:
                await ctx.respond(f"Das Wort befindet sich nicht auf der Blacklist.", ephemeral=True)

    @is_mod()
    @mod.command(name="blacklist", description="Lass dir die Blacklist zeigen")
    async def blacklist(self, ctx):
        if not ctx.author.bot:
            respond = bl()
            blacklist = ""
            for i in respond:
                blacklist += i + "\n"
            if respond:
                embed = discord.Embed(title=f"Blacklist",
                                      description=blacklist,
                                      color=discord.Color(config()["color"]))
                await ctx.respond(embed=embed, ephemeral=True)
            else:
                await ctx.respond("Du hast wohl keine Berechtigung dazu")

    @is_mod()
    @mod.command(name="identify", description="Warum wurde der Text geblockt?")
    async def identify(self, ctx, *text: str):
        pass


def setup(bot):
    bot.add_cog(ModerationCommands(bot))
