import numpy as np
import pygame
import random
class mazeGeneration:

    def __init__(self) -> None:
        self.maze = None
        self.A_x = None
        self.A_y = None
        self.B_x = None
        self.B_y = None
        self.parent = None
        self.dx = [-2, 0, 0 ,2]
        self.dy = [0, -2, 2, 0]
        self.size = 35
        self.visited = None

    def createMaze(self):
        self.parent = np.array([[None for i in range(self.size)]for j in range(self.size)])
        self.maze = np.array([['x' for i in range(self.size)] for j in range(self.size)])
        self.maze[1:self.size - 1:2, 1:self.size - 1:2] = 'o'
        self.visited = np.array([[False for i in range(self.size)]for j in range(self.size)])
        #print(self.maze)
        self.dfs(1,1)
        #print(self.visited)
        self.maze[self.visited] = 'o'
        return self.maze

    def dfs(self, s, t):
        self.visited[s, t] = True
        parent = self.parent[s, t]
        if(parent != None):
            self.visited[(s + parent[0])//2, (t + parent[1]) // 2] = True
        self.maze[s, t] = 'x'
        way = [0,1,2,3]
        while(len(way) > 0):
            k = random.choice(way)
            way.remove(k)
            s1 = s + self.dx[k]
            t1 = t + self.dy[k]
            if(s1 >= 0 and s1 < self.size and t1 >= 0 and t1 < self.size and self.visited[s1,t1] == False and self.maze[s1, t1] == 'o'):
                self.parent[s1, t1] = (s, t)
                self.dfs(s1, t1)