"""My first exercise in COMP110!"""

__author__ = "730825624"


def greet(name: str) -> str:
    """A welcoming first functiond definition"""
    return "Hello " + name + "!"


if __name__ == "__main__":
    print(greet(name=input("What is your name? ")))
