from tkinter import Tk, BOTH, Canvas

from cell import Cell
from maze import Maze
from point import Point, Line

class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("title")
        self.__canvas = Canvas(self.__root, width=self.width, height=self.height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas,fill_color)

    def close(self):
        self.__running = False

def main():
    win = Window(800,600)
    #print(win.width)
    #print(win.height)
    #point1 = Point(50,100)
    ##point3 = Point(100,200)
    #line = Line(point1, point2)
    #line2 = Line(point2, point3)
    #win.draw_line(line, "red")
    #win.draw_line(line2, "black")
    #cell = Cell(point1.x,point2.x,point1.y,point2.y,win)
    #cell.draw()
    # Two cells next to each other
    #cell3 = Cell(300, 400, 100, 200, win)
    #cell4 = Cell(300, 400, 200, 300, win)
    #cell3.draw()
    #cell4.draw()
    #cell3.draw_move(cell4, True)
    num_cols = 10
    num_rows = 10
    m1 = Maze(0, 0, num_rows, num_cols, win.width, win.height, win)
    m1.solve()
    win.wait_for_close()

if __name__ == "__main__":
    main()