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

