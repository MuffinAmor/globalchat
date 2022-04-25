import discord
from discord.ext import commands
import os
import json

os.chdir(r'/home/niko/bot/rankdata')
if not os.path.isfile("rank.json"):
    rank = {}
    rank['dev'] = []
    rank['dev'].append({
        'id': ["474947907913515019"]
    })
    rank['lmod'] = []
    rank['lmod'].append({
        'id': ["474947907913515019"]
    })
    rank['mod'] = []
    rank['mod'].append({
        'id': ["474947907913515019"]
    })
    rank['manager'] = []
    rank['manager'].append({
        'id': ["474947907913515019"]
    })
    rank['pmod'] = []
    rank['pmod'].append({
        'id': ["474947907913515019"]
    })
    rank['partner'] = []
    rank['partner'].append({
        'id': []
    })
    rank['vips'] = []
    rank['vips'].append({
        'id': []
    })
    rank['vip'] = []
    rank['vip'].append({
        'id': ["474947907913515019"]
    })
    rank['banned'] = []
    rank['banned'].append({
        'id': []
    })
    with open('rank.json', 'w') as f:
        json.dump(rank, f, indent=4)


def is_vale():
    def predicate(ctx):
        return ctx.author.id in [474947907913515019]

    return commands.check(predicate)


def is_dev():
    def predicate(ctx):
        with open('rank.json', encoding='utf-8') as r:
            rank = json.load(r)
        for a in rank['dev']:
            return str(ctx.author.id) in str(a['id'])

    return commands.check(predicate)


def is_lmod():
    def predicate(ctx):
        with open('rank.json', encoding='utf-8') as r:
            rank = json.load(r)
        for a in rank['lmod']:
            return str(ctx.author.id) in a['id']

    return commands.check(predicate)


def is_mod():
    def predicate(ctx):
        with open('rank.json', encoding='utf-8') as r:
            rank = json.load(r)
        for a in rank['mod']:
            return str(ctx.author.id) in a['id']

    return commands.check(predicate)


def is_vip():
    def predicate(ctx):
        with open('rank.json', encoding='utf-8') as r:
            rank = json.load(r)
        for a in rank['vip']:
            return str(ctx.author.id) in str(a['id'])

    return commands.check(predicate)


def is_vipm():
    def predicate(ctx):
        with open('rank.json', encoding='utf-8') as r:
            rank = json.load(r)
        for a in rank['manager']:
            return str(ctx.author.id) in a['id']

    return commands.check(predicate)


########################################################################################################################			
def get_xp(user_id: str):
    if os.path.isfile('users.json'):
        with open('users.json', 'r') as fp:
            users = json.load(fp)
        return users[user_id]['exp']
    else:
        return 0


########################################################################################################################
def get_lvl(user_id: str):
    if os.path.isfile('users.json'):
        with open('users.json', 'r') as fp:
            users = json.load(fp)
        return users[user_id]['level']
    else:
        return 0


########################################################################################################################
def get_time(user_id: str):
    if os.path.isfile('users.json'):
        with open('users.json', 'r') as fp:
            users = json.load(fp)
        return users[user_id]['time']
    else:
        return 0


########################################################################################################################

def user_add_credits(user_id: int, money: int):
    if os.path.isfile("money.json"):
        try:
            with open('money.json', 'r') as fp:
                credit = json.load(fp)
            credit[user_id]['money'] += money
            with open('money.json', 'w') as fp:
                json.dump(credit, fp, sort_keys=True, indent=4)
        except KeyError:
            with open('money.json', 'r') as fp:
                credit = json.load(fp)
            credit[user_id] = {}
            credit[user_id]['money'] = money
            with open('money.json', 'w') as fp:
                json.dump(credit, fp, sort_keys=True, indent=4)
    else:
        credit = {user_id: {}}
        credit[user_id]['money'] = money
        with open('money.json', 'w') as fp:
            json.dump(credit, fp, sort_keys=True, indent=4)


########################################################################################################################
def get_credits(user_id: int):
    if os.path.isfile('money.json'):
        with open('money.json', 'r') as fp:
            credit = json.load(fp)
        return credit[user_id]['money']
    else:
        return 0


########################################################################################################################
def user_remove_credits(user_id: int, money: int):
    if os.path.isfile("money.json"):
        try:
            with open('money.json', 'r') as fp:
                credit = json.load(fp)
            credit[user_id]['money'] -= money
            with open('money.json', 'w') as fp:
                json.dump(credit, fp, sort_keys=True, indent=4)
        except KeyError:
            with open('money.json', 'r') as fp:
                credit = json.load(fp)
            credit[user_id] = {}
            credit[user_id]['money'] = 0
            with open('money.json', 'w') as fp:
                json.dump(credit, fp, sort_keys=True, indent=4)
    else:
        credit = {user_id: {}}
        credit[user_id]['money'] = 0
        with open('money.json', 'w') as fp:
            json.dump(credit, fp, sort_keys=True, indent=4)
