from geometry.rec_collision import Rectangle, RecCollision

start_point1 = input("Select the starting point for the rectangle No. 1 (x,y): ")
horizontal_side1 = input("Select length of horizontal side: [+ right/ - left]: ")
vertical_side1 = input("Select length of vertical side: [+ right/ - left]: ")

rec1 = Rectangle(eval(start_point1), int(horizontal_side1), int(vertical_side1))

start_point2 = input("Select the starting point for the rectangle No. 2 (x,y): ")
horizontal_side2 = input("Select length of horizontal side: [+ right/ - left]: ")
vertical_side2 = input("Select length of vertical side: [+ right/ - left]: ")

rec2 = Rectangle(eval(start_point2), int(horizontal_side2), int(vertical_side2))

collision = input("\nTo check if rectangles collide press enter:")

if RecCollision.check_if_collision(rec1, rec2):
    print("Rectangles are in collision")
else:
    print("Great! No collision")