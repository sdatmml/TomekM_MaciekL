from geometry.rectangle import Rectangle
from geometry.rec_collision import RecCollision
import pytest


@pytest.mark.parametrize("test_input,exp_result2,exp_result3,exp_result4",
                         (
                                 (Rectangle((1, 1), 3, 1), (4, 1), (4, 2), (1, 2)),
                                 (Rectangle((0, 0), -1, 3), (-1, 0), (-1, 3), (0, 3)),
                                 (Rectangle((2, 2), 2, 2), (4, 2), (4, 4), (2, 4)),
                                 (Rectangle((-2, -2), 2, -1), (0, -2), (0, -3), (-2, -3)),
                                 (Rectangle((3, 3), -2, -5), (1, 3), (1, -2), (3, -2)),
                                 (Rectangle((2, -2), -2, 2), (0, -2), (0, 0), (2, 0)),
                                 (Rectangle((0, 0), -4, 5), (-4, 0), (-4, 5), (0, 5))
                         ))
def test_rec_points1(test_input, exp_result2, exp_result3, exp_result4):
    assert test_input.point2 == exp_result2
    assert test_input.point3 == exp_result3
    assert test_input.point4 == exp_result4


@pytest.mark.parametrize("test_input1,test_input2,exp_result",
                         (
                                 (Rectangle((1, 1), 5, 4), Rectangle((2, 1), 1, 1), True),
                                 (Rectangle((1, 1), 1, 1), Rectangle((3, 3), 1, 1), False),
                                 (Rectangle((1, 1), 3, 6), Rectangle((2, 2), 1, 3), True),
                                 (Rectangle((2, 2), 2, 2), Rectangle((2, 6), 2, 2), False),
                                 (Rectangle((1, 1), 2, 2), Rectangle((0, 0), -2, 3), False),
                                 (Rectangle((1, 1), 2, 2), Rectangle((-1, -1), 3, 3), True),
                                 (Rectangle((0, 0), 1, 1), Rectangle((1, 0), 1, 1), False),
                                 (Rectangle((-1, -1), 2, 2), Rectangle((-2, -2), 4, 4), True),
                                 (Rectangle((0, 0), -2, 2), Rectangle((-2, 0), -2, 2), False),
                                 (Rectangle((1, 1), 1, 1), Rectangle((-1, -1), -1, -1), False),
                                 (Rectangle((2, -2), -2, 2), Rectangle((0, 0), -4, 5), False)
                         ))
def test_collision(test_input1, test_input2, exp_result):
    assert RecCollision.check_if_collision(test_input1, test_input2) == exp_result

