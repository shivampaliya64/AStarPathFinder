import pygame
import math
from queue import PriorityQueue

WIDTH = 800 #Window Size
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finder")

RED = (255, 0, 0) #visited/checked node
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255) #unvisited
BLACK = (0, 0, 0) #not in region
ORANGE = (255, 165, 0) #start node
GREY = (128, 128, 128)
PURPLE = (128, 0, 128) #final path
TURQUOISE = (64, 224 , 208)

class Spot:  # Node, to keep track of all nodes, their position ,color
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = row*width
        self.color=WHITE
        self.neighbors=[]
        self.width=width
        self.total_rows=total_rows

    def get_pos(self):
        return self.row,self.col

    def is_closed(self): # to check if node has been visited marked red and color
        return self.color==RED

    def is_open(self):
        return self.color==GREEN

    def is_barrier(self):
         return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color == WHITE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE

    def draw(self,win):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.width))

    def update_neighbors(self,grid):
        #pass


     def __lt__(self, other):# for handling 2 spots together
         return False

def h(p1,p2): #Heuristics here considering L distance, only right and down travelling
    x1,y1=p1
    x2,y2=p2
    return abs(x1-x2)+abs(y1-y2)
def make_grid(rows,width): # to hold the spots to perform operations on
     grid =[] # list
     gap = width // rows # Integer divison or gap between each cube
     for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot =Spot(i,j,gap,rows)
            grid[i].append(spot)

        return grid

def draw_grid(win,rows,width):
    gap = width//rows
    for i in range(rows):
        pygame.draw.line(win,GREY,(0,i*gap),(width,i*gap)) # creating gap wise space
        for j in range(rows):
            pygame.draw.line(win,GREY,(gap*j,0),(j*gap,width)) # drwaing vertical lines

def draw(win,grid,row,width):
    win.fill(WHITE)
    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win,rows,width)
    pygame.display.update()
