from cape_userdb.base import DB
from cape_userdb.session import Session
from cape_userdb.user import User
from cape_userdb.event import Event
from cape_userdb.bot import Bot
from cape_userdb.coverage import Coverage
from cape_userdb.email_event import EmailEvent
from cape_userdb.facebook_bot import FacebookBot
from cape_userdb.hangouts_space import HangoutsSpace


def create_tables():
    DB.connect()
    DB.create_tables([User, Session, Event, Bot, Coverage, EmailEvent, HangoutsSpace, FacebookBot], safe=True)


if __name__ == "__main__":
    create_tables()
