"""Creating wordle in Python"""

__author__ = "730825624"


def contains_char(word: str, character: str) -> bool:
    """A function that searches an input word for an input character"""
    assert len(character) == 1, f"len('character') is not 1"
    idx: int = 0
    while idx < len(word):
        # If a match is found it will return True
        if character == word[idx]:
            return True
        idx += 1
    # If it loops through the whole word and doesn't find a match, it returns False
    return False


def emojified(guess: str, secret: str) -> str:
    """Emojifies letters in the guess based on how they match those in the secret word"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002b1c"
    GREEN_BOX: str = "\U0001f7e9"
    YELLOW_BOX: str = "\U0001f7e8"
    emoji_string: str = ""
    idx = 0
    while idx < len(guess):
        # Checks for an exact match at the same index
        if guess[idx] == secret[idx]:
            emoji_string += GREEN_BOX
        # Checks for no match at any index
        elif contains_char(secret, guess[idx]) == False:
            emoji_string += WHITE_BOX
        # Checks for a match but not at the same index
        elif contains_char(secret, guess[idx]) == True:
            emoji_string += YELLOW_BOX
        idx += 1
    return emoji_string


def input_guess(expected_length: int) -> str:
    """Verifies that the user guess is the correct length and returns it back"""
    guess = input("Enter a " + str(expected_length) + " character word: ")
    while len(guess) != expected_length:
        guess = input("That wasn't " + str(expected_length) + " chars! Try again: ")
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""

    turn: int = 0
    length: int = len(secret)
    guess: str = ""
    # Runs this loop if turn is less than 6 and the guess
    # is not the same as the secret word
    while turn < 6 and guess != secret:
        turn += 1
        print("=== Turn " + str(turn) + "/6 ===")
        # The guess is a separate variable (not just
        # inputting input_guess straight into emojified)
        # so that it is equal to the word that's guessed and
        # not the emoji string that's output from the emojified function
        guess = input_guess(length)
        print(emojified(guess, secret))

    if guess == secret:
        print("You won in " + str(turn) + "/6 turns!")
    elif turn == 6:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
