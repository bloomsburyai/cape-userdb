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
