import unittest
import pytest
from src.user import User

@pytest.fixture
def user_t():
    return User("Josh", "Nijjar")

def test_fullname(user_t):
    assert user_t.fullname() == "Josh Nijjar"

def test_alarm(user_t):
    alarm_time = user_t.alarm_time("6:00am")
    assert alarm_time == "Josh, wakes up at 6:00am."



