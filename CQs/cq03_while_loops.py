"""Practicing string iteration with while loops"""

__author__ = 730825624


def num_instances(phrase: str, search_char: str) -> int:
    phrase_idx = 0
    count = 0
    # the index must be less than the length of the phrase
    while phrase_idx < len(phrase):
        # if the letter at the index is the same as the search character, 1 is added
        # to the count
        if phrase[phrase_idx] == search_char:
            count = count + 1
        phrase_idx = phrase_idx + 1
    return count
