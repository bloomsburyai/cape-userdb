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
