from discord.ext import commands

from lib.CacheHandler import full_rank_check
from lib.RankHandler import RankCheck


def is_owner():
    def predicate(ctx):
        return RankCheck(ctx.author.id).is_owner()

    return commands.check(predicate)


def is_admin():
    def predicate(ctx):
        ranks = full_rank_check()[ctx.author.id]
        return RankCheck(ctx.author.id).is_admin() or "owner" in ranks

    return commands.check(predicate)


def is_team():
    def predicate(ctx):
        ranks = full_rank_check()[ctx.author.id]
        return RankCheck(ctx.author.id).is_team() or "owner" in ranks or "admin" in ranks

    return commands.check(predicate)


def is_moderator():
    def predicate(ctx):
        ranks = full_rank_check()[ctx.author.id]
        return RankCheck(ctx.author.id).is_moderator() or "owner" in ranks or "admin" in ranks or "team" in ranks

    return commands.check(predicate)


def is_partner():
    def predicate(ctx):
        return RankCheck(ctx.author.id).is_partner()

    return commands.check(predicate)


def is_vip():
    def predicate(ctx):
        return RankCheck(ctx.author.id).is_vip()

    return commands.check(predicate)
