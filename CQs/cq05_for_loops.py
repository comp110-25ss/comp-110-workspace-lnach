"""Practice for-looping over lists and dicts."""

__author__ = "730825624"


def w_sum(vals: list[float]) -> float:
    """Uses a while loop to find the sum of the vals list"""
    idx: int = 0
    sum: float = 0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Uses a for .. in loop to find the sum of the vals list"""
    sum: float = 0
    for val in vals:
        sum += val
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Uses a for .. in loop and range() to find the sum of the vals list"""
    sum: float = 0
    for idx in range(0, len(vals)):
        sum += vals[idx]
    return sum


def get_keys(dict: dict[str, int]) -> list[str]:
    """Takes a dictionary input and returns a list of the keys"""
    keys: list[str] = []
    for key in dict:
        keys.append(key)
    return keys


def get_values(dict: dict[str, int]) -> list[int]:
    """Takes a dictionary input and returns a list of the values"""
    values: list[int] = []
    # Access the dictionary values by using the keys and append
    # the value to the values list
    for key in dict:
        values.append(dict[key])
    return values
