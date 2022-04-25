import discord
from discord import SlashCommandGroup, Option
from discord.ext import commands

from lib.RankHandler import EditRanks


class AdminCommands(commands.Cog):
    admin = SlashCommandGroup("admin", "Administrations commands")

    def __init__(self, bot):
        self.bot = bot


    '''@is_registered()
    @admin.command(name="remove_mod", description="Entferne einen Moderator aus deinem Chatraum")
    async def remove_mod(self, ctx, room_name: Option(str, Options.room_named), user: discord.User):
        if not ctx.author.bot:
            respond = EditRanks(room_name, ctx.author.id).remove_mod(user.id)
            if respond == "a":
                user_c.cache_clear()
                room.cache_clear()
                await ctx.respond(f"{user.name} wurde als Moderator aus dem Chatraum {room_name} entfernt")
            elif respond == "b":
                await ctx.respond("Dieser Nutzer ist nicht registiert.")
            elif respond == "c":
                await ctx.respond("Diese Person scheint kein Moderator zu sein.")
            else:
                await ctx.respond("Du hast wohl keine Berechtigung dazu")'''


'''    
    @is_registered()
    @admin.command(name="room_setup", description="Setze ein Thema und eine Beschreibung für deinen Chatraum!")
    async def room_setup(self, ctx, room_name: Option(str, Options.room_named)):
        if room()[room_name]:
            if room()[room_name]["owner"] == ctx.author.id:
                modal = MyModal(room_name)
                await ctx.interaction.response.send_modal(modal)
        else:
            await ctx.respond("Wie es aussieht, administrierst du diesen Chatraum nicht.")'''


def setup(bot):
    bot.add_cog(AdminCommands(bot))
