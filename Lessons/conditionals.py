"""Practicing conditionals"""


def check_first_letter(word: str, letter: str) -> str:
    """Returns "match" if letter is first char of word"""
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter("happy", "s"))
