import pygame
import mazeGeneration as mg 
import saveLoad as sv
from sys import exit
from mode import Mode
from load import Load
from leaderboard import LeaderBoard
from guide_credit import Guide_Credit
from humanModes2 import gameGeneral

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
        {"text": "BACK", "pos_x": 840, "pos_y": 624}
        ]
        self.buttons_menu_version = [
        {"text": "VERSION 1", "pos_x": 840, "pos_y": 304},
        {"text": "VERSION 2", "pos_x": 840, "pos_y": 384},
        {"text": "QUIT", "pos_x": 840, "pos_y": 464}
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
        self.selected_button_menu = 0
        self.selected_button_menu_version = 0
        self.selected_button_setting = 0
        self.selected_music = 0
        self.run_setting = False
        self.run_version = False
        self.run_menu = False
        self.background_musics = [
            pygame.mixer.Sound("audio/music1.wav"),
            pygame.mixer.Sound("audio/music2.wav"),
            pygame.mixer.Sound("audio/music3.wav"),
            pygame.mixer.Sound("audio/music4.wav"),
            pygame.mixer.Sound("audio/music5.wav")
        ]
        self.sound_on = True
        self.selected_music = 0
        self.background_musics[self.selected_music].play(-1)

    # SOUND ON/OFF
    def turn_sound_on_off(self):
            self.sound_on = not self.sound_on
            if self.sound_on == True:
                self.background_musics[self.selected_music].play(-1)
                mg.Initialization().draw_text("SOUND ON", 36, screen_color, 840, 264)
            else:   
                self.background_musics[self.selected_music].stop()
                mg.Initialization().draw_text("SOUND OFF", 36, screen_color, 840, 264)

    # CHANGE SOUND
    def change_sound(self):
        if self.sound_on:
            self.background_musics[self.selected_music].stop()
            self.selected_music = (self.selected_music + 1) % len(self.background_musics)
            self.background_musics[self.selected_music].play(-1)
    
    # VERSION
    def draw_menu_version(self):
        # Vẽ nút
        for i, button in enumerate(self.buttons_menu_version):
            color = (255, 255, 255) if i == self.selected_button_menu_version else (255, 255, 0)
            mg.Initialization().draw_text(button["text"], 36, color, button["pos_x"], button["pos_y"])
        pygame.display.flip()
    def handle_key_events_version(self, event):
        if event.key == pygame.K_UP:
            self.selected_button_menu_version = (self.selected_button_menu_version - 1) % len(self.buttons_menu_version)
        elif event.key == pygame.K_DOWN:
            self.selected_button_menu_version = (self.selected_button_menu_version + 1) % len(self.buttons_menu_version)
        elif event.key == pygame.K_RETURN:
            self.handle_button_click_version(self.selected_button_menu_version)
    def handle_mouse_events_version(self):
        mouse_pos = pygame.mouse.get_pos()
        for i, button in enumerate(self.buttons_menu_version):
            text_rect = mg.Initialization().draw_text(button["text"], 36, (255, 255, 0), button["pos_x"], button["pos_y"])
            if text_rect.collidepoint(mouse_pos):
                self.handle_button_click_version(i)
    def handle_button_click_version(self, index):
        if index == 0:
            mg.Initialization().draw_to_delete("MAIN MENU")
            self.run_menu = True
            while self.run_menu:
                self.handle_menu_events()
                self.draw_menu()
            mg.Initialization().draw_floor()
        elif index == 1:
            A = gameGeneral()
            A.gameplay()
            mg.Initialization().draw_floor()
        elif index == 2:
            pygame.quit()
            exit()
    def handle_menu_events_version(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                self.handle_key_events_version(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_events_version()

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
            Mode().run_menu_start()
            mg.Initialization().draw_floor()
        elif index == 1:
            self.file_save_name = sv.saveLoad().takeNameFile()
            self.buttons_file_load = [
                {"text": name, "pos_x": 250, "pos_y": 124 + 40 * i}
                for i, name in enumerate(self.file_save_name)
            ]
            self.run_load = True
            mg.Initialization().draw_to_delete("LOAD")
            Load().run_menu_load()
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
            LeaderBoard().run_menu_leader_board()
            mg.Initialization().draw_floor()
        elif index == 4:
            mg.Initialization().draw_to_delete("GUIDE")
            Guide_Credit().run_menu_guide()
            mg.Initialization().draw_floor()
        elif index == 5:
            mg.Initialization().input_image_background("image/credit.png")
            mg.Initialization().draw_to_delete("Credits")
            Guide_Credit().run_menu_credits()
            mg.Initialization().draw_floor()
        elif index == 6:
            self.run_menu = False
    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                self.handle_key_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_events()

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
        if self.selected_button_setting == 0:        
            if self.sound_on == True:
                mg.Initialization().input_image_background("image/unmute.png")
            else:
                mg.Initialization().input_image_background("image/mute.png")
        elif self.selected_button_setting == 1:
            mg.Initialization().input_image_background("image/floor_bg.png")
            name_songs = [
            {"text": "1. EXCITED", "pos_x": 300, "pos_y": 264},
            {"text": "2. DELIGHTED", "pos_x": 300, "pos_y": 324},
            {"text": "3. INTERESTED", "pos_x": 300, "pos_y": 384},
            {"text": "4. ENJOYED", "pos_x": 300, "pos_y": 444},
            {"text": "5. RELAXED", "pos_x": 300, "pos_y": 504}    
            ]
            for i, button in enumerate(name_songs):
                color = (0, 0, 255) if i == self.selected_music else (0, 0, 0)
                mg.Initialization().draw_text_2(button["text"], 36, color, button["pos_x"], button["pos_y"])
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
            self.turn_sound_on_off()
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

