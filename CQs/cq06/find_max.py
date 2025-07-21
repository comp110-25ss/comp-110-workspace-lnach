"""Practice writing a function that modifies a list"""

__author__ = "730825624"


def find_and_remove_max(input: list[int]) -> int:
    """Finds the max value in a list, removes it from the list, and returns that
    max value"""
    # If it's an empty list, immediately returns -1
    if len(input) == 0:
        return -1
    idx: int = 0
    max_value: int = input[0]
    # Use a while loop to find the max value
    while idx < len(input):
        if input[idx] > max_value:
            max_value = input[idx]
        idx += 1
    # Once the max value is found, a second while loop removes it from the list
    # It does not change indices when a match is found to account for the .pop()
    # method mutating the list.
    idx = 0
    while idx < len(input):
        if input[idx] == max_value:
            input.pop(idx)
        else:
            idx += 1

    return max_value
