import pygame
import mazeGeneration as mg
from pygame.locals import *
import playAutomatically as pA
import saveLoad as sv
from sys import exit
import json as js

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
        self.mode_play = 0
        self.run_pause = False
        self.run_exit = False
        self.button_pause_manual = [
        {"text": "SAVE", "pos_x": 896, "pos_y": 304},
        {"text": "RESUME", "pos_x": 896, "pos_y": 384},
        {"text": "EXIT", "pos_x": 896, "pos_y": 464}]
        self.buttons_menu_exit = [
        {"text": "Yes", "pos_x": 448, "pos_y": 420},
        {"text": "No", "pos_x": 576, "pos_y": 420}]
        self.buttons_menu_pause_help = [
        {"text": "PAUSE (P)", "pos_x": 896, "pos_y": 344},
        {"text": "HELP (O)", "pos_x": 896, "pos_y": 424}]
        self.selected_button_pause_manual = 0
        self.selected_button_exit = 0
        self.selected_button = 0
        self.running = True
        self.background_musics = [
            pygame.mixer.Sound("audio/music1.wav"),
            pygame.mixer.Sound("audio/music2.wav"),
            pygame.mixer.Sound("audio/music3.wav"),
            pygame.mixer.Sound("audio/music4.wav"),
            pygame.mixer.Sound("audio/music5.wav")
        ]
        self.help = False

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

    # CONTROL IN GAME            
    def creatingMaze(self):
        self.draw_menu_pause_help()
        if self.mode_play == 0:
            pygame.draw.rect(screen, (255, 0, 0), (0 + 3 + self.player_pos[1] * self.cell_size 
                                                ,0 + 3 + self.player_pos[0] * self.cell_size, self.cell_size - 5, self.cell_size - 5))
            pygame.draw.rect(screen, (0, 0, 255), (0 + 3 + self.player_aimbitation[1] * self.cell_size 
                                                ,0 + 3 + self.player_aimbitation[0] * self.cell_size, self.cell_size - 5, self.cell_size - 5))
            pygame.display.flip()
        ###Thoi gian choi
        start_ticks = pygame.time.get_ticks() 
        ###
        self.time_pause = None
        while self.running:
            seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # milisec --> sec
            mg.Initialization().draw_rectangle_with_text(824, 20, 140,f"time: {seconds: .2f}")
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mouse_events_pause_help(seconds, start_ticks)    
                if event.type == pygame.KEYDOWN:
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
                        mg.Initialization().delete_pause_menu()
                        self.run_pause = True
                        self.time_pause = self.run_pause_manual(seconds)
                        start_ticks = start_ticks + self.time_pause * 1000
                        mg.Initialization().delete_pause_menu()
                        self.draw_menu_pause_help()
                    elif event.key == pygame.K_o:
                        self.help = not self.help
                        if self.help:
                            ### Goi y nuoc di
                            play = pA.playAutomatically().Maze_bfs_solving(self.matrix)
                            play.Bfs(self.player_pos, self.player_aimbitation)
                            path = play.Truyvet()
                            mg.mazeGeneration().mazeApplicationManual(self.matrix, path, (255,0,0))
                        else: 
                            ### Tat nuoc di goi y
                            self.drawMaze()
                            pygame.draw.rect(screen, (255, 0, 0), (0 + 3 + self.player_pos[1] * self.cell_size 
                                            ,0 + 3 + self.player_pos[0] * self.cell_size, self.cell_size - 5, self.cell_size - 5))
                            pygame.draw.rect(screen, (0, 0, 255), (0 + 3 + self.player_aimbitation[1] * self.cell_size 
                                            ,0 + 3 + self.player_aimbitation[0] * self.cell_size, self.cell_size - 5, self.cell_size - 5))
                            self.draw_menu_pause_help()
                    elif event.key == pygame.K_ESCAPE:
                        self.running = False
            if(self.player_pos == self.player_aimbitation): 
                save = sv.LeaderBoard()
                save.saveWin(self.player_step, seconds)
                self.running = False

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
    
    # PAUSE MENU
    def draw_pause_manual(self):
        for i, button in enumerate(self.button_pause_manual):
            color = (0, 0, 0) if i == self.selected_button_pause_manual else (0, 0, 255)
            mg.Initialization().draw_text(button["text"], 24, color, button["pos_x"], button["pos_y"])
        pygame.display.flip()

    def handle_key_events_pause_manual(self, event, time):
        if event.key == pygame.K_UP:
            self.selected_button_pause_manual = (self.selected_button_pause_manual - 1) % len(self.button_pause_manual)
        elif event.key == pygame.K_DOWN:
            self.selected_button_pause_manual = (self.selected_button_pause_manual + 1) % len(self.button_pause_manual)
        elif event.key == pygame.K_RETURN:
            self.handle_button_click_pause_manual(self.selected_button_pause_manual, time)

    def handle_mouse_events_pause_manual(self, time):
        mouse_pos = pygame.mouse.get_pos()
        for i, button in enumerate(self.button_pause_manual):
            text_rect = mg.Initialization().draw_text(button["text"], 24, (0, 0, 0), button["pos_x"], button["pos_y"])
            if text_rect.collidepoint(mouse_pos):
                self.handle_button_click_pause_manual(i, time)

    def handle_button_click_pause_manual(self, index, time):
        if index == 0:
            save = sv.saveLoad()
            save.saveGame(self.matrix, self.player_pos, self.player_aimbitation, self.player_step, time)
            mg.Initialization().draw_text("SAVE", 24, (0, 255, 0), 896, 304)
        elif index == 1:
            self.run_pause = False
        elif index == 2:
            mg.Initialization().draw_rectangle(384, 320, 256, 128, (0, 0, 0))
            mg.Initialization().draw_rectangle(392, 320, 248, 120, (255, 255, 255))
            mg.Initialization().draw_text("Do you want", 28, (0, 0, 0), 512, 344)
            mg.Initialization().draw_text("to save?", 28, (0, 0, 0), 512, 374)
            self.run_exit = True
            while self.run_exit:
                self.handle_menu_events_exit(time)
                self.draw_menu_exit()
            self.run_pause = False

    def handle_pause_manual_events(self, time):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                self.handle_key_events_pause_manual(event, time)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_events_pause_manual(time)
    
    def run_pause_manual(self, time):
        pause_time = pygame.time.get_ticks()
        while self.run_pause:
            self.handle_pause_manual_events(time)
            self.draw_pause_manual()
            seconds = (pygame.time.get_ticks() - pause_time) / 1000
        return seconds
    
    # EXIT MENU 
    def draw_menu_exit(self):
        # Vẽ nút
        for i, button in enumerate(self.buttons_menu_exit):
            color = (0, 255, 0) if i == self.selected_button_exit else (255, 0, 0)
            mg.Initialization().draw_text(button["text"], 24, color, button["pos_x"], button["pos_y"])
        pygame.display.flip()
    
    def handle_key_events_exit(self, event, time):
        if event.key == pygame.K_LEFT:
            self.selected_button_exit = (self.selected_button_exit - 1) % len(self.buttons_menu_exit)
        elif event.key == pygame.K_RIGHT:
            self.selected_button_exit = (self.selected_button_exit + 1) % len(self.buttons_menu_exit)
        elif event.key == pygame.K_RETURN:
            self.handle_button_click_exit(self.selected_button_exit, time)
    
    def handle_mouse_events_exit(self, time):
        mouse_pos = pygame.mouse.get_pos()
        for i, button in enumerate(self.buttons_menu_exit):
            text_rect = mg.Initialization().draw_text(button["text"], 24, (0, 255, 0), button["pos_x"], button["pos_y"])
            if text_rect.collidepoint(mouse_pos):
                self.handle_button_click_exit(i, time)
    
    def handle_button_click_exit(self, index, time):
        if index == 0: # i want to save before exit
            save = sv.saveLoad()
            save.saveGame(self.matrix, self.player_pos, self.player_aimbitation, self.player_step, time)
            self.run_exit = False
            self.running = False
        elif index == 1: # i dont want to save before exit
            self.run_exit = False
            self.running = False
    
    def handle_menu_events_exit(self, time):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                self.handle_key_events_exit(event, time)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_events_exit(time)
        
    # PAUSE - HELP 
    def draw_menu_pause_help(self):
        for i, button in enumerate(self.buttons_menu_pause_help):
            color = (0, 0, 255)
            mg.Initialization().draw_text(button["text"], 24, color, button["pos_x"], button["pos_y"])
        pygame.display.flip()
    def handle_mouse_events_pause_help(self, time, start_ticks):
        mouse_pos = pygame.mouse.get_pos()
        for i, button in enumerate(self.buttons_menu_pause_help):
            text_rect = mg.Initialization().draw_text(button["text"], 24, (0, 0, 255), button["pos_x"], button["pos_y"])
            if text_rect.collidepoint(mouse_pos):
                self.handle_button_click_pause_help(i, time, start_ticks)

    def handle_button_click_pause_help(self, index, time, start_ticks):
        if index == 0:
            mg.Initialization().delete_pause_menu()
            self.run_pause = True
            self.time_pause = self.run_pause_manual(time)
            start_ticks = start_ticks + self.time_pause * 1000
            mg.Initialization().delete_pause_menu()
            self.draw_menu_pause_help()
        elif index == 1:
            self.help = not self.help
            if self.help:
                play = pA.playAutomatically().Maze_bfs_solving(self.matrix)
                play.Bfs(self.player_pos, self.player_aimbitation)
                path = play.Truyvet()
                mg.mazeGeneration().mazeApplicationManual(self.matrix, path, (255,0,0))
            else:
                ### Tat nuoc di goi y
                self.drawMaze()
                pygame.draw.rect(screen, (255, 0, 0), (0 + 3 + self.player_pos[1] * self.cell_size 
                                ,0 + 3 + self.player_pos[0] * self.cell_size, self.cell_size - 5, self.cell_size - 5))
                pygame.draw.rect(screen, (0, 0, 255), (0 + 3 + self.player_aimbitation[1] * self.cell_size 
                                ,0 + 3 + self.player_aimbitation[0] * self.cell_size, self.cell_size - 5, self.cell_size - 5))
                self.draw_menu_pause_help()

        
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
        if self.mode_play == 0:
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
                    elif event.key == pygame.K_p:
                        gameManually.run_pause = True
                        time_pause = gameManually(self.size).run_pause_manual(seconds)
                        start_ticks = start_ticks + time_pause * 1000
                        mg.Initialization().delete_pause_menu()
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