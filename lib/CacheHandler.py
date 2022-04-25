import json
from functools import lru_cache

from lib.sql import session_scope, GlobalTable, Ranks

message_cache = {}

'''
@lru_cache(maxsize=120)
def blacklist():
    blacklist = {}
    with session_scope() as db_session:
        room_data = db_session.query(RoomTable)
        room_table = [p.dump() for p in room_data]
        print("[DATENBANK] >> Blacklist Cache wird geladen")
        for i in room_table:
            blacklist[i["name"]] = i["blacklist"]["data"]
        return blacklist


def check_for_word(room, message):
    for i in message:
        if i.lower() in blacklist()[room]:
            return True

@lru_cache()
def public():
    public_cache = {}
    with session_scope() as db_session:
        room_data = db_session.query(PublicTable)
        room_table = [p.dump() for p in room_data]
        print("[DATENBANK] >> Public Cache wird geladen")
        for i in room_table:
            public_cache[i["name"]] = {
                "owner": i["owner"]
            }
        return public_cache'''


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
