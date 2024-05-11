import pygame
import mazeGeneration as mg 
import saveLoad as sv
from sys import exit
from gameplay import Gameplay
from humanMode import gameManually
from autoMode import gameAutomatically
from humanMode import gameLoadManually
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
        {"text": "START", "pos_x": 840, "pos_y": 184},
        {"text": "LOAD", "pos_x": 840, "pos_y": 264},
        {"text": "SETTING", "pos_x": 840, "pos_y": 344},
        {"text": "GUIDE", "pos_x": 840, "pos_y": 424},
        {"text": "CREDITS", "pos_x": 840, "pos_y": 504},
        {"text": "QUIT", "pos_x": 840, "pos_y": 584}
        ]
        self.buttons_menu_start = [
        {"text": "MANUAL", "pos_x": 840, "pos_y": 304},
        {"text": "AUTOMATIC", "pos_x": 840, "pos_y": 384},
        {"text": "BACK", "pos_x": 840, "pos_y": 464},
        ]
        self.buttons_menu_setting = None
        self.buttons_menu_setting_on = [
        {"text": "SOUND OFF", "pos_x": 840, "pos_y": 264},
        {"text": "CHANGE SOUND", "pos_x": 840, "pos_y": 344},
        {"text": "CHANGE THEME", "pos_x": 840, "pos_y": 424},
        {"text": "BACK", "pos_x": 840, "pos_y": 504},
        ]
        self.buttons_menu_setting_off = [
        {"text": "SOUND ON", "pos_x": 840, "pos_y": 264},
        {"text": "CHANGE SOUND", "pos_x": 840, "pos_y": 344},
        {"text": "CHANGE THEME", "pos_x": 840, "pos_y": 424},
        {"text": "BACK", "pos_x": 840, "pos_y": 504},
        ]
        self.buttons_menu_load = [
        {"text": "BACK", "pos_x": 840, "pos_y": 124},
        {"text": "FILE_SAVE", "pos_x": 840, "pos_y": 204}
        ]
        self.buttons_menu_guide_credits = [
        {"text": "BACK", "pos_x": 840, "pos_y": 384}
        ]
        self.file_save_name = sv.saveLoad().takeNameFile()
        self.buttons_file_load = [
            {"text": name, "pos_x": 250, "pos_y": 124 + 40 * i}
            for i, name in enumerate(self.file_save_name)
        ]
        self.selected_button_menu = 0
        self.selected_button_setting = 0
        self.selected_button_load_guide_credits = 0
        self.selected_button_load_file = 0
        self.selected_button_start = 0
        self.selected_music = 0
        self.selected_load = False # chon giua load ben trai va ben phai
        self.run_start = False
        self.run_setting = False
        self.run_load = False
        self.run_guide = False
        self.run_credits = False
        self.background_musics = [
            pygame.mixer.Sound("audio/music1.wav"),
            pygame.mixer.Sound("audio/music2.wav"),
            pygame.mixer.Sound("audio/music3.wav"),
            pygame.mixer.Sound("audio/music4.wav"),
            pygame.mixer.Sound("audio/music5.wav")
        ]
        self.background_musics[self.selected_music].play(-1)
        self.sound_on = True

    # Main menu
    def draw_menu(self):
        # Vẽ nút
        for i, button in enumerate(self.buttons_menu):
            color = (255, 255, 255) if i == self.selected_button_menu else (255, 255, 0)
            mg.Initialization().draw_text(button["text"], 36, color, button["pos_x"], button["pos_y"])
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
            mg.Initialization().draw_to_delete("LOAD")
            self.file_save_name = sv.saveLoad().takeNameFile()
            self.buttons_file_load = [
                {"text": name, "pos_x": 250, "pos_y": 124 + 40 * i}
                for i, name in enumerate(self.file_save_name)
            ]
            self.run_load = True
            mg.Initialization().draw_load()
            while self.run_load:
                self.handle_menu_events_load()
                self.draw_menu_load()
            mg.Initialization().draw_floor()
        elif index == 2:
            mg.Initialization().draw_to_delete("SETTING")
            self.run_setting = True
            while self.run_setting:
                self.handle_menu_events_setting()
                self.draw_menu_setting()
            mg.Initialization().draw_floor()
        elif index == 3:
            mg.Initialization().draw_to_delete("GUIDE")
            self.run_guide = True
            while self.run_guide:
                self.handle_menu_events_guide()
                self.draw_menu_guide()
            mg.Initialization().draw_floor()
        elif index == 4:
            image = pygame.image.load("image/credit.png").convert()
            screen.blit(image, (84, 84))
            mg.Initialization().draw_to_delete("Credits")
            self.run_credits = True
            while self.run_credits:
                self.handle_menu_events_credits()
                self.draw_menu_credits()
            mg.Initialization().draw_floor()
        elif index == 5:
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

    # Start
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
            play = gameManually()
            play.creatingMaze()
            mg.Initialization().draw_floor()
        elif index == 1:
            play = gameAutomatically()
            play.creatingMaze()
            mg.Initialization().draw_floor()
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
            self.sound_on = not self.sound_on
            if self.sound_on == True:
                self.background_musics[self.selected_music].play(-1)
                mg.Initialization().draw_text("SOUND ON", 36, screen_color, 840, 264)
            else:   
                self.background_musics[self.selected_music].stop()
                mg.Initialization().draw_text("SOUND OFF", 36, screen_color, 840, 264)
        elif index == 1:
            if self.sound_on:
                self.background_musics[self.selected_music].stop()
                self.selected_music += 1
                if self.selected_music > 4:
                    self.selected_music = 0
                self.background_musics[self.selected_music].play(-1)
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