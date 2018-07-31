from functools import partial

from typing import Union
from peewee import CharField
import secrets

from cape_userdb.base import BaseDB

_TOKEN_BYTE_SIZE = 32
_SESSION_RECHECK_EVERY_SECS = 86400


class Session(BaseDB):
    recheck_every = _SESSION_RECHECK_EVERY_SECS
    # Inherited fields are:
    # modified: Union[RealDatetimeField, datetime.datetime] = RealDatetimeField(default=utc_now, index=True)
    # id: int
    user_id: Union[CharField, str] = CharField(index=True)
    session_id: Union[CharField, str] = CharField(default=partial(secrets.token_urlsafe, _TOKEN_BYTE_SIZE), index=True,
                                                  unique=True)

