import json
import os
import random
import string

from discord.ext import commands

rank_list = ['banned', 'vip']


def create():
    if not os.path.isfile("User"):
        try:
            os.mkdir("User")
        except:
            pass
    if not os.path.isfile("User/ranks.json"):
        data = {}
        for rank in rank_list:
            data[rank] = []
            with open("User/ranks.json", "w+") as fp:
                json.dump(data, fp, indent=4)
        else:
            return None
    else:
        with open("User/ranks.json", encoding="utf-8") as fp:
            data = json.load(fp)
        for i in data:
            if not i in rank_list:
                del i
                with open("User/ranks.json", "w+") as fp:
                    json.dump(data, fp, indent=4)
                print(f"{i} wurde entfernt.")
        for rank in rank_list:
            if not rank in data:
                data[rank] = []
                with open("User/ranks.json", "w+") as fp:
                    json.dump(data, fp, indent=4)
                print(f"{rank} wurde hinzugefügt.")


def add_user(id: str, rank: str):
    create()
    with open('User/ranks.json', encoding='utf-8') as fp:
        data = json.load(fp)
    if id in data[rank]:
        return "User ist bereits in als {} eingetragen.".format(rank)
    elif not rank in rank_list:
        return "Dieser Rang existiert nicht."
    else:
        data[rank].append(id)
        with open('User/ranks.json', "w+") as fp:
            json.dump(data, fp, indent=4)
        return "User wurde in die Datenbank eingetragen."


def remove_user(id: str, rank: str):
    create()
    with open('User/ranks.json', encoding='utf-8') as fp:
        data = json.load(fp)
    if not str(id) in data[rank]:
        return "User ist nicht als {} eingetragen.".format(rank)
    elif not str(rank) in rank_list:
        return "Dieser Rang existiert nicht."
    else:
        data[rank].remove(id)
        with open('User/ranks.json', "w+") as fp:
            json.dump(data, fp, indent=4)
        return "User wurde entfernt."


def is_rank(rank: str):
    def predicate(ctx):
        with open('User/ranks.json', encoding='utf-8') as fp:
            data = json.load(fp)
        return str(ctx.author.id) in data[rank]

    return commands.check(predicate)


def has_rank(id: str, rank):
    with open('User/ranks.json', encoding='utf-8') as fp:
        data = json.load(fp)
    if id in data[rank]:
        return True
    else:
        return False


def list_rank(rank: str):
    with open('User/ranks.json', encoding='utf-8') as fp:
        data = json.load(fp)
    liste = []
    for i in data[rank]:
        liste.append(i)
    return liste


######################################################################################################################


def get_token(n: int):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))

########################################################################################################################
