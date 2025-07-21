"""Practice writing unit tests"""

__author__ = "730825624"

from find_max import find_and_remove_max


def test_return_max_value() -> None:
    """Tests if the function returns the max value"""
    assert find_and_remove_max([1, 2, 3, 4, 5]) == 5


def test_mutate_max_value() -> None:
    """Tests if the function mutates the list correctly"""
    a = [1, 2, 3, 4, 5, 5, 5]
    find_and_remove_max(a)
    assert a == [1, 2, 3, 4]


def test_unconventional_input() -> None:
    """Tests if the function returns -1 on an empty list"""
    assert find_and_remove_max([]) == -1
