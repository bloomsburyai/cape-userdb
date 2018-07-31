from typing import Union
from peewee import CharField

from cape_userdb.base import BaseDB


class FacebookBot(BaseDB):
    # Inherited fields are:
    # modified: Union[RealDatetimeField, datetime.datetime] = RealDatetimeField(default=utc_now, index=True)
    # id: int
    user_id: Union[CharField, str] = CharField(index=True)
    facebook_psid: Union[CharField, str] = CharField(index=True, null=True)
    authorization_code: Union[CharField, str] = CharField()
