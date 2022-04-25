import json
import os


def create_tree():
    if not os.path.isfile("Secure"):
        try:
            os.mkdir("Secure")
        except:
            pass
    if not os.path.isfile("Secure/ban.json"):
        data = {}
        with open("Secure/ban.json", "w+") as fp:
            json.dump(data, fp, indent=4)


def add_server(server_id: str, reason: str):
    create_tree()
    with open("Secure/ban.json", encoding='utf-8') as fp:
        data = json.load(fp)
    data[server_id] = reason
    with open("Secure/ban.json", "w+") as fp:
        json.dump(data, fp, indent=4)
    return "Der Server mit der ID {} wurde erfolgreich gebannt".format(server_id)


def request_server(amount: str, server_id: str = None):
    create_tree()
    with open("Secure/ban.json", encoding='utf-8') as fp:
        data = json.load(fp)
    if amount == "single":
        if server_id in data:
            return True
        else:
            return False
    elif amount == "all":
        string = ""
        for i in data:
            s_id = i
            reason = data[i]
            string += "Serverid: {}\n" \
                      "Grund: {}\n\n".format(s_id, reason)
        if string == "":
            return "Empty"
        else:
            return string


def remove_server(server_id: str):
    create_tree()
    with open("Secure/ban.json", encoding='utf-8') as fp:
        data = json.load(fp)
    if server_id in data:
        del data[server_id]
        with open("Secure/ban.json", "w+") as fp:
            json.dump(data, fp, indent=4)
    else:
        return False
