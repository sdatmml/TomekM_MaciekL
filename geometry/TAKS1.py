class Geometry:
    """Finding center of a section"""
    @staticmethod
    def section_center(point1: tuple, point2: tuple) -> tuple:
        if point1 == point2:
            raise Exception("Data is no section error")
        else:
            new_x = (point1[0] + point2[0])/2
            new_y = (point1[1] + point2[1])/2
            new_z = (point1[2] + point2[2])/2

            return tuple([new_x, new_y, new_z])
