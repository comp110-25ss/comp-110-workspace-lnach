from Lessons.first import get_first


def test_get_first() -> None:
    """Testing basic behavior for get_first function"""
    assert get_first([4, 5, 6, 7]) == 4
