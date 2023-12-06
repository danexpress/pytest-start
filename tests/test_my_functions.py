import pytest
import time
import source.my_functions as my_functions


def test_add():
    result = my_functions.add(number_one=1, number_two=4)
    assert result == 5


def test_add_strings():
    result = my_functions.add(number_one="i like ", number_two="baddies")
    assert result == "i like baddies"


def test_divide():
    result = my_functions.divide(number_one=10, number_two=5)
    assert result == 2


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(number_one=10, number_two=0)


@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = my_functions.divide(number_one=10, number_two=5)
    assert result == 2


@pytest.mark.skip(reason="This feature is broken")
def test_add():
    assert my_functions.add(number_one=2, number_two=3) == 7


@pytest.mark.xfail(reason="We know we cannot divide by zero")
def test_divide_zero_broken():
    my_functions.divide(number_one=4, number_two=0)
