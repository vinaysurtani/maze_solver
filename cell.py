from point import Line, Point


class Cell():
    def __init__(self,x1,x2,y1,y2,win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win
        self.visited = False

    def draw(self):
        if self._win:
            left_wall = Line(Point(self._x1,self._y1),Point(self._x1,self._y2))
            right_wall = Line(Point(self._x2,self._y1),Point(self._x2,self._y2))
            top_wall = Line(Point(self._x1,self._y1),Point(self._x2,self._y1))
            bottom_wall = Line(Point(self._x1,self._y2),Point(self._x2,self._y2))
            self._win.draw_line(left_wall,"black" if self.has_left_wall else "white")
            self._win.draw_line(right_wall,"black" if self.has_right_wall else "white")
            self._win.draw_line(top_wall,"black" if self.has_top_wall else "white")
            self._win.draw_line(bottom_wall,"black" if self.has_bottom_wall else "white")

    def draw_move(self, to_cell, undo=False):
        xc1 = (self._x1 + self._x2) / 2
        yc1 = (self._y1 + self._y2) / 2
        xc2 = (to_cell._x1 + to_cell._x2) / 2
        yc2 = (to_cell._y1 + to_cell._y2) / 2
        c1 = Point(xc1,yc1)
        c2 = Point(xc2,yc2)
        center_line = Line(c1,c2)
        if undo == False:
            self._win.draw_line(center_line,"red")
        else:
            self._win.draw_line(center_line,"gray")

    def remove_walls_between(cell1, cell2):
        if cell2._x1 == cell1._x2:
            cell1.has_right_wall = False
            cell2.has_left_wall = False
        elif cell2._x2 == cell1._x1:
            cell1.has_left_wall = False
            cell2.has_right_wall = False
        elif cell2._y1 == cell1._y2:
            cell1.has_bottom_wall = False
            cell2.has_top_wall = False
        elif cell2._y2 == cell1._y1:
            cell1.has_top_wall = False
            cell2.has_bottom_wall = False