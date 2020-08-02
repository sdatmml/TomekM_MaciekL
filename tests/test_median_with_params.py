from statistics_.median_with_params import MathFunc
import pytest


@pytest.fixture(scope='module', name='math_func')
def math_func():
    return MathFunc()


@pytest.mark.parametrize("test_input,expected",
                         (
                            ([1, 2, 3, 4, 10], 7.43),
                            ([1, 2, 3], 5.86),
                            ([1, 2, 15, 19], 16.07),
                            ([1, 2, 7, 56], 9.79)
                         ))
def test_median_with_params(test_input, expected, math_func):
    assert math_func.calculate_median_with_params(test_input) == expected

