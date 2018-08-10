# Copyright 2018 BLEMUNDSBURY AI LIMITED
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pickle
import zlib
import argon2
import datetime
from typing import List, Union, Any

from pytz import utc
from peewee import DateTimeField, BlobField, Model, CharField

from cape_userdb.cape_userdb_settings import DB_PATH
from peewee import SqliteDatabase

DB = SqliteDatabase(DB_PATH)

_COMPRESSION_LEVEL = 9
_PROTOCOL_LEVEL = pickle.HIGHEST_PROTOCOL
_PASSWORD_HASHER = argon2.PasswordHasher()
_PASSWORD_HASHER_PREFIX = '$argon2i'


class RealDatetimeField(DateTimeField):
    db_field = 'datetime_fsp6'


class CurrentTimestampField(DateTimeField):
    db_field = 'TIMESTAMP'

    def db_value(self, value):
        return BaseDB.utc_now()


class TimestampField(DateTimeField):
    db_field = 'TIMESTAMP'


class CompressedPickleField(BlobField):
    def __init__(self, *args, **kwargs):
        self.compression_level = _COMPRESSION_LEVEL
        self.pickle_protocol = _PROTOCOL_LEVEL
        super(CompressedPickleField, self).__init__(*args, **kwargs)

    def db_value(self, value):
        if value is not None:
            return zlib.compress(pickle.dumps(value, self.pickle_protocol), self.compression_level)

    def python_value(self, value):
        if value is not None:
            return pickle.loads(zlib.decompress(value))


class ArgonField(CharField):
    verify = _PASSWORD_HASHER.verify

    def db_value(self, value):
        """Use Argon2 algorithm to hash protect passwords"""
        if value is not None:
            if not value.startswith(_PASSWORD_HASHER_PREFIX):
                return _PASSWORD_HASHER.hash(value)
            return value


def _utc_now() -> datetime.datetime:
    return datetime.datetime.utcnow().replace(tzinfo=utc)


class BaseDB(Model):
    modified: Union[CurrentTimestampField, datetime.datetime] = CurrentTimestampField(index=True, default=0)
    id: int

    class Meta:
        database = DB

    @staticmethod
    def utc_now() -> datetime.datetime:
        return datetime.datetime.utcnow().replace(tzinfo=utc)

    @classmethod
    def _get(cls, field_name: str, field_value: Any) -> Union[Model, None]:
        try:
            return next(iter(cls.select().where(getattr(cls, field_name) == field_value).limit(1)))
        except StopIteration:
            return None

    @classmethod
    def get(cls, field_name: str, field_value: Any) -> Union[Model, None]:
        instance = cls._get(field_name, field_value)
        return instance

    @classmethod
    def all(cls, field_name: str, field_value: Any) -> List:
        try:
            return list(cls.select().where(getattr(cls, field_name) == field_value))
        except StopIteration:
            return []

    @classmethod
    def last_modification_from_field(cls, field_name: str, field_value: Any) -> Union[datetime.datetime, None]:
        try:
            return next(iter(cls.select(cls.modified).where(getattr(cls, field_name) == field_value).order_by(
                cls.modified.desc()).limit(1).tuples()))[0]
        except StopIteration:
            return None
