import datetime, uuid

from typing import Union
from peewee import CharField, TextField, BooleanField, DoubleField

from cape_userdb.base import BaseDB, CompressedPickleField, RealDatetimeField


def uuid_str():
    return str(uuid.uuid4())


class EmailEvent(BaseDB):
    unique_id: Union[CharField, str] = CharField(index=True, default=uuid_str)
    user_id: Union[CharField, str] = CharField(index=True, null=False)

    question_email_package: Union[CompressedPickleField, dict] = CompressedPickleField(null=False)
    question_email_extracted_body: Union[TextField, str] = TextField(null=False)
    question_email_sender: Union[TextField, str] = TextField(null=False)
    question_email_timestamp: Union[RealDatetimeField, datetime.datetime] = RealDatetimeField(null=False)

    suggested_email_results: Union[CompressedPickleField, list] = CompressedPickleField(null=True)
    suggested_email_extracted_body: Union[TextField, str] = TextField(null=True)
    suggested_email_sender: Union[TextField, str] = TextField(null=True)
    suggested_email_timestamp: Union[RealDatetimeField, datetime.datetime] = RealDatetimeField(null=True)

    corrected_email_package: Union[CompressedPickleField, dict] = CompressedPickleField(null=True)
    corrected_email_extracted_body: Union[TextField, str] = TextField(null=True)
    corrected_email_sender: Union[TextField, str] = TextField(null=True)
    corrected_email_timestamp: Union[RealDatetimeField, datetime.datetime] = RealDatetimeField(null=True)

    final_email_saved_reply_id: Union[TextField, str] = TextField(null=True)
    final_email_extracted_body: Union[TextField, str] = TextField(null=True)
    final_email_sender: Union[TextField, str] = TextField(null=True)
    final_email_timestamp: Union[RealDatetimeField, datetime.datetime] = RealDatetimeField(null=True)
