from lib.sql import GlobalTable, session_scope


class ChannelHandler:
    def __init__(self, server_id: int, channel=None):
        self.server_id = server_id
        self.channel = channel

    def set_channel(self):
        with session_scope() as db_session:
            data = db_session.query(GlobalTable).filter_by(server_id=self.server_id).first()
            if not data:
                new_channel = GlobalTable(
                    server_id=self.server_id,
                    channel_id=self.channel.id
                )
                db_session.add(new_channel)
            else:
                db_session.query(GlobalTable).filter_by(server_id=self.server_id).update(channel_id=self.channel.id)

    def remove_channel(self):
        with session_scope() as db_session:
            data = db_session.query(GlobalTable).filter_by(server_id=self.server_id).first()
            if data:
                db_session.query(GlobalTable).filter_by(server_id=self.server_id).delete()
                return "a"
            else:
                return "b"


class SetttingsHandler:
    def __int__(self, bot_id):
        self.bot_id = bot_id

    def edit_spam(self, seconds):
        with session_scope() as db_session:
            db_session.query(GlobalTable).filter_by(bot_id=self.bot_id).update(spam=seconds)
            return True
