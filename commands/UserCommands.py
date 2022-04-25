from discord import slash_command
from discord.ext import commands

from lib.RankHandler import UserData


class UserCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="register", description="Registriere dich")
    async def register(self, ctx):
        if not ctx.author.bot:
            respond = UserData(ctx.author.id).register()
            if not respond:
                await ctx.respond("Wie es aussieht, bist du bereits registriert")
            else:
                await ctx.respond("Glückwunsch, du bist nun registriert.")




def setup(bot):
    bot.add_cog(UserCommands(bot))
