import json
from functools import lru_cache

from lib.RankHandler import UserData
from lib.sql import session_scope, GlobalTable, Ranks, Blacklist

message_cache = {}


def check_for_word(message):
    for i in message:
        if i.lower() in blacklist():
            return True


@lru_cache()
def blacklist():
    words = []
    with session_scope() as db_session:
        word_data = db_session.query(Blacklist)
        word_table = [p.dump() for p in word_data]
        print("[DATENBANK] >> User Cache wird geladen")
        for i in word_table:
            words.append(i['word'])
        return words


@lru_cache()
def users():
    user = []
    with session_scope() as db_session:
        user_data = db_session.query(Ranks)
        user_table = [p.dump() for p in user_data]
        print("[DATENBANK] >> User Cache wird geladen")
        for i in user_table:
            user.append(i['user_id'])
        return user


@lru_cache()
def channels():
    channel_cache = []
    with session_scope() as db_session:
        room_data = db_session.query(GlobalTable)
        room_table = [p.dump() for p in room_data]
        print("[DATENBANK] >> Channel Cache wird geladen")
        for i in room_table:
            channel_cache.append(i['channel_id'])

        return channel_cache


@lru_cache()
def full_rank_check() -> dict:
    user_dict = {}
    with session_scope() as db_session:
        role_data = db_session.query(Ranks)
        role_table = [p.dump() for p in role_data]
        print("[DATENBANK] >> Role Cache wird geladen")
        for i in role_table:
            role_list = [_.replace("_role", "") for _ in i if i[_] is True]
            user_dict[i['user_id']] = role_list
    return user_dict


@lru_cache()
def config():
    with open("config.json") as fp:
        data = json.load(fp)
    return data
