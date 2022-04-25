import json
import os
from time import time


def create_database():
    if not os.path.isfile('users.json'):
        data = {}
        with open('users.json', 'w+') as fp:
            json.dump(data, fp, indent=4)
    if not os.path.isfile('chat.json'):
        data = {}
        with open('chat.json', encoding='utf-8') as fp:
            json.dump(data, fp, indent=4)


def create_user(user_id: str):
    create_database()
    with open('users.json', encoding='utf-8') as fp:
        data = json.load(fp)
    if user_id not in data:
        data[user_id] = {
            'level': 1,
            'exp': 0,
            'time': 6
        }
        with open('users.json', 'w') as fp:
            json.dump(data, fp, indent=4)


def set_global(server_id: str, channel_id: str):
    create_database()
    with open('chat.json', encoding='utf-8') as fp:
        data = json.load(fp)
    data[server_id] = channel_id
    with open('chat.json', 'w+') as fp:
        json.dump(data, fp, indent=4)


def request_global(data_type: str, server_id: str = None):
    create_database()
    with open('chat.json', encoding='utf-8') as fp:
        data = json.load(fp)
    if data_type == "single":
        if server_id in data:
            return data[server_id]
    elif data_type == "list":
        data_list = []
        for i in data:
            data_list.append(data[i])
        return data_list


def delete_global(server_id: str):
    create_database()
    with open('chat.json', encoding='utf-8') as fp:
        data = json.load(fp)
    del data[server_id]
    with open('chat.json', 'w+') as fp:
        json.dump(data, fp, indent=4)


def set_time(user_id: str):
    create_user(user_id)
    with open('users.json', encoding='utf-8') as fp:
        data = json.load(fp)
    data[user_id]['time'] = str(time())
    with open('users.json', 'w') as fp:
        json.dump(data, fp, indent=4)


def get_time(user_id: str):
    create_user(user_id)
    with open('users.json', encoding='utf-8') as fp:
        data = json.load(fp)
    last_time = data[user_id]['time']
    return last_time
