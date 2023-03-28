from turtle import distance

import pygame
from design_set.global_variables import *


class Node:
    def __init__(self, row, col, width, total_rows, isVisited, distance, previous, isStart, isEnd):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
        self.isVisited = [0, 0]
        self.distance = distance
        self.previous = [-1, -1]
        self.isStart = isStart
        self.isEnd = isEnd

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def found_barrier(self):
        return self.color == YELLOW

    def is_start(self):
        return self.color == RED

    def is_end(self):
        return self.color == GREEN

    def reset(self):
        self.color = WHITE

    def make_start(self):
        self.color = RED

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = YELLOW

    def make_end(self):
        self.color = GREEN

    def make_path(self):
        self.color = YELLOW

    def getVisited(self):
        return self.isVisited[0], self.isVisited[1]

    def getDistance(self):
        return distance

    def getPrevious(self):
        return self.previous[0], self.previous[1]

    def getStart(self):
        return self.isStart

    def getEnd(self):
        return self.isEnd

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].found_barrier():  # DOWN
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].found_barrier():  # TOP
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].found_barrier():  # RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].found_barrier():  # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False
