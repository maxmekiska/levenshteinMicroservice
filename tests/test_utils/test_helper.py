import pytest

from service.utils.helper import *

data = {"s1": "nice", "s2": "cool"}


def test_lev():
    val = compute_levenshtein_distance(data)
    assert val == 4


def test_ratio():
    val = compute_ratio(data)
    assert val == 0.25


def test_hamming():
    val = compute_hamming(data)
    assert val == 4


def test_jaro():
    val = compute_jaro(data)
    assert val == 0.0
