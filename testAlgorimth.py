import numpy as np
import random
import heapq as pq

class mazeGeneration:
    def __init__(self) -> None:
        self.size = 20

    def createMaze(self):
        maze = np.ones((self.size, self.size, 4), dtype= 'int32') # wall(up, left, right, down)
        r = 0 # row
        c = 0 # col
        cur = [r, c]
        visited = np.zeros((self.size, self.size), dtype= 'int32')
        visited[0, 0] = 1
        visit_log = [[0, 0]]
        n = 0 # thu tu cua o da di den
        count_visit = int(0)
        while count_visit != (self.size * self.size):
            option = [0, 0, 0, 0] # phia tuong co the remove: down, right, up, left
            if r != 0:
                if visited[r - 1][c] == 0:
                    option[2] = 1 # co the remove up
            if r != self.size - 1:
                if visited[r + 1][c] == 0:
                    option[0] = 1 # co the remove down
            if c != 0:
                if visited[r][c - 1] == 0:
                    option[3] = 1 # co the remove left
            if c != self.size - 1:
                if visited[r][c + 1] == 0:
                    option[1] = 1 # co the remove right
            if option == [0, 0, 0, 0]: # khong the remove bat ki huong nao
                if n == 0: break
                cur = visit_log[n - 1]
                visit_log.pop()
                r = cur[0]
                c = cur[1]
                n -= 1
                # tro lai o truoc do
            else:
                nodefound = False
                while nodefound == False:
                    remove_wall = random.randint(0,3) # chon ngau nhien 1 phia tuong de xem dieu kien (xoa/ khong xoa)
                    if option[remove_wall] == 1: # buc tuong da chon co the xoa
                        if remove_wall == 0: # down
                            maze[cur[0]][cur[1]][0] = 0 # xoa tuong phia duoi
                            opposite_node = [cur[0] + 1, cur[1]] # di chuyen den o ben duoi
                            maze[opposite_node[0]][opposite_node[1]][2] = 0
                        elif remove_wall == 1: # right
                            maze[cur[0]][cur[1]][1] = 0 # xoa tuong ben phai
                            opposite_node = [cur[0], cur[1] + 1] # di chuyen den o ben phai
                            maze[opposite_node[0]][opposite_node[1]][3] = 0
                        elif remove_wall == 2: # up
                            maze[cur[0]][cur[1]][2] = 0 # xoa tuong ben duoi
                            opposite_node = [cur[0] - 1, cur[1]] # di chuyen den o ben duoi
                            maze[opposite_node[0]][opposite_node[1]][0] = 0 # 
                        elif remove_wall == 3: # left
                            maze[cur[0]][cur[1]][3] = 0 # xoa tuong phia trai
                            opposite_node = [cur[0], cur[1] - 1] # di chuyen den o phia trai
                            maze[opposite_node[0]][opposite_node[1]][1] = 0
                        n += 1
                        visit_log.append(opposite_node) # them vao danh sach o da di qua -> xac dinh de tro ve
                        cur = opposite_node # di chuyen den o da di chuyen o phia tren
                        visited[cur[0]][cur[1]] = 1
                        r = cur[0]
                        c = cur[1]
                        nodefound = True
            count_visit = visited.sum()
        return maze

class Maze_bfs_solving:
    def __init__(self, matrix) -> None:
        self.maze = matrix
        self.A_x = None
        self.A_y = None
        self.B_x = None
        self.B_y = None
        self.size = 20
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
        self.size = 20
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
            

maze = mazeGeneration().createMaze()
print(maze)
T = Maze_bfs_solving(maze)
T1 = maze_dijkstra_solving(maze)
T.Bfs((0,0),(19,19))
T1.Dijkstra((0,0),(19,19))
print(T.searching_area)
print(T1.searching_area)
# in lan luot - nhung o nao da xuat hien trong in roi thi k in nua
