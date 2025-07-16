"""Demonstrates while loops by finding low value in string"""

cards: str = "5235"

card_idx: int = 0
# look at each number in the string
low_card: int = int(cards[0])
while card_idx < 4:
    current_card: int = int(cards[card_idx])
    # check if current card is less than the low card
    if current_card < low_card:
        # update low card to be the value of the current card
        low_card = current_card
    card_idx += 1
print(low_card)
