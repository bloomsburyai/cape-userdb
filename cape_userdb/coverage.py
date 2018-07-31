import datetime
from typing import Union
from peewee import CharField, DoubleField

from cape_userdb.base import BaseDB, RealDatetimeField


class Coverage(BaseDB):
    # Inherited fields are:
    # modified: Union[RealDatetimeField, datetime.datetime] = RealDatetimeField(default=utc_now, index=True)
    # id: int
    user_id: Union[CharField, str] = CharField(index=True)
    coverage: Union[DoubleField, float] = DoubleField()
    created: Union[RealDatetimeField, datetime.datetime] = RealDatetimeField(default=BaseDB.utc_now)