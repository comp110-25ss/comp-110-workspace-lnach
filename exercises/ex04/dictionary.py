"""Practicing dictionary functions"""

__author__ = "730825624"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the key:value pair in a dictionary"""
    keys: list[str] = []
    values: list[str] = []
    # Puts each key and value in a separate list
    for key in input_dict:
        keys.append(key)
        values.append(input_dict[key])

    new_dict: dict[str, str] = {}

    index = 0
    # Inverts the dictionary
    while index < len(keys):
        # Checks if the key is already in the dict and if it is it throws a KeyError
        if values[index] in new_dict:
            raise KeyError("Duplicate key while inverting values!")
        new_dict[values[index]] = keys[index]
        index += 1
    return new_dict


def favorite_color(input_dict: dict[str, str]) -> str:
    """Returns the most frequently appearing favorite color"""
    color_count: dict[str, int] = {}
    # Saves each color as a key to a new dictionary. If the color is already in the
    # dictionary, it adds to the count
    for name in input_dict:
        if input_dict[name] in color_count:
            color_count[input_dict[name]] += 1
        else:
            color_count[input_dict[name]] = 1

    fav_color_count: int = 0
    fav_color: str = ""
    # Loops through the color count dictionary and appends the color with the highest
    # count to favorite_color while logging its value to favorite_color_count to
    # compare the other colors to. Because it starts at the beginning of the
    # dictionary, if there's a tie, it will return the first color with the highest count
    for color in color_count:
        if color_count[color] > fav_color_count:
            fav_color = color
            fav_color_count = color_count[color]
    return fav_color


def count(strings: list[str]) -> dict[str, int]:
    """Counts the frequency of each string in a list"""
    # Accidentally already created this when writing favorite_color
    # Counts each string that appears, appending a new key if it doesn't exist and
    # adding 1 to the existing count if it's already in the dictionary
    variable_dict: dict[str, int] = {}
    for string in strings:
        if string in variable_dict:
            variable_dict[string] += 1
        else:
            variable_dict[string] = 1
    return variable_dict


def alphabetizer(strings: list[str]) -> dict[str, list[str]]:
    """Returns a dictionary containg the starting letter of words in the list
    followed by the words associated with the letter"""
    # Initializes an empty dictionary
    words_dict: dict[str, list[str]] = {}
    # Iterates through the list, extracts the first letter, sets it to lowercase, and
    # checks if it already exists in the dictionary. If it does, it appends the full
    #  word to the list. If it doesn't it creates a new key with the value being the
    # full word in a list.
    for string in strings:
        letter = string[0].lower()
        if letter in words_dict:
            words_dict[letter].append(string)
        else:
            words_dict[letter] = [string]
    return words_dict


def update_attendance(
    attendance_dict: dict[str, list[str]], day: str, student: str
) -> None:
    """Updates an attendance dictionary given a day of the week and a student's name"""
    if day in attendance_dict:
        attendance_dict[day].append(student)
    else:
        attendance_dict[day] = [student]
