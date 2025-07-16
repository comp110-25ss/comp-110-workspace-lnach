"""Plan a tea party by inputting the number of guests"""

__author__ = "730825624"


def main_planner(guests: int) -> None:
    """The main function of the program that produces a printed output"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    # Creates a print statement and turns the cost function output into a string
    # The arguments in the cost function are the tea_bags and treats functions with
    # the arguments in those functions being the number of guests
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Calculates the number of tea bags needed based on the number of guests"""
    return people * 2


def treats(people: int) -> int:
    """Calculates the number of treats needed based on the number of tea bags"""
    # Utilizes the tea_bags function so that if any changes are made to how many
    # tea bags are purchased per person, only one change needs to be made in the
    # tea_bags function
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the total cost of the tea bags and treats"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
