from tkinter.messagebox import YES
import pytest


def always_returns_true():
    Return True


def test_always_returns_true():
    assert always_returns_true()
