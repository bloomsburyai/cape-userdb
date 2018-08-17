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

import datetime, uuid

from typing import Union
from peewee import CharField, TextField

from cape_userdb.base import BaseDB, CompressedPickleField, DateTimeField


def uuid_str():
    return str(uuid.uuid4())


class EmailEvent(BaseDB):
    # Inherited fields are:
    # modified: Union[DateTimeField, datetime.datetime] = DateTimeField(index=True, default=utc_now)
    # id: int
    unique_id: Union[CharField, str] = CharField(index=True, default=uuid_str)
    user_id: Union[CharField, str] = CharField(index=True, null=False)

    question_email_package: Union[CompressedPickleField, dict] = CompressedPickleField(null=False)
    question_email_extracted_body: Union[TextField, str] = TextField(null=False)
    question_email_sender: Union[TextField, str] = TextField(null=False)
    question_email_timestamp: Union[DateTimeField, datetime.datetime] = DateTimeField(null=False)

    suggested_email_results: Union[CompressedPickleField, list] = CompressedPickleField(null=True)
    suggested_email_extracted_body: Union[TextField, str] = TextField(null=True)
    suggested_email_sender: Union[TextField, str] = TextField(null=True)
    suggested_email_timestamp: Union[DateTimeField, datetime.datetime] = DateTimeField(null=True)

    corrected_email_package: Union[CompressedPickleField, dict] = CompressedPickleField(null=True)
    corrected_email_extracted_body: Union[TextField, str] = TextField(null=True)
    corrected_email_sender: Union[TextField, str] = TextField(null=True)
    corrected_email_timestamp: Union[DateTimeField, datetime.datetime] = DateTimeField(null=True)

    final_email_saved_reply_id: Union[TextField, str] = TextField(null=True)
    final_email_extracted_body: Union[TextField, str] = TextField(null=True)
    final_email_sender: Union[TextField, str] = TextField(null=True)
    final_email_timestamp: Union[DateTimeField, datetime.datetime] = DateTimeField(null=True)
