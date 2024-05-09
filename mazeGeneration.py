import random
import pygame
import numpy as np

# Khởi tạo Pygame

# self.size = 20
# self.size = 25  # Kích thước của mỗi ô trong mê cung
# self.WINDOW_WIDTH = 1024
# self.WINDOW_HEIGHT = 768 
# white, black = (255, 255, 255), (0, 0, 0)
# screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
# screen_color = (0, 0, 150)
#font_path = 'font/Pixeltype.TTF'

class Initialization:
    def __init__(self, screen):
        self.screen_width = 1024
        self.screen_height = 768
        self.screen_color = (0, 0, 150)
        self.font_path = 'font/Pixeltype.TTF'
        self.screen = screen

    def draw_rectangle(self, x, y, width, height, color):
        pygame.draw.rect(self.screen, color, (x, y, width, height))
        pygame.display.flip()

    def draw_text (self, text, text_size, color, x, y):
        text = pygame.font.Font(self.font_path, text_size).render(text, True, color)
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        return text_rect

    def draw_floor(self):
        self.screen.fill(self.screen_color)
        # Vẽ hình
        self.draw_rectangle(75, (self.screen_height - 618) // 2, 618, 618, (255, 215, 0))
        self.draw_rectangle(84, (self.screen_height - 600) // 2, 600, 600, (255, 255, 255))
        self.draw_rectangle(716, (self.screen_height - 618) // 2, 248, 618, (255, 215, 0))
        self.draw_rectangle(725, (self.screen_height - 600) // 2, 230, 600, self.screen_color)
        self.draw_text("MENU", 64, (255, 255, 0), 384, 42)
        self.background_image("image/Tam and gia huy.png")
    
    def background_image(self, image_path):
        image = pygame.image.load(image_path).convert()
        self.screen.blit(image, (84, 84))
    
    def draw_to_delete(self, title):
        self.draw_rectangle(740, (self.screen_height - 600) // 2, 200, 600, self.screen_color)
        self.draw_rectangle(84, 0, 600, 70, self.screen_color)
        self.draw_text(title, 64, (255, 255, 0), 384, 42)

class mazeGeneration:
    def __init__(self) -> None:
        self.maze = None
        self.A_x = None
        self.A_y = None
        self.B_x = None
        self.B_y = None
        self.parent = None
        self.dx = [1, 0, -1, 0]
        self.dy = [0, 1, 0, -1]
        self.size = 20
        self.size = 25
        pygame.init()
        self.screen = pygame.display.set_mode((1024, 768))
        self.visited = None

    def initialize_pygame(self):
        Initialization().draw_floor()

    def createMaze(self):
        self.parent = np.array([[None for i in range(self.size)]for j in range(self.size)])
        self.maze = [[[1 for i in range(4)] for i in range(self.size)] for j in range(self.size)]
        self.visited = np.array([[False for i in range(self.size)]for j in range(self.size)])
        #print(self.maze)
        self.dfs(0, 0)
        #print(self.visited)
        return self.maze

    def dfs(self, s, t):
        self.visited[s, t] = True
        way = [0, 1, 2, 3]
        while(len(way) > 0):
            k = random.choice(way)
            way.remove(k)
            s1 = s + self.dx[k]
            t1 = t + self.dy[k]
            if(s1 >= 0 and s1 < self.size and t1 >= 0 and t1 < self.size and self.visited[s1,t1] == False):
                self.maze[s][t][k] = 0
                if k == 0: self.maze[s1][t1][2] = 0    
                if k == 1: self.maze[s1][t1][3] = 0   
                if k == 2: self.maze[s1][t1][0] = 0   
                if k == 3: self.maze[s1][t1][1] = 0                 
                self.dfs(s1, t1)

    def draw_maze(self, Walls):
        # Tính toán tọa độ bắt đầu vẽ mê cung để canh chỉnh vào giữa màn hình
        maze_width = self.size * self.size
        maze_height = self.size * self.size
        start_x = (self.WINDOW_WIDTH - maze_width) // 2
        start_y = (self.WINDOW_HEIGHT - maze_height) // 2

        for x in range(self.size):
            for y in range(self.size):
                if Walls[y][x][3] == 1:  # Tường bên trái
                    pygame.draw.line(self.screen, self.black, (start_x + x * self.size, start_y + y * self.size),
                                    (start_x + x * self.size, start_y + (y + 1) * self.size))
                if Walls[y][x][2] == 1:  # Tường phía trên
                    pygame.draw.line(self.screen, self.black, (start_x + x * self.size, start_y + y * self.size),
                                    (start_x + (x + 1) * self.size, start_y + y * self.size))
                if Walls[y][x][1] == 1:  # Tường bên phải
                    pygame.draw.line(self.screen, self.black, (start_x + (x + 1) * self.size, start_y + y * self.size),
                                    (start_x + (x + 1) * self.size, start_y + (y + 1) * self.size))
                if Walls[y][x][0] == 1:  # Tường phía dưới
                    pygame.draw.line(self.screen, self.black, (start_x + x * self.size, start_y + (y + 1) * self.size),
                                    (start_x + (x + 1) * self.size, start_y + (y + 1) * self.size))


    def mazeApplication(self, Walls, path, color):
        maze_width = self.size * self.size
        maze_height = self.size * self.size
        start_x = (self.WINDOW_WIDTH - maze_width) // 2
        start_y = (self.WINDOW_HEIGHT - maze_height) // 2
        # Vòng lặp chính
        for i in range(len(path) - 1):
                start = (start_x + path[i][1] * self.size + self.size // 2,start_y + path[i][0] * self.size + self.size // 2)
                end = (start_x + path[i + 1][1] * self.size + self.size // 2,start_y + path[i + 1][0] * self.size + self.size // 2)
                pygame.draw.line(self.screen, color, start, end, 3)
        pygame.display.flip()
        # Đặt tốc độ hiển thị

generator = mazeGeneration()
Walls = generator.createMaze()





