'''def is_mod():
    def predicate(ctx):
        return RankCheck().is_mod()

    return commands.check(predicate)
'''

from lib.sql import session_scope, Ranks


class UserData:
    def __init__(self, user_id: int):
        self.user_id = user_id

    def check_if(self) -> bool:
        with session_scope() as db_session:
            data = db_session.query(Ranks).filter_by(user_id=self.user_id).first()
            if data:
                return True

    def register(self) -> bool:
        with session_scope() as db_session:
            data = db_session.query(Ranks).filter_by(user_id=self.user_id).first()
            if not data:
                new_user = Ranks(
                    user_id=self.user_id,
                    owner_role=False,
                    admin_role=False,
                    team_role=False,
                    moderator_role=False,
                    partner_role=False,
                    vip_role=False,
                    banned=False,
                    special="False"
                )
                db_session.add(new_user)
                return True

    def unregister(self) -> bool:
        with session_scope() as db_session:
            data = db_session.query(Ranks).filter_by(user_id=self.user_id).first()
            if data:
                db_session.query(Ranks).filter_by(user_id=self.user_id).delete()
                return True


class RankCheck(UserData):
    def __init__(self, user_id: int):
        super().__init__(user_id)

    def is_owner(self) -> bool:
        with session_scope() as db_session:
            data = db_session.query(Ranks).filter_by(user_id=self.user_id).first()
            if data.owner_role:
                return True

    def is_admin(self) -> bool:
        with session_scope() as db_session:
            data = db_session.query(Ranks).filter_by(user_id=self.user_id).first()
            if data.admin_role:
                return True

    def is_team(self) -> bool:
        with session_scope() as db_session:
            data = db_session.query(Ranks).filter_by(user_id=self.user_id).first()
            if data.team_role:
                return True

    def is_moderator(self) -> bool:
        with session_scope() as db_session:
            data = db_session.query(Ranks).filter_by(user_id=self.user_id).first()
            if data.moderator_role:
                return True

    def is_partner(self) -> bool:
        with session_scope() as db_session:
            data = db_session.query(Ranks).filter_by(user_id=self.user_id).first()
            if data.partner_role:
                return True

    def is_vip(self) -> bool:
        with session_scope() as db_session:
            data = db_session.query(Ranks).filter_by(user_id=self.user_id).first()
            if data.vip_role:
                return True

    def is_banned(self) -> bool:
        with session_scope() as db_session:
            data = db_session.query(Ranks).filter_by(user_id=self.user_id).first()
            if data.banned:
                return True


class EditRanks(RankCheck):
    """
    I'm pretty sure, there is an easier way than this.
    """

    def __init__(self, user_id: int):
        super().__init__(user_id)

    def add_owner(self):
        with session_scope() as db_session:
            if self.check_if():
                if not self.is_owner():
                    db_session.query(Ranks).filter_by(user_id=self.user_id).update({Ranks.owner_role: True})
                else:
                    return "a"
            else:
                return "b"

    def remove_owner(self):
        with session_scope() as db_session:
            if self.check_if():
                if self.is_owner:
                    db_session.query(Ranks).filter_by(user_id=self.user_id).update({Ranks.owner_role: False})
                else:
                    return "a"
            else:
                return "b"

    def add_admin(self):
        with session_scope() as db_session:
            if self.check_if():
                if not self.is_admin():
                    db_session.query(Ranks).filter_by(user_id=self.user_id).update({Ranks.admin_role: True})
                else:
                    return "a"
            else:
                return "b"

    def remove_admin(self):
        with session_scope() as db_session:
            if self.check_if():
                if self.is_admin():
                    db_session.query(Ranks).filter_by(user_id=self.user_id).update({Ranks.admin_role: False})
                else:
                    return "a"
            else:
                return "b"

    def add_team(self):
        with session_scope() as db_session:
            if self.check_if():
                if not self.is_team():
                    db_session.query(Ranks).filter_by(user_id=self.user_id).update({Ranks.team_role: True})
                else:
                    return "a"
            else:
                return "b"

    def remove_team(self):
        with session_scope() as db_session:
            if self.check_if():
                if self.is_admin():
                    db_session.query(Ranks).filter_by(user_id=self.user_id).update({Ranks.team_role: False})
                else:
                    return "a"
            else:
                return "b"

    def add_moderator(self):
        with session_scope() as db_session:
            if self.check_if():
                if not self.is_moderator():
                    db_session.query(Ranks).filter_by(user_id=self.user_id).update({Ranks.moderator_role: True})
                else:
                    return "a"
            else:
                return "b"

    def remove_moderator(self):
        with session_scope() as db_session:
            if self.check_if():
                if self.is_moderator():
                    db_session.query(Ranks).filter_by(user_id=self.user_id).update({Ranks.moderator_role: False})
                else:
                    return "a"
            else:
                return "b"

    def add_partner(self):
        with session_scope() as db_session:
            if self.check_if():
                if not self.is_partner():
                    db_session.query(Ranks).filter_by(user_id=self.user_id).update({Ranks.partner_role: True})
                else:
                    return "a"
            else:
                return "b"

    def remove_partner(self):
        with session_scope() as db_session:
            if self.check_if():
                if self.is_partner():
                    db_session.query(Ranks).filter_by(user_id=self.user_id).update({Ranks.partner_role: False})
                else:
                    return "a"
            else:
                return "b"

    def add_vip(self):
        with session_scope() as db_session:
            if self.check_if():
                if not self.is_vip():
                    db_session.query(Ranks).filter_by(user_id=self.user_id).update({Ranks.vip_role: True})
                else:
                    return "a"
            else:
                return "b"

    def remove_vip(self):
        with session_scope() as db_session:
            if self.check_if():
                if self.is_vip():
                    db_session.query(Ranks).filter_by(user_id=self.user_id).update({Ranks.vip_role: False})
                else:
                    return "a"
            else:
                return "b"

    def ban_user(self):
        with session_scope() as db_session:
            if self.check_if():
                if not self.is_banned():
                    db_session.query(Ranks).filter_by(user_id=self.user_id).update({Ranks.banned: True})
                    return "a"
            else:
                return "b"

    def unban_user(self):
        with session_scope() as db_session:
            if self.check_if():
                if self.is_banned():
                    db_session.query(Ranks).filter_by(user_id=self.user_id).update({Ranks.banned: False})
                else:
                    return "a"
            else:
                return "b"
