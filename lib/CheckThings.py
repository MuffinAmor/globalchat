from discord.ext import commands

from lib.RankHandler import RankCheck


def is_owner():
    def predicate(ctx):
        return RankCheck(ctx.author.id).is_owner()

    return commands.check(predicate)


def is_admin():
    def predicate(ctx):
        return RankCheck(ctx.author.id).is_admin()

    return commands.check(predicate)


def is_team():
    def predicate(ctx):
        return RankCheck(ctx.author.id).is_team()

    return commands.check(predicate)


def is_moderator():
    def predicate(ctx):
        return RankCheck(ctx.author.id).is_moderator()

    return commands.check(predicate)


def is_partner():
    def predicate(ctx):
        return RankCheck(ctx.author.id).is_partner()

    return commands.check(predicate)


def is_vip():
    def predicate(ctx):
        return RankCheck(ctx.author.id).is_vip()

    return commands.check(predicate)
