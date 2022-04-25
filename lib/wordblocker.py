import json
import os
import sys


def blocked(word: str):
    try:
        if not os.path.isfile("Secure"):
            try:
                os.mkdir("Secure")
            except:
                pass
        if os.path.isfile("Secure/wordblocker.json"):
            with open('Secure/wordblocker.json', encoding='utf-8') as r:
                blacklist = json.load(r)
            wordlist = list(blacklist['data']['blacklistet'])
            for i in wordlist:
                if i.lower() in word.lower():
                    return True
            else:
                return False
        else:
            blacklist = {'name': 'Wordblacklist', 'bot': 'Nellie', 'data': {'blacklistet': {}}}
            blacklist['data']['blacklistet'] = []
            wordlist = blacklist['data']['blacklistet']
            with open('Secure/wordblocker.json', 'w') as r:
                json.dump(blacklist, r, indent=4)
            if word in wordlist:
                return True
            else:
                return False
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)


def addword(word: str):
    wordlist = blocked(word)
    with open('Secure/wordblocker.json', encoding='utf-8') as r:
        blacklist = json.load(r)
    if wordlist:
        return 'The Word is allready in the Blacklist.'
    elif not wordlist:
        list = blacklist['data']['blacklistet']
        list.append(word)
        with open('Secure/wordblocker.json', 'w') as r:
            json.dump(blacklist, r, indent=4)
        return 'The Word **{}** has been added to the Blacklist.'.format(word)


def removeword(word: str):
    wordlist = blocked(word)
    with open('Secure/wordblocker.json', encoding='utf-8') as r:
        blacklist = json.load(r)
    if not wordlist:
        return 'The Word is not in the Blacklist.'
    elif wordlist:
        list = blacklist['data']['blacklistet']
        list.remove(word)
        with open('Secure/wordblocker.json', 'w') as r:
            json.dump(blacklist, r, indent=4)
        return 'The Word **{}** has been removed from the Blacklist.'.format(word)


def blacklist():
    blocked('Ping')
    with open('Secure/wordblocker.json', encoding='utf-8') as r:
        blacklist = json.load(r)
    return blacklist['data']['blacklistet']
