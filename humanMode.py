import pygame
import mazeGeneration as mg
from pygame.locals import *
import playAutomatically as pA
import saveLoad as sv
from sys import exit
import gamepause

screen = mg.screen
screen_width = mg.WINDOW_WIDTH
screen_height = mg.WINDOW_HEIGHT
white, black = (255, 255, 255), (0, 0, 0)


class gameManually:
    def __init__(self, size) -> None:
        self.screen = None
        self.size = size
        self.matrix = mg.mazeGeneration().createMaze(self.size)
        self.cell_size = ((768)**2 / (self.size) ** 2) ** 0.5
        self.player_pos = (0,0) #Vi tri co the thay doi
        self.player_aimbitation = (3, 3) #Vi tri dich co the thay doi va chuong trinh se tu dong tat sau khi dat den vi tri nay
        self.player_past = None
        self.player_step = 0
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
        pygame.draw.rect(screen, (255, 0, 0), (0 + 1 + self.player_pos[1] * self.cell_size 
                                               ,0 + 1 + self.player_pos[0] * self.cell_size, self.cell_size - 2, self.cell_size - 2))
        pygame.draw.rect(screen, (0, 0, 255), (0 + 1 + self.player_aimbitation[1] * self.cell_size 
                                               ,0 + 1 + self.player_aimbitation[0] * self.cell_size, self.cell_size - 2, self.cell_size - 2))
        pygame.display.flip()
    def creatingMaze(self):
        self.drawMaze()
        ###Thoi gian choi
        start_ticks = pygame.time.get_ticks() 
        ###
        running = True
        self.time_pause = None
        while running:
            seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # milisec --> sec
            mg.Initialization().draw_rectangle_with_text(824,20,140,f"time: {seconds: .2f}")
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.player_step += 1
                        self.Move(-1, 0)
                    elif event.key == pygame.K_DOWN:
                        self.player_step += 1
                        self.Move(1, 0)
                    elif event.key == pygame.K_LEFT:
                        self.player_step += 1
                        self.Move(0, -1)
                    elif event.key == pygame.K_RIGHT:
                        self.player_step += 1
                        self.Move(0, 1)
                    elif event.key == pygame.K_p:
                        pause = gamepause.Pause(self.matrix, self.player_pos, self.player_aimbitation, self.player_step, -seconds * 1000)
                        self.time_pause = pause.run_pause_manual()
                        start_ticks = start_ticks + self.time_pause * 1000
                        self.drawMaze()
                    elif event.key == pygame.K_o:
                        ### Goi y nuoc di
                        play = pA.playAutomatically().Maze_bfs_solving(self.matrix)
                        play.Bfs(self.player_pos, self.player_aimbitation)
                        path = play.Truyvet()
                        mg.mazeGeneration().mazeApplicationManual(self.matrix, path, (255,0,0))
                    elif event.key == pygame.K_c:
                        ### Tat nuoc di goi y
                        self.drawMaze()
                    elif event.key == pygame.K_ESCAPE:
                        ###pause game
                        running = False
            if(self.player_pos == self.player_aimbitation): 
                save = sv.LeaderBoard()
                save.saveWin(self.player_step, seconds)
                running = False

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
        start_x = 0
        start_y = 0
        player_x = start_x + self.player_pos[1] * self.cell_size + 1 #Hoanh do
        player_y = start_y + self.player_pos[0] * self.cell_size + 1
        player_x_past = start_x + self.player_past[1] * self.cell_size + 1
        player_y_past = start_y + self.player_past[0] * self.cell_size + 1
        pygame.draw.rect(screen, (255, 255, 255), (player_x_past, player_y_past, self.cell_size - 2, self.cell_size - 2))
        pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, self.cell_size - 2, self.cell_size - 2))
        pygame.display.flip()
        
class gameLoadManually:
    def __init__(self, save_matrix, gameInfo) -> None:
        self.screen = None
        self.gameInfo = gameInfo
        self.size = len(save_matrix)
        self.cell_size = ((768)**2 / (self.size) ** 2) ** 0.5
        self.matrix = save_matrix
        self.player_pos = tuple(gameInfo[0]) #Vi tri co the thay doi
        self.player_aimbitation = tuple(gameInfo[1]) #Vi tri dich co the thay doi va chuong trinh se tu dong tat sau khi dat den vi tri nay
        self.player_past = None
        self.player_step = gameInfo[2]
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
        pygame.draw.rect(screen, (255, 0, 0), (0 + 1 + self.player_pos[1] * self.cell_size 
                                               ,0 + 1 + self.player_pos[0] * self.cell_size, self.cell_size - 2, self.cell_size - 2))
        pygame.draw.rect(screen, (0, 0, 255), (0 + 1 + self.player_aimbitation[1] * self.cell_size 
                                               ,0 + 1 + self.player_aimbitation[0] * self.cell_size, self.cell_size - 2, self.cell_size - 2))
        pygame.display.flip()
    def creatingMaze(self):
        self.drawMaze()
        save_ticks = self.gameInfo[3]
        start_ticks = pygame.time.get_ticks() 
        time_pause = None
        running = True
        while running:
            seconds = (pygame.time.get_ticks() - start_ticks - save_ticks) / 1000  # milisec --> sec
            mg.Initialization().draw_rectangle_with_text(824,20,140,f"time: {seconds: .2f}")
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    print(self.player_pos)
                    print(self.player_aimbitation)
                    if event.key == pygame.K_UP:
                        self.player_step += 1
                        self.Move(-1, 0)
                    elif event.key == pygame.K_DOWN:
                        self.player_step += 1
                        self.Move(1, 0)
                    elif event.key == pygame.K_LEFT:
                        self.player_step += 1
                        self.Move(0, -1)
                    elif event.key == pygame.K_RIGHT:
                        self.player_step += 1
                        self.Move(0, 1)
                    elif event.key == pygame.K_o:
                        ### Goi y nuoc di
                        play = pA.playAutomatically().Maze_bfs_solving(self.matrix)
                        play.Bfs(self.player_pos, self.player_aimbitation)
                        path = play.Truyvet()
                        print(path)
                        mg.mazeGeneration().mazeApplicationManual(self.matrix, path, (255,0,0))
                    elif event.key == pygame.K_c:
                        ### Tat nuoc di goi y
                        self.drawMaze()
                    # elif event.key == pygame.K_s:
                    #     ### Luu game
                    #     save = sv.saveLoad()
                    #     save.saveGame(self.matrix, self.player_pos, self.player_aimbitation, self.player_step)
                    elif event.key == pygame.K_p:
                        pause = gamepause.Pause(self.matrix, self.player_pos, self.player_aimbitation, self.player_step, -seconds * 1000)
                        time_pause = pause.run_pause_manual()
                        self.drawMaze()
                    elif event.key == pygame.K_ESCAPE:
                        ###pause game
                        running = False
            if(self.player_pos == self.player_aimbitation): 
                save = sv.LeaderBoard()
                save.saveWin(self.player_step, seconds)
                running = False

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
        start_x = 0
        start_y = 0
        player_x = start_x + self.player_pos[1] * self.cell_size + 1 #Hoanh do
        player_y = start_y + self.player_pos[0] * self.cell_size + 1
        player_x_past = start_x + self.player_past[1] * self.cell_size + 1
        player_y_past = start_y + self.player_past[0] * self.cell_size + 1
        pygame.draw.rect(screen, (255, 255, 255), (player_x_past, player_y_past, self.cell_size - 2, self.cell_size - 2))
        pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, self.cell_size - 2, self.cell_size - 2))
        pygame.display.flip()