class Rectangle:

    def __init__(self, start_point: tuple, horizontal_side: float, vertical_side: float):
        self.start_point = start_point
        self.horizontal_side = horizontal_side
        self.vertical_side = vertical_side
        self.point2 = (start_point[0]+self.horizontal_side, start_point[1])
        self.point3 = (start_point[0]+self.horizontal_side, start_point[1] + self.vertical_side)
        self.point4 = (start_point[0], start_point[1] + self.vertical_side)

    def __str__(self):
        return f"Rectangle with points {self.start_point}, {self.point2}, {self.point3}, {self.point4}"