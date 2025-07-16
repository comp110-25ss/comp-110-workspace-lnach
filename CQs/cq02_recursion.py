"""Writing recursive functions"""

__author__ = "730825624"


def f(n: int, k: int) -> int:
    if n == 0:
        return 0
    else:
        return k + f(n - 1, k)
