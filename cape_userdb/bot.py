from typing import Union
from peewee import CharField

from cape_userdb.base import BaseDB


class Bot(BaseDB):
    # Inherited fields are:
    # modified: Union[RealDatetimeField, datetime.datetime] = RealDatetimeField(default=utc_now, index=True)
    # id: int
    user_id: Union[CharField, str] = CharField(index=True)
    bot_id: Union[CharField, str] = CharField(index=True, unique=True)
    bot_token: Union[CharField, str] = CharField()
    access_token: Union[CharField, str] = CharField()
