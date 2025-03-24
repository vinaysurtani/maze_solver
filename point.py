class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point1, point2):
        self.__point1 = point1
        self.__point2 = point2
    
    def draw(self, canvas, fill_color):
        x1 = self.__point1.x
        y1 = self.__point1.y
        x2 = self.__point2.x
        y2 = self.__point2.y
        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)