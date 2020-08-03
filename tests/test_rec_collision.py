from geometry.rectangle import Rectangle
from geometry.rec_collision import RecCollision
import pytest


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
                                 (Rectangle((1, 1), 1, 1), Rectangle((-1, -1), -1, -1), False)
                         ))
def test_collision(test_input1, test_input2, exp_result):
    assert RecCollision.check_if_collision(test_input1, test_input2) == exp_result

