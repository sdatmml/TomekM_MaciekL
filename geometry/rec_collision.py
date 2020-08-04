from geometry.rectangle import Rectangle


class RecCollision:

    @staticmethod
    def check_if_collision(rec1: Rectangle, rec2: Rectangle) -> bool:
        """
        Method calculate shadows on axis x and y created by rec1 and rec2
        :return: True if rectangles are in collision, False otherwise
        """
        rec1_sh_x, rec1_sh_y = (rec1.start_point[0], rec1.point2[0]), (rec1.start_point[1], rec1.point3[1])
        rec2_sh_x, rec2_sh_y = (rec2.start_point[0], rec2.point2[0]), (rec2.start_point[1], rec2.point3[1])

        if rec1_sh_x[0] <= rec2_sh_x[0] and rec1_sh_x[0] <= rec2_sh_x[1] and \
                rec1_sh_x[1] <= rec2_sh_x[0] and rec1_sh_x[1] <= rec2_sh_x[1]:
            return False

        elif rec1_sh_x[0] >= rec2_sh_x[0] and rec1_sh_x[0] >= rec2_sh_x[1] and \
                rec1_sh_x[1] >= rec2_sh_x[0] and rec1_sh_x[1] >= rec2_sh_x[1]:
            return False

        elif rec1_sh_y[0] <= rec2_sh_y[0] and rec1_sh_y[0] <= rec2_sh_y[1] and \
                rec1_sh_y[1] <= rec2_sh_y[0] and rec1_sh_y[1] <= rec2_sh_y[1]:
            return False

        elif rec1_sh_y[0] >= rec2_sh_y[0] and rec1_sh_y[0] >= rec2_sh_y[1] and \
                rec1_sh_y[1] >= rec2_sh_y[0] and rec1_sh_y[1] >= rec2_sh_y[1]:
            return False

        return True


if __name__ == "__main__":

    rec1 = Rectangle((1, 1), 1, 1)
    rec2 = Rectangle((2, 1), 1, 1)
    print(RecCollision.check_if_collision(rec1, rec2))




