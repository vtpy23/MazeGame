import random
import pygame
import mazeGeneration as mg
from pygame.locals import *
import playAutomatically as pA
import saveLoad as sv

screen = mg.screen
Walls = mg.mazeGeneration().createMaze()
screen_width = mg.WINDOW_WIDTH
screen_height = mg.WINDOW_HEIGHT
cell_size = mg.cell_size
white, black = (255, 255, 255), (0, 0, 0)


class gameManually:
    def __init__(self) -> None:
        self.screen = None
        self.size = mg.size
        self.matrix = Walls
        self.player_pos = (0,0) #Vi tri co the thay doi
        self.player_aimbitation = (3, 3) #Vi tri dich co the thay doi va chuong trinh se tu dong tat sau khi dat den vi tri nay
        self.player_past = None
    def drawMaze(self):
        size = self.size
        # Khởi tạo Pygame
        pygame.init()
        screen.fill(white)
        maze_width = size * cell_size
        maze_height = size * cell_size
        start_x = (screen_width - maze_width) // 2
        start_y = (screen_height - maze_height) // 2

        for x in range(size):
            for y in range(size):
                if self.matrix[y][x][3] == 1:  # Tường bên trái
                    pygame.draw.line(screen, black, (start_x + x * cell_size, start_y + y * cell_size),
                                    (start_x + x * cell_size, start_y + (y + 1) * cell_size))
                if self.matrix[y][x][2] == 1:  # Tường phía trên
                    pygame.draw.line(screen, black, (start_x + x * cell_size, start_y + y * cell_size),
                                    (start_x + (x + 1) * cell_size, start_y + y * cell_size))
                if self.matrix[y][x][1] == 1:  # Tường bên phải
                    pygame.draw.line(screen, black, (start_x + (x + 1) * cell_size, start_y + y * cell_size),
                                    (start_x + (x + 1) * cell_size, start_y + (y + 1) * cell_size))
                if self.matrix[y][x][0] == 1:  # Tường phía dưới
                    pygame.draw.line(screen, black, (start_x + x * cell_size, start_y + (y + 1) * cell_size),
                                    (start_x + (x + 1) * cell_size, start_y + (y + 1) * cell_size))
        pygame.draw.rect(screen, (255, 0, 0), ((screen_width - self.size * cell_size) // 2 + 3 + self.player_pos[1] * cell_size 
                                               , (screen_height - self.size * cell_size) // 2 + 3 + self.player_pos[0] * cell_size, cell_size - 5, cell_size - 5))
        pygame.display.flip()
    def creatingMaze(self):
        self.drawMaze()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.Move(-1, 0)
                    elif event.key == pygame.K_DOWN:
                        self.Move(1, 0)
                    elif event.key == pygame.K_LEFT:
                        self.Move(0, -1)
                    elif event.key == pygame.K_RIGHT:
                        self.Move(0, 1)
                    elif event.key == pygame.K_o:
                        ### Goi y nuoc di
                        play = pA.playAutomatically().Maze_bfs_solving(Walls)
                        play.Bfs(self.player_pos, self.player_aimbitation)
                        path = play.Truyvet()
                        print(path)
                        mg.mazeGeneration().mazeApplication(self.matrix, path, (255,0,0))
                    elif event.key == pygame.K_c:
                        ### Tat nuoc di goi y
                        self.drawMaze()
                    elif event.key == pygame.K_s:
                        ### Luu game
                        save = sv.saveLoad()
                        save.saveGame(self.matrix, self.player_pos, self.player_aimbitation)
                    elif event.key == pygame.K_ESCAPE:
                        running = False
            if(self.player_pos == self.player_aimbitation): running = False
        pygame.quit()

    def Move(self, dx, dy):
        # Kiểm tra xem người chơi có thể di chuyển đến ô mới không
        new_x = self.player_pos[0] + dx
        new_y = self.player_pos[1] + dy
        move = [(1,0), (0,1), (-1,0), (0,-1)]
        k = move.index((dx, dy))
        if 0 <= new_x < self.size and 0 <= new_y < self.size:
            # Kiểm tra xem ô mới có là tường không
            if  self.matrix[self.player_pos[0]][self.player_pos[1]][k] == 0:
                # Cập nhật vị trí mới của người chơi
                self.player_past = self.player_pos
                self.player_pos = (new_x, new_y)
                # Vẽ lại màn hình với vị trí mới của người chơi
                self.draw_player()

    def draw_player(self):
        # Vẽ hình vuông đại diện cho người chơi
        start_x = (screen_width - self.size * cell_size) // 2 + 3
        start_y = (screen_height - self.size * cell_size) // 2 + 3
        player_x = start_x + self.player_pos[1] * cell_size #Hoanh do
        player_y = start_y + self.player_pos[0] * cell_size
        player_x_past = start_x + self.player_past[1] * cell_size
        player_y_past = start_y + self.player_past[0] * cell_size
        pygame.draw.rect(screen, (255, 255, 255), (player_x_past, player_y_past, cell_size - 5, cell_size - 5))
        pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, cell_size - 5, cell_size - 5))
        pygame.display.flip()
        
