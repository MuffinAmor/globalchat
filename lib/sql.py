import json
import random
import string
from contextlib import contextmanager

from sqlalchemy import INTEGER, String, JSON, Column, create_engine, BigInteger, DateTime, Boolean, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()

with open("config.json") as fp:
    data = json.load(fp)["sql"]


class ColorShop(Base):
    __tablename__ = 'colorshop'
    color_id = Column(Integer, autoincrement=True, primary_key=True)
    hex_code = Column(String(50))
    number = Column(Integer)
    credits = Column(INTEGER)

    def __init__(self, color_id, hex_code, number, credits):
        self.color_id = color_id
        self.hex_code = hex_code
        self.number = number
        self.credits = credits

    def dump(self):
        return dict([(k, v) for k, v in vars(self).items() if not k.startswith('_')])


class LevelRoles(Base):
    __tablename__ = 'levelroles'
    level = Column(Integer, primary_key=True, autoincrement=False)
    role_name = Column(String(20), nullable=False)


class Ranks(Base):
    __tablename__ = 'ranks'
    user_id = Column(BigInteger, primary_key=True, autoincrement=False)
    banned = Column(Boolean)
    owner_role = Column(Boolean)
    admin_role = Column(Boolean)
    team_role = Column(Boolean)
    moderator_role = Column(Boolean)
    partner_role = Column(Boolean)
    vip_role = Column(Boolean)
    special = Column(String(50))

    def __init__(self, user_id, banned, owner_role, admin_role, team_role, moderator_role, partner_role, vip_role,
                 special):
        self.user_id = user_id
        self.banned = banned
        self.owner_role = owner_role
        self.admin_role = admin_role
        self.team_role = team_role
        self.moderator_role = moderator_role
        self.partner_role = partner_role
        self.vip_role = vip_role
        self.special = special

    def dump(self):
        return dict([(k, v) for k, v in vars(self).items() if not k.startswith('_')])


class Settings(Base):
    __tablename__ = 'settings'
    bot_id = Column(BigInteger, primary_key=True)
    spam = Column(INTEGER)
    blacklist = Column(JSON)
    exp_per_msg = Column(INTEGER)
    money_per_daily = Column(INTEGER)
    level_calc_percent = Column(INTEGER)

    def __init__(self, bot_id, spam, blacklist, exp_per_msg, money_per_daily, level_calc_percent):
        self.bot_id = bot_id
        self.spam = spam
        self.blacklist = blacklist
        self.exp_per_msg = exp_per_msg
        self.money_per_daily = money_per_daily
        self.level_calc_percent = level_calc_percent

    def dump(self):
        return dict([(k, v) for k, v in vars(self).items() if not k.startswith('_')])


class CalcTable(Base):
    __tablename__ = 'level_calc'
    level = Column(Integer, primary_key=True)
    exp = Column(BigInteger)

    def __init__(self, level, exp):
        self.level = level
        self.exp = exp

    def dump(self):
        return dict([(k, v) for k, v in vars(self).items() if not k.startswith('_')])


class GlobalTable(Base):
    __tablename__ = 'global'
    guild_id = Column(BigInteger, primary_key=True, autoincrement=False)
    channel_id = Column(BigInteger)

    def __init__(self, guild_id, channel_id):
        self.guild_id = guild_id
        self.channel_id = channel_id

    def dump(self):
        return dict([(k, v) for k, v in vars(self).items() if not k.startswith('_')])


class LevelTable(Base):
    __tablename__ = 'level'
    user_id = Column(BigInteger, primary_key=True, autoincrement=False)
    exp = Column(INTEGER, nullable=False)
    level = Column(INTEGER, nullable=False)

    def __init__(self, user_id, exp, level):
        self.user_id = user_id
        self.exp = exp
        self.level = level

    def dump(self):
        return dict([(k, v) for k, v in vars(self).items() if not k.startswith('_')])


class Credittable(Base):
    __tablename__ = 'credits'
    user_id = Column(BigInteger, primary_key=True, autoincrement=False)
    credits = Column(INTEGER, nullable=False)

    def __init__(self, user_id, credits):
        self.user_id = user_id
        self.credits = credits

    def dump(self):
        return dict([(k, v) for k, v in vars(self).items() if not k.startswith('_')])


def random_id():
    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=16))


def init_db(uri):
    engine = create_engine(uri, pool_recycle=3600, pool_pre_ping=True, pool_use_lifo=True)
    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False,
                                             bind=engine))
    Base.metadata.create_all(bind=engine)
    return db_session


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = init_db(f'mysql+pymysql://{data["user"]}:{data["password"]}@localhost/{data["database"]}')
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
