import random
import pygame
import numpy as np

# Khởi tạo Pygame
pygame.init()

WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768 
white, black = (255, 255, 255), (0, 0, 0)
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
screen_color = (0, 0, 150)
font_path = 'font/Pixeltype.TTF'

class Initialization:
    def __init__(self):
        self.screen_width = WINDOW_WIDTH
        self.screen_height = WINDOW_HEIGHT
        self.screen_color = screen_color
        self.font_path = font_path
        self.screen = screen

    def draw_rectangle(self, x, y, width, height, color):
        pygame.draw.rect(self.screen, color, (x, y, width, height))
        pygame.display.flip()

    def draw_text(self, text, text_size, color, x, y):
        text = pygame.font.Font(self.font_path, text_size).render(text, True, color)
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        return text_rect

    def input_image_background(self, image_path):
        image = pygame.image.load(image_path).convert()
        self.screen.blit(image, (84, 84))
        
    def draw_floor(self):
        self.screen.fill(self.screen_color)
        # Vẽ hình
        self.draw_rectangle(75, (self.screen_height - 618) // 2, 618, 618, (255, 215, 0))
        self.draw_rectangle(84, (self.screen_height - 600) // 2, 600, 600, (255, 255, 255))
        self.draw_rectangle(716, (self.screen_height - 618) // 2, 248, 618, (255, 215, 0))
        self.draw_rectangle(725, (self.screen_height - 600) // 2, 230, 600, self.screen_color)
        self.draw_text("MENU", 64, (255, 255, 0), 384, 42)
        self.input_image_background("image/Tam and gia huy.png")

    def draw_load(self):
        self.screen.fill(self.screen_color)
        # Vẽ hình
        self.draw_rectangle(75, (self.screen_height - 618) // 2, 618, 618, (255, 215, 0))
        self.draw_rectangle(84, (self.screen_height - 600) // 2, 600, 600, (255, 255, 255))
        self.draw_rectangle(716, (self.screen_height - 618) // 2, 248, 618, (255, 215, 0))
        self.draw_rectangle(725, (self.screen_height - 600) // 2, 230, 600, self.screen_color)
        self.draw_text("MENU", 64, (255, 255, 0), 384, 42)

    def draw_rectangle_with_text(self,x, y,width,text):
        font = pygame.font.Font(None, 36)
        rect = pygame.Rect(x, y, width,40)
        pygame.draw.rect(screen, white, rect)
        text_surface = font.render(text, True, black)
        text_rect = text_surface.get_rect(center=(x + width // 2, y + 20))
        screen.blit(text_surface, text_rect)
    
    def draw_to_delete(self, title):
        self.draw_rectangle(725, (self.screen_height - 600) // 2, 230, 600, self.screen_color)
        self.draw_rectangle(84, 0, 600, 70, self.screen_color)
        self.draw_text(title, 64, (255, 255, 0), 384, 42)
        
class mazeGeneration:
    def __init__(self) -> None:
        self.size = None
        self.cell_size = None
        return 
    
    def createMaze(self, size):
        self.size = size
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
        maze_list = maze.tolist()
        #maze co size nhu da khoi tao
        return maze_list

    def draw_maze(self, Walls):
        # Tính toán tọa độ bắt đầu vẽ mê cung để canh chỉnh vào giữa màn hình
        self.cell_size = ((768)**2 / (len(Walls)) ** 2) ** 0.5
        maze_width = self.size * self.cell_size
        maze_height = self.size * self.cell_size
        start_x = (WINDOW_WIDTH - maze_width) // 2
        start_y = (WINDOW_HEIGHT - maze_height) // 2

        for x in range(self.size):
            for y in range(self.size):
                if Walls[y][x][3] == 1:  # Tường bên trái
                    pygame.draw.line(screen, black, (start_x + x * self.cell_size, start_y + y * self.cell_size),
                                    (start_x + x * self.cell_size, start_y + (y + 1) * self.cell_size))
                if Walls[y][x][2] == 1:  # Tường phía trên
                    pygame.draw.line(screen, black, (start_x + x * self.cell_size, start_y + y * self.cell_size),
                                    (start_x + (x + 1) * self.cell_size, start_y + y * self.cell_size))
                if Walls[y][x][1] == 1:  # Tường bên phải
                    pygame.draw.line(screen, black, (start_x + (x + 1) * self.cell_size, start_y + y * self.cell_size),
                                    (start_x + (x + 1) * self.cell_size, start_y + (y + 1) * self.cell_size))
                if Walls[y][x][0] == 1:  # Tường phía dưới
                    pygame.draw.line(screen, black, (start_x + x * self.cell_size, start_y + (y + 1) * self.cell_size),
                                    (start_x + (x + 1) * self.cell_size, start_y + (y + 1) * self.cell_size))


    def mazeApplication(self, Walls, path, color, drew):
        #dua vao matran, duong di
        self.cell_size = ((768)**2 / (len(Walls)) ** 2) ** 0.5
        maze_width = len(Walls) * self.cell_size
        maze_height = len(Walls) * self.cell_size
        start_x = 0
        start_y = 0
        # Vòng lặp chính
        path_drew = [path[0]]
        for i, cell in enumerate(path):
                if i == 0: continue
                if cell in drew:
                    path_drew.append(cell)
                    start = (start_x + path[i - 1][1] * self.cell_size + self.cell_size // 2, start_y + path[i - 1][0] * self.cell_size + self.cell_size // 2)
                    end = (start_x + path[i][1] * self.cell_size + self.cell_size // 2, start_y + path[i][0] * self.cell_size + self.cell_size // 2)
                    pygame.draw.line(screen, color, start, end, 3)
        pygame.display.flip()
        return path_drew
    def mazeApplicationManual(self, Walls, path, color):
        self.cell_size = ((768)**2 / (len(Walls)) ** 2) ** 0.5
        maze_width = len(Walls) * self.cell_size
        maze_height = len(Walls) * self.cell_size
        start_x = 0
        start_y = 0
        # Vòng lặp chính
        for i in range(len(path) - 1):
                start = (start_x + path[i][1] * self.cell_size + self.cell_size // 2,start_y + path[i][0] * self.cell_size + self.cell_size // 2)
                end = (start_x + path[i + 1][1] * self.cell_size + self.cell_size // 2,start_y + path[i + 1][0] * self.cell_size + self.cell_size // 2)
                pygame.draw.line(screen, color, start, end, 3)
        pygame.display.flip()