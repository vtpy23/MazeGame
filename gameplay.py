import pygame
import mazeGeneration as mG
import playAutomatically as pA
import playManually as pM
import numpy as np

# Các hằng số
white = mG.white
black = mG.black
cell_size = mG.cell_size
WINDOW_WIDTH = mG.WINDOW_WIDTH
WINDOW_HEIGHT = mG.WINDOW_HEIGHT
screen = mG.screen
Walls = mG.Walls

# Lớp Gameplay
class Gameplay:
    def __init__(self) -> None:
        self.size = mG.size
        self.player_pos = (0, 0) #Vi tri co the thay doi
        self.player_aimbitation = (5, 0) #Vi tri dich co the thay doi va chuong trinh se tu dong tat sau khi dat den vi tri nay
        self.player_past = None
        self.buttons_gameplay = [
            {"text": "Người chơi", "rect": pygame.Rect(200, 720, 220, 70)},
            {"text": "Máy chơi", "rect": pygame.Rect(500, 720, 220, 70)},
            {"text": "Quay lại", "rect": pygame.Rect(800, 720, 220, 70)},
        ]
        self.selected_button_gameplay = 0
        self.choose_algorithm = [
            {"text": "BFS", "rect": pygame.Rect(200, 720, 220, 70)},
            {"text": "DIJKSTRA", "rect": pygame.Rect(500, 720, 220, 70)},
            {"text": "A-STAR", "rect": pygame.Rect(800, 720, 220, 70)},
        ]
        self.selected_choose_algorithm = 0
        self.game_active = False

    def creatingMaze(self):
        size = self.size
        screen.fill(white)
        maze_width = size * cell_size
        maze_height = size * cell_size
        start_x = (WINDOW_WIDTH - maze_width) // 2
        start_y = (WINDOW_HEIGHT - maze_height) // 2

        for x in range(size):
            for y in range(size):
                if Walls[y][x][3] == 1:  # Tường bên trái
                    pygame.draw.line(screen, black, (start_x + x * cell_size, start_y + y * cell_size),
                                    (start_x + x * cell_size, start_y + (y + 1) * cell_size))
                if Walls[y][x][2] == 1:  # Tường phía trên
                    pygame.draw.line(screen, black, (start_x + x * cell_size, start_y + y * cell_size),
                                    (start_x + (x + 1) * cell_size, start_y + y * cell_size))
                if Walls[y][x][1] == 1:  # Tường bên phải
                    pygame.draw.line(screen, black, (start_x + (x + 1) * cell_size, start_y + y * cell_size),
                                    (start_x + (x + 1) * cell_size, start_y + (y + 1) * cell_size))
                if Walls[y][x][0] == 1:  # Tường phía dưới
                    pygame.draw.line(screen, black, (start_x + x * cell_size, start_y + (y + 1) * cell_size),
                                    (start_x + (x + 1) * cell_size, start_y + (y + 1) * cell_size))
        pygame.draw.rect(screen, (255, 0, 0), ((WINDOW_WIDTH - self.size * cell_size) // 2 + 3 + self.player_pos[1] * cell_size 
                                               , (WINDOW_HEIGHT - self.size * cell_size) // 2 + 3 + self.player_pos[0] * cell_size, cell_size - 5, cell_size - 5))
        aim_x = (WINDOW_WIDTH - self.size * cell_size) // 2 + 3 + self.player_aimbitation[1] * cell_size
        aim_y = (WINDOW_HEIGHT - self.size * cell_size) // 2 + 3 + self.player_aimbitation[0] * cell_size
        pygame.draw.rect(screen, (0, 255, 0), (aim_x, aim_y, cell_size - 5, cell_size - 5))
        pygame.display.flip()

    def selectMode(self):
        while not self.game_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()   
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.selected_button_gameplay = (self.selected_button_gameplay - 1) % len(self.buttons_gameplay)
                    elif event.key == pygame.K_RIGHT:
                        self.selected_button_gameplay = (self.selected_button_gameplay + 1) % len(self.buttons_gameplay)
                    elif event.key == pygame.K_RETURN:
                        if self.selected_button_gameplay == 0:  # Chế độ người chơi
                            self.game_active = True
                            self.creatingMaze()
                            play = pM.playManually()
                            play.run()
                            self.game_active = False
                        elif self.selected_button_gameplay == 1:  # Chế độ máy chơi 
                            self.game_active = True
                            self.selectAlgorithm()                            
                        elif self.selected_button_gameplay == 2:  # Quay lại
                            self.game_active = True
            for i, button in enumerate(self.buttons_gameplay):
                color = (200, 200, 200) if i == self.selected_button_gameplay else (111, 196, 169)
                pygame.draw.rect(screen, color, button["rect"])
                text = pygame.font.Font('font/Pixeltype.TTF', 50).render(button["text"], True, (0, 0, 0))
                screen.blit(text, (button["rect"].x + 50, button["rect"].y + 10))
            pygame.display.flip()

    def selectAlgorithm(self):
        while self.game_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()   
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.selected_choose_algorithm = (self.selected_choose_algorithm - 1) % len(self.choose_algorithm)
                    elif event.key == pygame.K_RIGHT:
                        self.selected_choose_algorithm = (self.selected_choose_algorithm + 1) % len(self.choose_algorithm)
                    elif event.key == pygame.K_RETURN:
                        if self.selected_choose_algorithm == 0:  # chọn thuật toán BFS
                            play = pA.playAutomatically().Maze_bfs_solving()
                            play.Bfs(self.player_pos, self.player_aimbitation)
                            path = play.Truyvet()
                            mG.mazeGeneration().mazeApplication(Walls, path, (255, 0, 0))
                            self.game_active = False
                        elif self.selected_choose_algorithm == 1:  # Chọn thuật toán DIJKSTRA
                            play = pA.playAutomatically().maze_dijkstra_solving()
                            play.Dijkstra(self.player_pos, self.player_aimbitation)
                            path = play.Truyvet()
                            mG.mazeGeneration().mazeApplication(Walls, path, (0, 255, 0))
                            self.game_active = False
                        elif self.selected_choose_algorithm == 2:  # Chọn thuật toán A-STAR
                            play = pA.playAutomatically().A_solving()
                            path = play.A_star(np.array(Walls), self.player_pos, self.player_aimbitation)
                            mG.mazeGeneration().mazeApplication(Walls, path, (0, 0, 255))
                            self.game_active = False
            for i, button in enumerate(self.choose_algorithm):
                color = (200, 200, 200) if i == self.selected_choose_algorithm else (111, 196, 169)
                pygame.draw.rect(screen, color, button["rect"])
                text = pygame.font.Font('font/Pixeltype.otf', 50).render(button["text"], True, (0, 0, 0))
                screen.blit(text, (button["rect"].x + 50, button["rect"].y + 10))
            pygame.display.flip()

