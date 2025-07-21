"""Reverse engineering algorithms and abstractions"""

__author__ = "730825624"


def all(integers: list[int], integer: int) -> bool:
    """Checks if the integer given is the same as the integers in the list"""
    # If the list is empty it immediately returns False
    if len(integers) == 0:
        return False
    # Loops through the list and if any of the integers do not equal the integer given
    # it returns False. Otherwise it returns True
    for element in integers:
        if element != integer:
            return False

    return True


def max(integers: list[int]) -> int:
    """Returns the largest integer in a list. If the list is empty, it throws a
    ValueError"""
    if len(integers) == 0:
        raise ValueError("max() arg is an empty List")
    # Make the largest integer the first integer in case there are any negative
    # numbers in the list
    largest_int = integers[0]
    # Loops through the list and checks if each number is larger than the last.
    # Returns the largest
    for integer in integers:
        if integer > largest_int:
            largest_int = integer
    return largest_int


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Returns true if both lists are the same at every index and False if they are
    not"""
    idx = 0
    # If the lengths of each list are different, it will return False
    if len(list1) != len(list2):
        return False
    # Once the lengths are verified, it will loop through the list for as many indices
    # as it contains checking each integer at each index. If it's ever different it will
    # immediately return False and stop
    while idx < len(list1):
        if list1[idx] != list2[idx]:
            return False
        idx += 1
    # If it goes through the lists without returning False, it returns True
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    """Mutate list1 by appending all the values of list2 to the end of it"""
    # Iterate through list2 appending each integer to list1
    for num in list2:
        list1.append(num)
