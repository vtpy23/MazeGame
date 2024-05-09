import mazeGeneration as mG
import numpy as np
import heapq as pq
from queue import PriorityQueue

class playAutomatically:
    class Maze_bfs_solving:
        def __init__(self, matrix) -> None:
            self.maze = matrix
            self.A_x = None
            self.A_y = None
            self.B_x = None
            self.B_y = None
            self.size = mG.size
            self.visited = None
            self.parent = None
            self.step = None
            self.searching_area = []
        def createMaze(self, start_point, end_point):
            self.visited = np.array([[False for i in range(self.size)] for j in range(self.size)])
            self.parent = np.array([[None for i in range(self.size)] for j in range(self.size)])
            self.step = np.array([[0 for i in range(self.size)]for j in range(self.size)])
            self.A_x, self.A_y = map(int, start_point)
            self.B_x, self.B_y = map(int, end_point)

        def Bfs(self, start_point, end_point):
            dx = [1, 0, -1, 0]
            dy = [0, 1, 0, -1]
            self.createMaze(start_point, end_point)
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
                        if(self.maze[top[0]][top[1]][k] != 1 and self.visited[i1, j1] == False):
                            self.step[i1, j1] = self.step[top[0], top[1]] + 1
                            self.parent[i1, j1] = (top[0], top[1])
                            if(i1 == self.B_x and j1 == self.B_y): return
                            queue.append((i1, j1))
                            self.visited[i1, j1] = True
            return self.searching_area
        def Truyvet(self):
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
    class maze_dijkstra_solving:
        def __init__(self, matrix) -> None:
            self.maze = matrix.copy()
            self.A_x = None
            self.A_y = None
            self.B_x = None
            self.B_y = None
            self.size = mG.size
            self.visited = None
            self.parent = None
            self.step = None
            self.maxn = 100001
            self.INF = 1e9
            self.searching_area = []
        def creatingInfo(self, start_point, end_point):
            self.parent = np.array([[None for i in range(self.size)] for j in range(self.size)])
            self.step = np.array([[self.INF for i in range(self.size)] for j in range(self.size)])
            self.A_x, self.A_y = map(int, start_point)
            self.B_x, self.B_y = map(int, end_point)
        def Dijkstra(self, start_point, end_point):
            dx = [1, 0, -1, 0]
            dy = [0, 1, 0, -1]
            self.creatingInfo(start_point, end_point)     
            self.step[self.A_x, self.A_y] = 0
            Q = []
            pq.heappush(Q, (0, (self.A_x, self.A_y)))
            while(Q):
                top = pq.heappop(Q)
                kc = top[0]
                u = top[1]
                i = u[0]
                j = u[1]
                if(kc > self.step[u]): continue
                self.searching_area.append(u)
                for k in range(4):
                    newi = i + dx[k]
                    newj = j + dy[k] 
                    w = None
                    if(newi >= 0 and newi < self.size) and (newj < self.size and newj >= 0) :
                        if(self.maze[i][j][k] == 1):
                            w = self.INF
                        else: w = 1
                        if(self.step[newi, newj] > self.step[u] + w):
                            self.step[newi, newj] = self.step[u] + w
                            self.parent[newi, newj] = u
                            pq.heappush(Q, (self.step[newi, newj], (newi, newj)))
                    if(newi == self.B_x and newj == self.B_y):
                        break
            return self.searching_area
        def Truyvet(self):
            #print(self.parent[self.B_x, self.B_y])
            u, v = self.B_x, self.B_y
            way = []
            way.append((u, v))
            while(u != self.A_x or v != self.A_y):
                temp = self.parent[u, v]
                u = temp[0]
                v = temp[1]
                way.append((u, v))
            way.reverse()
            return way
            
    class A_solving: 
        def __init__(self, matrix) -> None:
            self.maze = matrix.copy()

        def heuristic(self, cell1, cell2): # heuristic : manhattan distance
            x1, y1 = cell1
            x2, y2 = cell2
            return abs(x1 - x2) + abs(y1 - y2)
        
        def A_star(self,  start, end):
            maze = np.array(self.maze)
            path = {}
            g_scores = {(i,j): float('inf') for i in range(maze.shape[0]) for j in range(maze.shape[1])} # cost (distance) from current cell to start cell
            g_scores[start] = 0
            f_scores = {(i,j): float('inf') for i in range(maze.shape[0]) for j in range(maze.shape[1])} # total cost = g_scores + h
            f_scores[start] = self.heuristic(start, end)
            open_set = PriorityQueue()
            open_set.put((f_scores[start], self.heuristic(start, end), start))
            
            while not open_set.empty():
                curCell = open_set.get()[2]
                if curCell == end:
                    break
                for m in range(4): # down right up left
                    if maze[curCell[0]][curCell[1]][m] == 0:
                        if m == 0: # down
                            childCell = (curCell[0] + 1, curCell[1]) 
                        elif m == 1: # right
                            childCell = (curCell[0], curCell[1] + 1)
                        elif m == 2: # up
                            childCell = (curCell[0] - 1, curCell[1])
                        elif m == 3: # left
                            childCell = (curCell[0], curCell[1] - 1)
                        temp_g_score = g_scores[curCell] + 1
                        temp_f_score = temp_g_score + self.heuristic(childCell, end) # f(child) = g(child) + h(child)
                        if temp_f_score < f_scores[childCell]: 
                            g_scores[childCell] = temp_g_score
                            f_scores[childCell] = temp_f_score
                            open_set.put((temp_f_score, self.heuristic(childCell, end), childCell))
                            path[childCell] = curCell
            
            fwdPath = {}
            cell = end
            while cell != start: # doi child <-> parent 
                fwdPath[path[cell]] = cell
                cell = path[cell]
            final_path = list(fwdPath.keys()) # tu child di nguoc ve start
            final_path.reverse()
            final_path.append(end)
            return final_path
        
