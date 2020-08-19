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
        return self.color ==PURPLE

    def reset(self):
        return self.color ==WHITE

    def make_closed(self):
        return self.color ==  RED

    def make_open(self):
        return self.color == GREEN