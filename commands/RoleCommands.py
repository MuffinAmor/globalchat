import discord
from discord import SlashCommandGroup
from discord.ext import commands

from lib.CacheHandler import full_rank_check
from lib.CheckThings import is_owner, is_admin, is_team
from lib.RankHandler import EditRanks


class RoleCommands(commands.Cog):
    role = SlashCommandGroup("role", "Rollen ", guilds=[754413698277441566, 953061114617417728])
    add = role.create_subgroup("add", description=" hinzufügen", guild_ids=[754413698277441566, 953061114617417728])
    remove = role.create_subgroup("remove", description=" entfernen", guild_ids=[754413698277441566, 953061114617417728])

    def __init__(self, bot):
        self.bot = bot

    @commands.is_owner()
    @add.command(name="owner", description="Vergebe jemanden die Owner Rolle.")
    async def owner(self, ctx, member: discord.Member):
        if not ctx.author.bot:
            respond = EditRanks(member.id).add_owner()
            if respond == "a":
                await ctx.respond(f"{member.name} besitzt die Rolle bereits.")
            elif respond == "b":
                await ctx.respond("Der genannte Nutzer ist leider noch nicht registiert.")
            else:
                full_rank_check.cache_clear()
                await ctx.respond(f"{member.name} wurde die Rolle gegeben.")

    @commands.is_owner()
    @remove.command(name="owner", description="Entferne die Ownerrolle.")
    async def owner(self, ctx, member: discord.Member):
        if not ctx.author.bot:
            respond = EditRanks(member.id).remove_owner()
            if respond == "a":
                await ctx.respond(f"{member.name} besitzt die Rolle nicht.")
            elif respond == "b":
                await ctx.respond("Der genannte Nutzer ist leider noch nicht registiert.")
            else:
                full_rank_check.cache_clear()
                await ctx.respond(f"{member.name} wurde die Rolle entzogen.")

    @is_owner()
    @add.command(name="admin", description="Vergebe jemanden die Admin Rolle.")
    async def admin(self, ctx, member: discord.Member):
        if not ctx.author.bot:
            respond = EditRanks(member.id).add_admin()
            if respond == "a":
                await ctx.respond(f"{member.name} besitzt die Rolle bereits.")
            elif respond == "b":
                await ctx.respond("Der genannte Nutzer ist leider noch nicht registiert.")
            else:
                full_rank_check.cache_clear()
                await ctx.respond(f"{member.name} wurde die Rolle gegeben.")

    @is_owner()
    @remove.command(name="admin", description="Entferne die Adminrolle.")
    async def admin(self, ctx, member: discord.Member):
        if not ctx.author.bot:
            respond = EditRanks(member.id).remove_admin()
            if respond == "a":
                await ctx.respond(f"{member.name} besitzt die Rolle nicht.")
            elif respond == "b":
                await ctx.respond("Der genannte Nutzer ist leider noch nicht registiert.")
            else:
                full_rank_check.cache_clear()
                await ctx.respond(f"{member.name} wurde die Rolle entzogen.")

    @is_admin()
    @add.command(name="team", description="Vergebe jemanden die Team Rolle.")
    async def team(self, ctx, member: discord.Member):
        if not ctx.author.bot:
            respond = EditRanks(member.id).add_team()
            if respond == "a":
                await ctx.respond(f"{member.name} besitzt die Rolle bereits.")
            elif respond == "b":
                await ctx.respond("Der genannte Nutzer ist leider noch nicht registiert.")
            else:
                full_rank_check.cache_clear()
                await ctx.respond(f"{member.name} wurde die Rolle gegeben.")

    @is_admin()
    @remove.command(name="team", description="Entferne die Teamrolle.")
    async def team(self, ctx, member: discord.Member):
        if not ctx.author.bot:
            respond = EditRanks(member.id).remove_team()
            if respond == "a":
                await ctx.respond(f"{member.name} besitzt die Rolle nicht.")
            elif respond == "b":
                await ctx.respond("Der genannte Nutzer ist leider noch nicht registiert.")
            else:
                full_rank_check.cache_clear()
                await ctx.respond(f"{member.name} wurde die Rolle entzogen.")

    @is_team()
    @add.command(name="moderator", description="Vergebe jemanden die Moderator Rolle.")
    async def moderator(self, ctx, member: discord.Member):
        if not ctx.author.bot:
            respond = EditRanks(member.id).add_moderator()
            if respond == "a":
                await ctx.respond(f"{member.name} besitzt die Rolle bereits.")
            elif respond == "b":
                await ctx.respond("Der genannte Nutzer ist leider noch nicht registiert.")
            else:
                full_rank_check.cache_clear()
                await ctx.respond(f"{member.name} wurde die Rolle gegeben.")

    @is_team()
    @remove.command(name="moderator", description="Entferne die Moderatorrolle.")
    async def moderator(self, ctx, member: discord.Member):
        if not ctx.author.bot:
            respond = EditRanks(member.id).remove_moderator()
            if respond == "a":
                await ctx.respond(f"{member.name} besitzt die Rolle nicht.")
            elif respond == "b":
                await ctx.respond("Der genannte Nutzer ist leider noch nicht registiert.")
            else:
                full_rank_check.cache_clear()
                await ctx.respond(f"{member.name} wurde die Rolle entzogen.")

    @is_team()
    @add.command(name="partner", description="Vergebe jemanden die Partner Rolle.")
    async def partner(self, ctx, member: discord.Member):
        if not ctx.author.bot:
            respond = EditRanks(member.id).add_partner()
            if respond == "a":
                await ctx.respond(f"{member.name} besitzt die Rolle bereits.")
            elif respond == "b":
                await ctx.respond("Der genannte Nutzer ist leider noch nicht registiert.")
            else:
                full_rank_check.cache_clear()
                await ctx.respond(f"{member.name} wurde die Rolle gegeben.")

    @is_team()
    @remove.command(name="partner", description="Entferne die Partnerrolle.")
    async def partner(self, ctx, member: discord.Member):
        if not ctx.author.bot:
            respond = EditRanks(member.id).remove_partner()
            if respond == "a":
                await ctx.respond(f"{member.name} besitzt die Rolle nicht.")
            elif respond == "b":
                await ctx.respond("Der genannte Nutzer ist leider noch nicht registiert.")
            else:
                full_rank_check.cache_clear()
                await ctx.respond(f"{member.name} wurde die Rolle entzogen.")

    @is_team()
    @add.command(name="vip", description="Vergebe jemanden die Vip Rolle.")
    async def vip(self, ctx, member: discord.Member):
        if not ctx.author.bot:
            respond = EditRanks(member.id).add_vip()
            if respond == "a":
                await ctx.respond(f"{member.name} besitzt die Rolle bereits.")
            elif respond == "b":
                await ctx.respond("Der genannte Nutzer ist leider noch nicht registiert.")
            else:
                full_rank_check.cache_clear()
                await ctx.respond(f"{member.name} wurde die Rolle gegeben.")

    @is_team()
    @remove.command(name="vip", description="Entferne die Viprolle.")
    async def vip(self, ctx, member: discord.Member):
        if not ctx.author.bot:
            respond = EditRanks(member.id).remove_vip()
            if respond == "a":
                await ctx.respond(f"{member.name} besitzt die Rolle nicht.")
            elif respond == "b":
                await ctx.respond("Der genannte Nutzer ist leider noch nicht registiert.")
            else:
                full_rank_check.cache_clear()
                await ctx.respond(f"{member.name} wurde die Rolle entzogen.")


def setup(bot):
    bot.add_cog(RoleCommands(bot))
