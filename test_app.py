from app import add, subtract, average


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_average():
    assert average([2, 4, 6]) == 4


def test_average_empty():
    # Expected: empty input returns 0. Currently crashes.
    assert average([]) == 0
