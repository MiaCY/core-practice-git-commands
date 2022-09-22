import pytest


def always_returns_true():
    print("Let's make a conflict")


def test_always_returns_true():
    assert always_returns_true()
