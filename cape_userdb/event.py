import datetime

from typing import Union
from peewee import CharField, TextField, BooleanField, DoubleField

from cape_userdb.base import BaseDB, CompressedPickleField, RealDatetimeField


class Event(BaseDB):
    # Inherited fields are:
    # modified: Union[RealDatetimeField, datetime.datetime] = RealDatetimeField(default=utc_now, index=True)
    # id: int
    user_id: Union[CharField, str] = CharField(index=True)
    question: Union[TextField, str] = TextField()
    question_source: Union[CharField, str] = CharField()
    answers: Union[CompressedPickleField, list] = CompressedPickleField()
    answered: Union[BooleanField, bool] = BooleanField()
    automatic: Union[BooleanField, bool] = BooleanField()
    read: Union[BooleanField, bool] = BooleanField(default=False)
    archived: Union[BooleanField, bool] = BooleanField(default=False)
    created: Union[RealDatetimeField, datetime.datetime] = RealDatetimeField(default=BaseDB.utc_now)
    duration: Union[DoubleField, float] = DoubleField(default=0)