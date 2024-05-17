import pygame
import mazeGeneration as mg 
import saveLoad as sv
from sys import exit
from humanMode import gameManually
from autoMode import gameAutomatically
from humanMode import gameLoadManually
import json as js
# Các hằng số
FONT_PATH = 'font/Pixeltype.TTF'
screen = mg.screen
pygame.display.set_caption("Maze Game")
font = pygame.font.Font(FONT_PATH, 50)
WINDOW_HEIGHT = mg.WINDOW_HEIGHT
WINDOW_WIDTH = mg.WINDOW_WIDTH
screen_color = (0, 0, 150)

class Menu:
    def __init__(self):
        self.buttons_menu = [
        {"text": "START", "pos_x": 840, "pos_y": 144},
        {"text": "LOAD", "pos_x": 840, "pos_y": 224},
        {"text": "LEADER", "pos_x": 840, "pos_y": 289},
        {"text": "SETTING", "pos_x": 840, "pos_y": 384},
        {"text": "GUIDE", "pos_x": 840, "pos_y": 464},
        {"text": "CREDITS", "pos_x": 840, "pos_y": 544},
        {"text": "QUIT", "pos_x": 840, "pos_y": 624}
        ]
        self.buttons_menu_start = [
        {"text": "MANUAL", "pos_x": 840, "pos_y": 304},
        {"text": "AUTOMATIC", "pos_x": 840, "pos_y": 384},
        {"text": "BACK", "pos_x": 840, "pos_y": 464}
        ]
        self.buttons_menu_setting_on = [
        {"text": "SOUND OFF", "pos_x": 840, "pos_y": 264},
        {"text": "CHANGE", "pos_x": 840, "pos_y": 329},
        {"text": "CHANGE", "pos_x": 840, "pos_y": 409},
        {"text": "BACK", "pos_x": 840, "pos_y": 504}
        ]
        self.buttons_menu_setting_off = [
        {"text": "SOUND ON", "pos_x": 840, "pos_y": 264},
        {"text": "CHANGE", "pos_x": 840, "pos_y": 329},
        {"text": "CHANGE", "pos_x": 840, "pos_y": 409},
        {"text": "BACK", "pos_x": 840, "pos_y": 504}
        ]
        self.buttons_menu_leader_board = [
        {"text": "PLAYER", "pos_x": 840, "pos_y": 264},
        {"text": "AVERGAGE", "pos_x": 840, "pos_y": 329},
        {"text": "AVERGAGE", "pos_x": 840, "pos_y": 409},
        {"text": "BACK", "pos_x": 840, "pos_y": 504}
        ]
        self.buttons_menu_load = [
        {"text": "BACK", "pos_x": 840, "pos_y": 124},
        {"text": "FILE_SAVE", "pos_x": 840, "pos_y": 204}
        ]
        self.buttons_menu_guide_credits = [
        {"text": "BACK", "pos_x": 840, "pos_y": 384}
        ]
        self.buttons_menu_sizemap = [
        {"text": "MAP", "pos_x": 840, "pos_y": 219},
        {"text": "MAP", "pos_x": 840, "pos_y": 319},
        {"text": "MAP", "pos_x": 840, "pos_y": 419},
        {"text": "BACK", "pos_x": 840, "pos_y": 534}
        ]
        self.buttons_menu_random_custom = [
        {"text": "RANDOM", "pos_x": 840, "pos_y": 304},
        {"text": "CUSTOM", "pos_x": 840, "pos_y": 384},
        {"text": "BACK", "pos_x": 840, "pos_y": 464}    
        ]
        self.file_save_name = sv.saveLoad().takeNameFile()
        self.buttons_file_load = [
            {"text": name, "pos_x": 250, "pos_y": 124 + 40 * i}
            for i, name in enumerate(self.file_save_name)
        ]
        self.selected_button_leader_board = 0
        self.selected_button_random_custom = 0
        self.selected_button_menu = 0
        self.selected_button_setting = 0
        self.selected_button_load_guide_credits = 0
        self.selected_button_load_file = 0
        self.selected_button_start = 0
        self.selected_button_sizemap = 0
        self.selected_music = 0
        self.selected_load = False # chon giua load ben trai va ben phai
        self.run_leader_board = False
        self.run_random_custom = False
        self.run_start = False
        self.run_setting = False
        self.run_load = False
        self.run_guide = False
        self.run_credits = False
        self.run_sizemap = False
        self.background_musics = [
            pygame.mixer.Sound("audio/music1.wav"),
            pygame.mixer.Sound("audio/music2.wav"),
            pygame.mixer.Sound("audio/music3.wav"),
            pygame.mixer.Sound("audio/music4.wav"),
            pygame.mixer.Sound("audio/music5.wav")
        ]
        with open("sound_status.json", encoding="utf-8") as fi:
                data = js.load(fi)
                self.sound_on = bool(data["status"])
                self.selected_music = int(data["song"])
        self.background_musics[self.selected_music].play(-1)

    # SOUND ON/OFF
    def turn_sound_on_off(self, text_color, text_x, text_y):
            with open("sound_status.json", encoding="utf-8") as fi:
                data = js.load(fi)
                self.sound_on = bool(data["status"])
                self.selected_music = int(data["song"])
                self.sound_on = not self.sound_on
                data["status"] = self.sound_on
                with open("sound_status.json", 'w') as file:
                    js.dump(data, file, indent=4)
            if self.sound_on == True:
                self.background_musics[self.selected_music].play(-1)
                mg.Initialization().draw_text("SOUND ON", 36, text_color, text_x, text_y)
            else:   
                self.background_musics[self.selected_music].stop()
                mg.Initialization().draw_text("SOUND OFF", 36, text_color, text_x, text_y)

    # CHANGE SOUND
    def change_sound(self):
        if self.sound_on:
                self.background_musics[self.selected_music].stop()
                self.selected_music += 1
                if self.selected_music > 4:
                    self.selected_music = 0
                try:
                    with open("sound_status.json", "r") as fr:
                        sound = js.load(fr)
                    sound_status = sound[0]
                except:
                    sound_status = {'status': True, 'song': 0}
                sound_status['song'] = self.selected_music
                with open("sound_status.json", "w") as fw:
                    js.dump([sound_status], fw, indent= 4)
                self.background_musics[self.selected_music].play(-1)
                
    # RANDOM / CUSTOM
    def draw_menu_random_custom(self):
        for i, button in enumerate(self.buttons_menu_random_custom):
            color = (255, 255, 255) if i == self.selected_button_random_custom else (255, 255, 0)
            mg.Initialization().draw_text(button["text"], 36, color, button["pos_x"], button["pos_y"])
        pygame.display.flip()
    def handle_key_events_random_custom(self, event, sizemap, mode):
        if event.key == pygame.K_UP:
            self.selected_button_random_custom = (self.selected_button_random_custom - 1) % len(self.buttons_menu_random_custom)
        elif event.key == pygame.K_DOWN:
            self.selected_button_random_custom = (self.selected_button_random_custom + 1) % len(self.buttons_menu_random_custom)
        elif event.key == pygame.K_RETURN:
            self.handle_button_click_random_custom(self.selected_button_random_custom, sizemap, mode)
    def handle_mouse_events_random_custom(self, sizemap, mode):
        mouse_pos = pygame.mouse.get_pos()
        for i, button in enumerate(self.buttons_menu_random_custom):
            text_rect = mg.Initialization().draw_text(button["text"], 36, (255, 255, 0), button["pos_x"], button["pos_y"])
            if text_rect.collidepoint(mouse_pos):
                self.handle_button_click_random_custom(i, sizemap, mode)
    def handle_button_click_random_custom(self, index, sizemap, mode):
        if index == 0:
            if mode == 0:
                if sizemap == 0: # map: 20x20, mode: manual, start point - end point: random
                    play = gameManually(20)
                    play.mode_play = 0
                    play.drawMaze()
                    play.creatingMaze()
                    mg.Initialization().draw_floor()
                    mg.Initialization().draw_to_delete("")
                    mg.Initialization().draw_text("START POINT - END POINT", 48, (255, 255, 0), 384, 42)
                elif sizemap == 1: # map: 40x40, mode: manual, start point - end point: random
                    play = gameManually(40)
                    play.mode_play = 0
                    play.drawMaze()
                    play.creatingMaze()
                    mg.Initialization().draw_floor()
                    mg.Initialization().draw_to_delete("")
                    mg.Initialization().draw_text("START POINT - END POINT", 48, (255, 255, 0), 384, 42)
                elif sizemap == 2: # map: 100x100, mode: manual, start point - end point: random
                    play = gameManually(100)
                    play.mode_play = 0
                    play.drawMaze()
                    play.creatingMaze()
                    mg.Initialization().draw_floor()
                    mg.Initialization().draw_to_delete("")
                    mg.Initialization().draw_text("START POINT - END POINT", 48, (255, 255, 0), 384, 42)
            elif mode == 1:
                if sizemap == 0: # map: 40x40, mode: auto, start point - end point: random
                    play = gameAutomatically(20)
                    play.mode_play = 0
                    play.creatingMaze()
                    mg.Initialization().draw_floor()
                    mg.Initialization().draw_to_delete("")
                    mg.Initialization().draw_text("START POINT - END POINT", 48, (255, 255, 0), 384, 42)                    
                elif sizemap == 1: # map: 40x40, mode: auto, start point - end point: random
                    play = gameAutomatically(40)
                    play.mode_play = 0
                    play.creatingMaze()
                    mg.Initialization().draw_floor()
                    mg.Initialization().draw_to_delete("")
                    mg.Initialization().draw_text("START POINT - END POINT", 48, (255, 255, 0), 384, 42)                    
                elif sizemap == 2: # map: 40x40, mode: auto, start point - end point: random
                    play = gameAutomatically(100)
                    play.mode_play = 0
                    play.creatingMaze()
                    mg.Initialization().draw_floor()
                    mg.Initialization().draw_to_delete("")
                    mg.Initialization().draw_text("START POINT - END POINT", 48, (255, 255, 0), 384, 42)                    
        elif index == 1:
            if mode == 0:
                if sizemap == 0: # map: 20x20, mode: manual, start point - end point: custom
                    play = gameManually(20)
                    play.mode_play = 1
                    play.drawMaze()
                    play.choose_start_end_point(20)
                    play.creatingMaze()
                    mg.Initialization().draw_floor()
                    mg.Initialization().draw_to_delete("")
                    mg.Initialization().draw_text("START POINT - END POINT", 48, (255, 255, 0), 384, 42)
                elif sizemap == 1: # map: 40x40, mode: manual, start point - end point: custom
                    play = gameManually(40)
                    play.mode_play = 1
                    play.drawMaze()
                    play.choose_start_end_point(40)
                    play.creatingMaze()
                    mg.Initialization().draw_floor()
                    mg.Initialization().draw_to_delete("")
                    mg.Initialization().draw_text("START POINT - END POINT", 48, (255, 255, 0), 384, 42)                   
                elif sizemap == 2: # map: 100x100, mode: manual, start point - end point: custom
                    play = gameManually(100)
                    play.mode_play = 1
                    play.drawMaze()
                    play.choose_start_end_point(100)
                    play.creatingMaze()
                    mg.Initialization().draw_floor()
                    mg.Initialization().draw_to_delete("")
                    mg.Initialization().draw_text("START POINT - END POINT", 48, (255, 255, 0), 384, 42)
            elif mode == 1:
                if sizemap == 0: # map: 20x20, mode: auto, start point - end point: custom
                    play = gameAutomatically(20)
                    play.mode_play = 1
                    play.drawMaze()
                    play.choose_start_end_point(20)
                    play.creatingMaze()
                    mg.Initialization().draw_floor()
                    mg.Initialization().draw_to_delete("")
                    mg.Initialization().draw_text("START POINT - END POINT", 48, (255, 255, 0), 384, 42)                    
                elif sizemap == 1: # map: 20x20, mode: auto, start point - end point: custom
                    play = gameAutomatically(40)
                    play.mode_play = 1
                    play.drawMaze()
                    play.choose_start_end_point(40)
                    play.creatingMaze()
                    mg.Initialization().draw_floor()
                    mg.Initialization().draw_to_delete("")
                    mg.Initialization().draw_text("START POINT - END POINT", 48, (255, 255, 0), 384, 42)                    
                elif sizemap == 2: # map: 20x20, mode: auto, start point - end point: custom
                    play = gameAutomatically(100)
                    play.mode_play = 1
                    play.drawMaze()
                    play.choose_start_end_point(100)
                    play.creatingMaze()
                    mg.Initialization().draw_floor()
                    mg.Initialization().draw_to_delete("")
                    mg.Initialization().draw_text("START POINT - END POINT", 48, (255, 255, 0), 384, 42)                    
        elif index == 2:
            self.run_random_custom = False
    def handle_menu_events_random_custom(self, sizemap, mode):     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                self.handle_key_events_random_custom(event, sizemap, mode)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_events_random_custom(sizemap, mode)       
    # Size maze
    def draw_menu_sizemaze(self):
        # Vẽ nút
        for i, button in enumerate(self.buttons_menu_sizemap):
            color = (255, 255, 255) if i == self.selected_button_sizemap else (255, 255, 0)
            mg.Initialization().draw_text(button["text"], 36, color, button["pos_x"], button["pos_y"])
            if i == 0:
                mg.Initialization().draw_text("20x20", 36, color, 840, 249)
            elif i == 1:
                mg.Initialization().draw_text("40x40", 36, color, 840, 349)
            elif i == 2:
                mg.Initialization().draw_text("100x100", 36, color, 840, 449)
        pygame.display.flip()
    def handle_key_events_sizemap(self, event, mode):
        if event.key == pygame.K_UP:
            self.selected_button_sizemap = (self.selected_button_sizemap - 1) % len(self.buttons_menu_sizemap)
        elif event.key == pygame.K_DOWN:
            self.selected_button_sizemap = (self.selected_button_sizemap + 1) % len(self.buttons_menu_sizemap)
        elif event.key == pygame.K_RETURN:
            self.handle_button_click_sizemap(self.selected_button_sizemap, mode)
    def handle_mouse_events_sizemap(self, mode):
        mouse_pos = pygame.mouse.get_pos()
        for i, button in enumerate(self.buttons_menu_sizemap):
            text_rect = mg.Initialization().draw_text(button["text"], 36, (255, 255, 0), button["pos_x"], button["pos_y"])
            if text_rect.collidepoint(mouse_pos):
                self.handle_button_click_sizemap(i, mode)
    def handle_button_click_sizemap(self, index, mode):
        if index == 0: # 20 x 20
            mg.Initialization().draw_to_delete("")
            mg.Initialization().draw_text("START POINT - END POINT", 48, (255, 255, 0), 384, 42)
            self.run_random_custom = True
            while self.run_random_custom:
                self.handle_menu_events_random_custom(index, mode)
                self.draw_menu_random_custom()
            mg.Initialization().draw_floor()
            mg.Initialization().draw_to_delete("CHOOSE SIZE MAP")
        elif index == 1: # 40 x 40
            mg.Initialization().draw_to_delete("")
            mg.Initialization().draw_text("START POINT - END POINT", 48, (255, 255, 0), 384, 42)
            self.run_random_custom = True
            while self.run_random_custom:
                self.handle_menu_events_random_custom(index, mode)
                self.draw_menu_random_custom()
            mg.Initialization().draw_floor()
            mg.Initialization().draw_to_delete("CHOOSE SIZE MAP")
        elif index == 2: # 100 x 100
            mg.Initialization().draw_to_delete("")
            mg.Initialization().draw_text("START POINT - END POINT", 48, (255, 255, 0), 384, 42)
            self.run_random_custom = True
            while self.run_random_custom:
                self.handle_menu_events_random_custom(index, mode)
                self.draw_menu_random_custom()
            mg.Initialization().draw_floor()
            mg.Initialization().draw_to_delete("CHOOSE SIZE MAP")
        elif index == 3:
            self.run_sizemap = False
    def handle_menu_events_sizemap(self, mode):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                self.handle_key_events_sizemap(event, mode)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_events_sizemap(mode)
    # Main menu
    def draw_menu(self):
        # Vẽ nút
        for i, button in enumerate(self.buttons_menu):
            color = (255, 255, 255) if i == self.selected_button_menu else (255, 255, 0)
            mg.Initialization().draw_text(button["text"], 36, color, button["pos_x"], button["pos_y"])
            if i == 2:
                mg.Initialization().draw_text("BOARD", 36, color, 840, 319)
        pygame.display.flip()
    def handle_key_events(self, event):
        if event.key == pygame.K_UP:
            self.selected_button_menu = (self.selected_button_menu - 1) % len(self.buttons_menu)
        elif event.key == pygame.K_DOWN:
            self.selected_button_menu = (self.selected_button_menu + 1) % len(self.buttons_menu)
        elif event.key == pygame.K_RETURN:
            self.handle_button_click(self.selected_button_menu)
    def handle_mouse_events(self):
        mouse_pos = pygame.mouse.get_pos()
        for i, button in enumerate(self.buttons_menu):
            text_rect = mg.Initialization().draw_text(button["text"], 36, (255, 255, 0), button["pos_x"], button["pos_y"])
            if text_rect.collidepoint(mouse_pos):
                self.handle_button_click(i)
    def handle_button_click(self, index):
        if index == 0:
            mg.Initialization().draw_to_delete("CHOOSE MODE")
            self.run_start = True
            while self.run_start:
                self.handle_menu_events_start()
                self.draw_menu_start()
            mg.Initialization().draw_floor()
        elif index == 1:
            self.file_save_name = sv.saveLoad().takeNameFile()
            self.buttons_file_load = [
                {"text": name, "pos_x": 250, "pos_y": 124 + 40 * i}
                for i, name in enumerate(self.file_save_name)
            ]
            self.run_load = True
            mg.Initialization().draw_to_delete("LOAD")
            while self.run_load:
                self.handle_menu_events_load()
                self.draw_menu_load()
            mg.Initialization().draw_floor()
        elif index == 3:
            mg.Initialization().draw_to_delete("SETTING")
            self.run_setting = True
            while self.run_setting:
                self.handle_menu_events_setting()
                self.draw_menu_setting()
            mg.Initialization().draw_floor()
        elif index == 2:
            mg.Initialization().draw_to_delete("LEADER BOARD")
            self.run_leader_board = True
            while self.run_leader_board:
                self.handle_menu_events_leader_board()
                self.draw_menu_leader_board()
            mg.Initialization().draw_floor()
        elif index == 4:
            mg.Initialization().draw_to_delete("GUIDE")
            self.run_guide = True
            while self.run_guide:
                self.handle_menu_events_guide()
                self.draw_menu_guide()
            mg.Initialization().draw_floor()
        elif index == 5:
            mg.Initialization().input_image_background("image/credit.png")
            mg.Initialization().draw_to_delete("Credits")
            self.run_credits = True
            while self.run_credits:
                self.handle_menu_events_credits()
                self.draw_menu_credits()
            mg.Initialization().draw_floor()
        elif index == 6:
            pygame.quit()
            exit()
    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                self.handle_key_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_events()

    # Start - CHOOSE MODE
    def draw_menu_start(self):
        # Vẽ nút
        for i, button in enumerate(self.buttons_menu_start):
            color = (255, 255, 255) if i == self.selected_button_start else (255, 255, 0)
            mg.Initialization().draw_text(button["text"], 36, color, button["pos_x"], button["pos_y"])
        pygame.display.flip()
    def handle_key_events_start(self, event):
        if event.key == pygame.K_UP:
            self.selected_button_start = (self.selected_button_start - 1) % len(self.buttons_menu_start)
        elif event.key == pygame.K_DOWN:
            self.selected_button_start = (self.selected_button_start + 1) % len(self.buttons_menu_start)
        elif event.key == pygame.K_RETURN:
            self.handle_button_click_start(self.selected_button_start)
    def handle_mouse_events_start(self):
        mouse_pos = pygame.mouse.get_pos()
        for i, button in enumerate(self.buttons_menu_start):
            text_rect = mg.Initialization().draw_text(button["text"], 36, (255, 255, 0), button["pos_x"], button["pos_y"])
            if text_rect.collidepoint(mouse_pos):
                self.handle_button_click_start(i)
    def handle_button_click_start(self, index):
        if index == 0:
            mg.Initialization().draw_to_delete("CHOOSE SIZE MAP")
            self.run_sizemap = True
            while self.run_sizemap:
                self.handle_menu_events_sizemap(index)
                self.draw_menu_sizemaze()
            mg.Initialization().draw_floor()
            mg.Initialization().draw_to_delete("CHOOSE MODE")
        elif index == 1:
            mg.Initialization().draw_to_delete("CHOOSE SIZE MAP")
            self.run_sizemap = True
            while self.run_sizemap:
                self.handle_menu_events_sizemap(index)
                self.draw_menu_sizemaze()
            mg.Initialization().draw_floor()
            mg.Initialization().draw_to_delete("CHOOSE MODE")
        elif index == 2:
            self.run_start = False
    def handle_menu_events_start(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                self.handle_key_events_start(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_events_start()

    # Load
    ###Cac bien duoc dat o day khi nao lam xong se sua
    #self.file_save_name = sv.saveLoad().takeNameFile()
    def draw_menu_load(self):
        # Vẽ nút
        for i, button in enumerate(self.buttons_menu_load ):
            color = (255, 255, 255) if i == self.selected_button_load_guide_credits else (255, 255, 0)
            mg.Initialization().draw_text(button["text"], 36, color, button["pos_x"], button["pos_y"])
        pygame.display.flip()
        #Ve game save
        for i, button in enumerate(self.buttons_file_load):
            color = (0, 255, 0) if i == self.selected_button_load_file else (0, 0, 255)
            mg.Initialization().draw_text(button["text"], 36, color, button["pos_x"], button["pos_y"])
        pygame.display.flip()
    def handle_key_events_load(self, event):
        if self.selected_load == False:
            if event.key == pygame.K_RETURN:
                self.handle_button_click_load_right(self.selected_button_load_guide_credits)
            elif event.key == pygame.K_UP:
                self.selected_button_load_guide_credits = (self.selected_button_load_guide_credits - 1) % len(self.buttons_menu_load)
            elif event.key == pygame.K_DOWN:
                self.selected_button_load_guide_credits = (self.selected_button_load_guide_credits + 1) % len(self.buttons_menu_load)
        elif self.selected_load == True:
            if event.key == pygame.K_RETURN:
                self.handle_button_click_load_left(self.selected_button_load_file)
            elif event.key == pygame.K_UP:
                self.selected_button_load_file = (self.selected_button_load_file - 1) % len(self.buttons_file_load)
            elif event.key == pygame.K_DOWN:
                self.selected_button_load_file = (self.selected_button_load_file + 1) % len(self.buttons_file_load)
    def handle_mouse_events_load(self):
        mouse_pos = pygame.mouse.get_pos()
        for i, button in enumerate(self.buttons_menu_load):
            text_rect = mg.Initialization().draw_text(button["text"], 36, (255, 255, 0), button["pos_x"], button["pos_y"])
            if text_rect.collidepoint(mouse_pos):
                self.handle_button_click_load_right(i)
        for i, button in enumerate(self.buttons_file_load):
            text_rect = mg.Initialization().draw_text(button["text"], 36, (255, 255, 0), button["pos_x"], button["pos_y"])
            if text_rect.collidepoint(mouse_pos):
                self.handle_button_click_load_left(i)
    def handle_button_click_load_right(self, index):
        if(index == 0):
            self.run_load = False
        if(index == 1):
            self.file_save_name = sv.saveLoad().takeNameFile()
            print(self.file_save_name)
    def handle_button_click_load_left(self, index):
        matrix, gameInfo = sv.saveLoad().loadGame(index + 1)
        play = gameLoadManually(matrix, gameInfo)
        play.creatingMaze()
        mg.Initialization().draw_load()
    def handle_menu_events_load(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.selected_load = True
                elif event.key == pygame.K_RIGHT:
                    self.selected_load = False
                self.handle_key_events_load(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_events_load()

    # Setting
    def draw_menu_setting(self):
        if self.sound_on == True:
            self.buttons_menu_setting = self.buttons_menu_setting_on
        else: 
            self.buttons_menu_setting = self.buttons_menu_setting_off
        # Vẽ nút
        for i, button in enumerate(self.buttons_menu_setting):
            color = (255, 255, 255) if i == self.selected_button_setting else (255, 255, 0)
            mg.Initialization().draw_text(button["text"], 36, color, button["pos_x"], button["pos_y"])
            if i == 1:
                mg.Initialization().draw_text("SOUND", 36, color, 840, 359)
            elif i == 2:
                mg.Initialization().draw_text("THEME", 36, color, 840, 439)
        pygame.display.flip()
    def handle_key_events_setting(self, event):
        if event.key == pygame.K_UP:
            self.selected_button_setting = (self.selected_button_setting - 1) % len(self.buttons_menu_setting)
        elif event.key == pygame.K_DOWN:
            self.selected_button_setting = (self.selected_button_setting + 1) % len(self.buttons_menu_setting)
        elif event.key == pygame.K_RETURN:
            self.handle_button_click_setting(self.selected_button_setting)
    def handle_mouse_events_setting(self):
        mouse_pos = pygame.mouse.get_pos()
        for i, button in enumerate(self.buttons_menu_setting):
            text_rect = mg.Initialization().draw_text(button["text"], 36, (255, 255, 0), button["pos_x"], button["pos_y"])
            if text_rect.collidepoint(mouse_pos):
                self.handle_button_click_setting(i)
    def handle_button_click_setting(self, index):
        if index == 0:
            self.turn_sound_on_off(screen_color, 840, 264)
        elif index == 1:
            self.change_sound()
        elif index == 2:
            print("change theme")
        elif index == 3:
            self.run_setting = False
    def handle_menu_events_setting(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                self.handle_key_events_setting(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_events_setting()

    # Guide
    def draw_menu_guide(self):
        # Vẽ nút
        for i, button in enumerate(self.buttons_menu_guide_credits):
            color = (255, 255, 255) if i == self.selected_button_load_guide_credits else (255, 255, 0)
            mg.Initialization().draw_text(button["text"], 36, color, button["pos_x"], button["pos_y"])
        pygame.display.flip()
    def handle_key_events_guide(self, event):
        if event.key == pygame.K_RETURN:
            self.run_guide = False
    def handle_mouse_events_guide(self):
        mouse_pos = pygame.mouse.get_pos()
        for i, button in enumerate(self.buttons_menu_guide_credits):
            text_rect = mg.Initialization().draw_text(button["text"], 36, (255, 255, 0), button["pos_x"], button["pos_y"])
            if text_rect.collidepoint(mouse_pos):
                self.run_guide = False
    def handle_button_click_guide(self, index):
        name = 1
    def handle_menu_events_guide(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                self.handle_key_events_guide(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_events_guide()

    # LEADER BOARD
    def draw_menu_leader_board(self):
        # Vẽ nút
        for i, button in enumerate(self.buttons_menu_leader_board):
            color = (255, 255, 255) if i == self.selected_button_leader_board else (255, 255, 0)
            mg.Initialization().draw_text(button["text"], 36, color, button["pos_x"], button["pos_y"])
            if i == 1:
                mg.Initialization().draw_text("TIME", 36, color, 840, 359)
            elif i == 2:
                mg.Initialization().draw_text("STEP", 36, color, 840, 439)
        pygame.display.flip()
    def handle_key_events_leader_board(self, event):
        if event.key == pygame.K_UP:
            self.selected_button_leader_board = (self.selected_button_leader_board - 1) % len(self.buttons_menu_leader_board)
        elif event.key == pygame.K_DOWN:
            self.selected_button_leader_board = (self.selected_button_leader_board + 1) % len(self.buttons_menu_leader_board)
        elif event.key == pygame.K_RETURN:
            self.handle_button_click_leader_board(self.selected_button_leader_board)
    def handle_mouse_events_leader_board(self):
        mouse_pos = pygame.mouse.get_pos()
        for i, button in enumerate(self.buttons_menu_leader_board):
            text_rect = mg.Initialization().draw_text(button["text"], 36, (255, 255, 0), button["pos_x"], button["pos_y"])
            if text_rect.collidepoint(mouse_pos):
                self.handle_button_click_leader_board(i)
    def handle_button_click_leader_board(self, index):
        if index == 0:
            print("information")
        elif index == 1:
            mg.Initialization().input_image_background("image/bg_line.png")
            mg.Initialization().draw_text_2("USER", 30, (0, 0, 0), 200, 190)
            mg.Initialization().draw_text_2("AVG_TIME", 30, (0, 0, 0), 500, 190)
            top_average_time = sv.LeaderBoard().get_top(sv.LeaderBoard().sort_average_time())
            for i, button in enumerate(top_average_time):
                rank = str(i + 1) + "."
                color = (0, 0, 0)
                mg.Initialization().draw_text_2(rank, 36, color, 150, 248 + 71 * i)
                mg.Initialization().draw_text_2(str(button["name"]).encode('utf-8'), 36, color, 200, 248 + 71 * i)
                mg.Initialization().draw_text_2(str(button["average_timer"])[:5].encode('utf-8'), 36, color, 500, 248 + 71 * i)
            pygame.display.flip()
        elif index == 2: 
            mg.Initialization().input_image_background("image/bg_line.png")
            mg.Initialization().draw_text_2("USER", 30, (0, 0, 0), 200, 190)
            mg.Initialization().draw_text_2("AVG_STEP", 30, (0, 0, 0), 500, 190)
            top_average_step = sv.LeaderBoard().get_top(sv.LeaderBoard().sort_average_step())
            for i, button in enumerate(top_average_step):
                rank = str(i + 1) + "."
                color = (0, 0, 0)
                mg.Initialization().draw_text_2(rank, 36, color, 150, 248 + 71 * i)
                mg.Initialization().draw_text_2(str(button["name"]).encode('utf-8'), 36, color, 200, 248 + 71 * i)
                mg.Initialization().draw_text_2(str(button["average_step"])[:5].encode('utf-8'), 36, color, 500, 248 + 71 * i)
            pygame.display.flip()
        elif index == 3:
            self.run_leader_board = False
    def handle_menu_events_leader_board(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                self.handle_key_events_leader_board(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_events_leader_board()

    # Credits   
    def draw_menu_credits(self):
        # Vẽ nút
        for i, button in enumerate(self.buttons_menu_guide_credits):
            color = (255, 255, 255) if i == self.selected_button_load_guide_credits else (255, 255, 0)
            mg.Initialization().draw_text(button["text"], 36, color, button["pos_x"], button["pos_y"])
        pygame.display.flip()
    def handle_key_events_credits(self, event):
        if event.key == pygame.K_RETURN:
            self.run_credits = False
    def handle_mouse_events_credits(self):
        mouse_pos = pygame.mouse.get_pos()
        for i, button in enumerate(self.buttons_menu_guide_credits):
            text_rect = mg.Initialization().draw_text(button["text"], 36, (255, 255, 0), button["pos_x"], button["pos_y"])
            if text_rect.collidepoint(mouse_pos):
                self.run_credits = False
    def handle_button_click_credits(self, index):
        name = 1
    def handle_menu_events_credits(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                self.handle_key_events_credits(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_events_credits()