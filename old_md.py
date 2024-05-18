import numpy as np
class Maze_bfs_solving:
    def __init__(self, maze) -> None:
        self.maze = maze.copy()
        self.A_x = None
        self.A_y = None
        self.B_x = None
        self.B_y = None
        self.size = len(self.maze)
        self.visited = None
        self.parent = None
        self.step = None
        self.searching_area = []

    def createMaze(self):
        self.visited = np.array([[False for i in range(self.size)] for j in range(self.size)])
        self.parent = np.array([[None for i in range(self.size)] for j in range(self.size)])
        self.step = np.array([[0 for i in range(self.size)]for j in range(self.size)])
        self.A_x, self.A_y = 1, 1
        self.B_x, self.B_y = self.size - 2 , self.size - 2
        self.maze[self.A_x, self.A_y] = 'A'
        self.maze[self.B_x, self.B_y] = 'B'

    def Bfs(self):
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        self.createMaze()
        s, t = self.A_x, self.A_y
        u, v = self.B_x, self.B_y
        queue = []
        queue.append((s, t))
        while(len(queue) > 0):
            top = queue.pop(0)
            self.searching_area.append(top)

            for k in range(4):
                i1 = top[0] + dx[k]
                j1 = top[1] + dy[k]
                if(i1 >= 0 and i1 < self.size and j1 >= 0 and j1 < self.size):
                    if(self.maze[i1, j1] != 'x'):
                        self.step[i1, j1] = self.step[top[0], top[1]] + 1
                        self.parent[i1, j1] = (top[0], top[1])
                        queue.append((i1, j1))
                        self.maze[i1, j1] = 'x'
        return self.searching_area

    def Truyvet(self):
            self.Bfs()
            u, v = self.B_x, self.B_y
            way = []
            way.append((u, v))
            while(u != self.A_x or v != self.A_y):
                temp = self.parent[u, v]
                u = temp[0]
                v = temp[1]
                way.append((u,v))
            way.reverse()
            return way
