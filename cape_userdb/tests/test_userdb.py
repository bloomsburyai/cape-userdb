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

from cape_userdb.user import User
from peewee import IntegrityError
import pytest


def test_user_creation():
    try:
        del_user = User.get('user_id', 'fake-id')
        del_user.delete_instance()
    except:
        pass
    user = User(user_id='fake-id', password='test')
    user.save()
    test_user = User.get('user_id', 'fake-id')
    assert user == test_user
    user.delete_instance()


def test_unique_user():
    try:
        del_user = User.get('user_id', 'fake-id')
        del_user.delete_instance()
    except:
        pass

    user = User(user_id='fake-id', password='test')
    user.save()
    with pytest.raises(IntegrityError):
        duplicate_user = User(user_id='fake-id', password='test')
        duplicate_user.save()

    user.delete_instance()


def test_delete_user():
    try:
        del_user = User.get('user_id', 'fake-id')
        del_user.delete_instance()
    except:
        pass

    user = User(user_id='fake-id', password='test')
    user.save()

    user.delete_instance()

    test_user = User.get('user_id', 'fake-id')
    assert test_user is None
