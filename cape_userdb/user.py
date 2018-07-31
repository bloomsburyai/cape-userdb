from functools import partial

from argon2.exceptions import VerifyMismatchError
from typing import Union, Optional
from peewee import CharField, BooleanField
import secrets
import datetime
from cape_userdb import cape_userdb_settings
from cape_userdb.base import BaseDB, CompressedPickleField, ArgonField, DateTimeField
from hashlib import sha256

_TOKEN_BYTE_SIZE = 32


class User(BaseDB):
    # Inherited fields are:
    # modified: Union[CurrentTimestampField, datetime.datetime] = CurrentTimestampField(index=True)
    # id: int
    user_id: Union[CharField, str] = CharField(index=True, unique=True)
    password: Union[CharField, str] = ArgonField()
    third_party_info: Union[None, CompressedPickleField, dict] = CompressedPickleField(null=True)
    terms_agreed: Union[BooleanField, bool] = BooleanField(default=False)
    # Settings for responder
    default_response: Union[CharField, str] = CharField(default=cape_userdb_settings.DEFAULT_RESPONSE)
    saved_reply_threshold: Union[CharField, str] = CharField(default=cape_userdb_settings.DEFAULT_THRESHOLD)
    document_threshold: Union[CharField, str] = CharField(default=cape_userdb_settings.DEFAULT_THRESHOLD)
    # Token
    token: Union[CharField, str] = CharField(default=partial(secrets.token_urlsafe, _TOKEN_BYTE_SIZE), index=True,
                                             unique=True)
    admin_token: Union[CharField, str] = CharField(default=partial(secrets.token_urlsafe, _TOKEN_BYTE_SIZE), index=True,
                                                   unique=True)
    plan: Union[CharField, str] = CharField(default='free')
    created: Union[DateTimeField, datetime.datetime] = DateTimeField(default=datetime.datetime.now)
    onboarding_completed: Union[BooleanField, bool] = BooleanField(default=False)
    # Settings for email forwarding
    forward_email: Union[CharField, str] = CharField(default=cape_userdb_settings.DEFAULT_EMAIL)
    forward_email_verified: Union[BooleanField, bool] = BooleanField(default=False)

    def verify_password(self, password_to_verify: str) -> bool:
        try:
            return ArgonField.verify(self.password, password_to_verify)
        except VerifyMismatchError:
            return False

    @property
    def verified_email(self) -> Optional[str]:
        if self.forward_email_verified:
            return self.forward_email

    @property
    def verified_email_token(self) -> Optional[str]:
        if self.forward_email != cape_userdb_settings.DEFAULT_EMAIL:
            return sha256(self.forward_email.encode()).hexdigest()
