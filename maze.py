import random
import time
from cell import Cell


class Maze():
    def __init__(self,x1,y1,num_rows,num_cols,window_width,window_height,win=None,seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        if self.num_rows < 1 or self.num_cols < 1:
            raise ValueError("num_rows or num cols cant be 0 or negative")
        if not isinstance(self.num_cols, int) or not isinstance(self.num_rows, int):
            raise TypeError("please stick to integer values for num_rows and num_cols")
        self.cell_size_x = window_width // num_cols
        self.cell_size_y = window_height // num_rows
        self.win = win
        if seed is not None:
            random.seed(seed)
        self._create_cells()
        self.generate_maze()
        #print(len(self._cells))    # Number of rows
        #print(len(self._cells[0])) # Number of columns (if rows exist)

    def _create_cells(self):
        self._cells = []
        for row in range(self.num_rows):
            rlst = []
            for col in range(self.num_cols):
                rlst.append(Cell(
                    self.x1 + (col * self.cell_size_x),
                    self.x1 + ((col+1) * self.cell_size_x),
                    self.y1 + (row*self.cell_size_y),
                    self.y1 + ((row+1)*self.cell_size_y),self.win))
            self._cells.append(rlst)
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(i,j)

    def _draw_cell(self,i,j):
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        if self.win:
            self.win.redraw()
            time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self.num_rows-1][self.num_cols-1].has_bottom_wall =False
        self._draw_cell(self.num_rows-1,self.num_cols-1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        up, down, left, right = None,None,None,None
        while True:
            lst = []
            if i-1 >=0:
                up = self._cells[i-1][j]
                upc = (i-1,j)
            if i+1 <= len(self._cells)-1:
                down = self._cells[i+1][j]
                downc = (i+1,j)
            if j-1 >=0:
                left = self._cells[i][j-1]
                leftc = (i,j-1)
            if j+1 <= len(self._cells[0])-1:
                right = self._cells[i][j+1]
                rightc = (i,j+1)
            if up and up.visited == False:
                lst.append(upc)
            if down and down.visited == False:
                lst.append(downc)
            if left and left.visited == False:
                lst.append(leftc)
            if right and right.visited == False:
                lst.append(rightc)
            if len(lst) == 0:
                self._draw_cell(i,j)
                return
            else:
                ni, nj = random.choice(lst)
                # Knock down walls between (i, j) and (ni, nj)
                if ni == i - 1:  # Moving up
                    self._cells[i][j].has_top_wall = False
                    self._cells[ni][nj].has_bottom_wall = False
                elif ni == i + 1:  # Moving down
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[ni][nj].has_top_wall = False
                elif nj == j - 1:  # Moving left
                    self._cells[i][j].has_left_wall = False
                    self._cells[ni][nj].has_right_wall = False
                elif nj == j + 1:  # Moving right
                    self._cells[i][j].has_right_wall = False
                    self._cells[ni][nj].has_left_wall = False
                self._break_walls_r(ni, nj)
            
    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def generate_maze(self):
    # Start breaking walls from the top-left cell
        self._break_walls_r(0, 0)
        # Reset visited flags after maze generation
        self._reset_cells_visited()

    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == len(self._cells) - 1 and j == len(self._cells[0])-1:
            return True
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        for dy, dx in directions:
            next_i, next_j = i + dy, j + dx
            if(0 <= next_i < len(self._cells) and 0 <= next_j < len(self._cells[0])):
                neighbour = self._cells[next_i][next_j]
                if dy == -1 and dx == 0:
                    if self._cells[i][j].has_top_wall or neighbour.has_bottom_wall:
                        continue
                elif dy == 1 and dx == 0:
                    if self._cells[i][j].has_bottom_wall or neighbour.has_top_wall:
                        continue
                elif dy == 0 and dx == -1:
                    if self._cells[i][j].has_left_wall or neighbour.has_right_wall:
                        continue
                elif dy ==0 and dx == 1:
                    if self._cells[i][j].has_right_wall or neighbour.has_left_wall:
                        continue
                if not neighbour.visited:
                    self._cells[i][j].draw_move(neighbour)
                    if self._solve_r(next_i, next_j):
                        return True
                    self._cells[i][j].draw_move(neighbour, True)
        return False