from lib.RankHandler import RankCheck
from lib.sql import RoomTable, session_scope


class Blacklist(RankCheck):
    def __init__(self, room_name: str, user_id: int, word: str = None):
        super().__init__(room_name, user_id)
        self.word = word

    def check(self) -> bool:
        with session_scope() as db_session:
            data = db_session.query(RoomTable).filter_by(name=self.room_name).first()
            return self.word.lower() in data.blacklist["data"]

    def get_list(self) -> list:
        with session_scope() as db_session:
            data = db_session.query(RoomTable).filter_by(name=self.room_name).first()
            if data:
                return data.blacklist["data"]

    def add_word(self):
        if self.is_mod():
            with session_scope() as db_session:
                data = db_session.query(RoomTable).filter_by(name=self.room_name).first()
                if self.word.lower() not in data.blacklist["data"]:
                    blacklist = data.blacklist
                    blacklist["data"].append(self.word.lower())
                    db_session.query(RoomTable).filter_by(name=self.room_name).update({RoomTable.blacklist: blacklist})
                    return "a"
                else:
                    return "b"

    def remove_word(self):
        if self.is_mod():
            with session_scope() as db_session:
                data = db_session.query(RoomTable).filter_by(name=self.room_name).first()
                if self.word in data.blacklist["data"]:
                    blacklist = data.blacklist
                    blacklist["data"].remove(self.word.lower())
                    return "a"
                else:
                    return "b"
