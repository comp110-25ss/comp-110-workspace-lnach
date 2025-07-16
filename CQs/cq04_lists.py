"""Mutating functions."""

__author__ = "730825624"


def manual_append(list: list[int], integer: int) -> None:
    list.append(integer)


def double(list: list[int]) -> None:
    idx: int = 0
    # while the index is less than the length of the list
    # it will keep running.
    # This will double every element in the list
    while idx < len(list):
        list[idx] = list[idx] * 2
        # Add to index to progress toward False for the loop
        idx += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1


double(list_2)

print(list_1)

print(list_2)
