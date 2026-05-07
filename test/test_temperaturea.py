import pytest
from temperature import is_overheating

def test_high_temperature():
    assert is_overheating(90) is True

def test_normal_temperature():
    assert is_overheating(60) is False
