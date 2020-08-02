from geometry.rectangle import Rectangle
from geometry.rec_collision import RecCollision


def test_rec_collision():
    rec1 = Rectangle((1, 1), 5, 4)
    rec2 = Rectangle((2, 1), 1, 1)
    assert RecCollision.check_if_collision(rec1, rec2)


def test2_rec_collision():
    rec1 = Rectangle((1, 1), 1, 1)
    rec2 = Rectangle((3, 3), 1, 1)
    assert not RecCollision.check_if_collision(rec1, rec2)