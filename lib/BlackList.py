from lib.CacheHandler import blacklist
from lib.sql import session_scope, Blacklist as BL


class BlacklistHandling:
    def __init__(self, word: str):
        self.word = word

    def check(self) -> bool:
        data = blacklist()
        return self.word.lower() in data

    def add_word(self) -> str:
        with session_scope() as db_session:
            data = db_session.query(BL).filter_by(word=self.word.lower()).first()
            if not data:
                new_word = BL(
                    word=self.word.lower()
                )
                db_session.add(new_word)
                return "a"
            else:
                return "b"

    def remove_word(self) -> str:
        with session_scope() as db_session:
            data = db_session.query(BL).filter_by(word=self.word.lower()).first()
            if data:
                db_session.query(BL).filter_by(word=self.word.lower()).delete()
                return "a"
            else:
                return "b"
