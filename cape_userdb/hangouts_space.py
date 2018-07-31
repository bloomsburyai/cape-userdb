from typing import Union
from peewee import CharField

from cape_userdb.base import BaseDB


class HangoutsSpace(BaseDB):
    # Inherited fields are:
    # modified: Union[RealDatetimeField, datetime.datetime] = RealDatetimeField(default=utc_now, index=True)
    # id: int
    user_id: Union[CharField, str] = CharField(index=True)
    space_id: Union[CharField, str] = CharField(index=True, unique=True)
