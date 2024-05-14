import random
import pygame
import mazeGeneration as mg
from pygame.locals import *
import playAutomatically as pA
import saveLoad as sv

screen = mg.screen
screen_width = mg.WINDOW_WIDTH
screen_height = mg.WINDOW_HEIGHT
white, black = (255, 255, 255), (0, 0, 0)


class gameAutomatically:
   
    def __init__(self, size) -> None:
        self.screen = None
        self.size = size
        self.matrix = mg.mazeGeneration().createMaze(size)
        self.cell_size = ((768)**2 / (self.size) ** 2) ** 0.5
        self.player_pos = (0,0) #Vi tri co the thay doi
        self.player_aimbitation = (10, 10) #Vi tri dich co the thay doi va chuong trinh se tu dong tat sau khi dat den vi tri nay
        self.size = len(self.matrix)
        self.player_past = None
        self.searching_area = None
        self.mode_play = 0

    def drawMaze(self):
        size = self.size
        # Khởi tạo Pygame
        pygame.init()
        screen.fill(white)
        maze_width = size * self.cell_size
        maze_height = size * self.cell_size
        start_x = 0
        start_y = 0

        for x in range(size):
            for y in range(size):
                if self.matrix[y][x][3] == 1:  # Tường bên trái
                    pygame.draw.line(screen, black, (start_x + x * self.cell_size, start_y + y * self.cell_size),
                                    (start_x + x * self.cell_size, start_y + (y + 1) * self.cell_size))
                if self.matrix[y][x][2] == 1:  # Tường phía trên
                    pygame.draw.line(screen, black, (start_x + x * self.cell_size, start_y + y * self.cell_size),
                                    (start_x + (x + 1) * self.cell_size, start_y + y * self.cell_size))
                if self.matrix[y][x][1] == 1:  # Tường bên phải
                    pygame.draw.line(screen, black, (start_x + (x + 1) * self.cell_size, start_y + y * self.cell_size),
                                    (start_x + (x + 1) * self.cell_size, start_y + (y + 1) * self.cell_size))
                if self.matrix[y][x][0] == 1:  # Tường phía dưới
                    pygame.draw.line(screen, black, (start_x + x * self.cell_size, start_y + (y + 1) * self.cell_size),
                                    (start_x + (x + 1) * self.cell_size, start_y + (y + 1) * self.cell_size))
        pygame.display.flip()

    def creatingMaze(self):
        if self.mode_play == 0:
            pygame.draw.rect(screen, (255, 0, 0), (0 + 3 + self.player_pos[1] * self.cell_size 
                                                ,0 + 3 + self.player_pos[0] * self.cell_size, self.cell_size - 5, self.cell_size - 5))
            pygame.draw.rect(screen, (0, 0, 255), (0 + 3 + self.player_aimbitation[1] * self.cell_size 
                                                ,0 + 3 + self.player_aimbitation[0] * self.cell_size, self.cell_size - 5, self.cell_size - 5))
            pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        ### bfs
                        play = pA.playAutomatically().Maze_bfs_solving(self.matrix)
                        self.searching_area = play.Bfs(self.player_pos, self.player_aimbitation)
                        drew = pA.showPath(self.size).show_searching_area(play.searching_area)
                        path = play.Truyvet()
                        print(path)
                        path_drew = mg.mazeGeneration().mazeApplication(self.matrix, path, (0, 0, 255), drew)
                        pA.showPath(self.size).go_to_final_cell(path_drew)
                    elif event.key == pygame.K_2:
                        ### dijkstra
                        play = pA.playAutomatically().maze_dijkstra_solving(self.matrix)
                        self.searching_area = play.Dijkstra(self.player_pos, self.player_aimbitation)
                        drew = pA.showPath(self.size).show_searching_area(play.searching_area)
                        path = play.Truyvet()
                        print(path)
                        path_drew = mg.mazeGeneration().mazeApplication(self.matrix, path, (0, 0, 255), drew)
                        pA.showPath(self.size).go_to_final_cell(path_drew)
                    elif event.key == pygame.K_3:
                        ### A_star
                        play = pA.playAutomatically().A_solving(self.matrix)
                        path = play.A_star(self.player_pos, self.player_aimbitation)
                        drew = pA.showPath(self.size).show_searching_area(play.searching_area)
                        print(path)
                        path_drew = mg.mazeGeneration().mazeApplication(self.matrix, path, (0, 0, 255), drew)
                        pA.showPath(self.size).go_to_final_cell(path_drew)
                    elif event.key == pygame.K_d:
                        self.drawMaze()
                    elif event.key == pygame.K_ESCAPE:
                        #Pause game
                        running = False
            if(self.player_pos == self.player_aimbitation): running = False

    def draw_player(self):
        # Vẽ hình vuông đại diện cho người chơi
        start_x = 0
        start_y = 0
        player_x = start_x + self.player_pos[1] * self.cell_size #Hoanh do
        player_y = start_y + self.player_pos[0] * self.cell_size
        player_x_past = start_x + self.player_past[1] * self.cell_size
        player_y_past = start_y + self.player_past[0] * self.cell_size
        pygame.draw.rect(screen, (255, 255, 255), (player_x_past, player_y_past, self.cell_size - 5, self.cell_size - 5))
        pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, self.cell_size - 5, self.cell_size - 5))
        pygame.display.flip()
    
    def get_area_rec(self):
        running  = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    (x, y) = pygame.mouse.get_pos()
                    running = False
        return (int((y + 3) // self.cell_size), int((x + 3) // self.cell_size))
    
    def choose_start_end_point(self, size):
        count_point = 0
        while count_point < 2:
            if count_point == 0: 
                self.player_pos = self.get_area_rec()
                cell = pA.showPath(size)
                cell.draw_cell(self.player_pos, (255, 0, 0))
                count_point += 1
            if count_point == 1: 
                self.player_aimbitation = self.get_area_rec()
                cell = pA.showPath(size)
                cell.draw_cell(self.player_aimbitation, (0, 0, 255))
                count_point += 1
