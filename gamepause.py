from typing import Any
import mazeGeneration as mg
import menu
import pygame
import saveLoad as sv

class Pause:
    def __init__(self, matrix, player_pos, player_aimbitation, player_step, time):
        self.matrix = matrix
        self.time = time
        self.player_pos = player_pos
        self.player_aimbitation = player_aimbitation
        self.player_step = player_step
        self.run_pause = True
        self.button_pause_manual = [
        {"text": "SAVE", "pos_x": 840, "pos_y": 224},
        {"text": "SOUND OFF", "pos_x": 840, "pos_y": 304},
        {"text": "CHANGE SOUND", "pos_x": 840, "pos_y": 384},
        {"text": "CHANGE THEME", "pos_x": 840, "pos_y": 464},
        {"text": "RESUME", "pos_x": 840, "pos_y": 544}]
        self.selected_button_pause_manual = 0
        # self.background_musics = menu.Menu().background_musics
        # self.sound_on = menu.Menu().sound_on
        # self.selected_music = menu.Menu().selected_music

    def draw_pause_manual(self):
        for i, button in enumerate(self.button_pause_manual):
            color = (0, 0, 0) if i == self.selected_button_pause_manual else (0, 0, 255)
            mg.Initialization().draw_text(button["text"], 36, color, button["pos_x"], button["pos_y"])
        pygame.display.flip()

    def handle_key_events_pause_manual(self, event):
        if event.key == pygame.K_UP:
            self.selected_button_pause_manual = (self.selected_button_pause_manual - 1) % len(self.button_pause_manual)
        elif event.key == pygame.K_DOWN:
            self.selected_button_pause_manual = (self.selected_button_pause_manual + 1) % len(self.button_pause_manual)
        elif event.key == pygame.K_RETURN:
            self.handle_button_click_pause_manual(self.selected_button_pause_manual)

    def handle_mouse_events_pause_manual(self):
        mouse_pos = pygame.mouse.get_pos()
        for i, button in enumerate(self.button_pause_manual):
            text_rect = mg.Initialization().draw_text(button["text"], 36, (255, 255, 0), button["pos_x"], button["pos_y"])
            if text_rect.collidepoint(mouse_pos):
                self.handle_button_click_pause_manual(i)

    def handle_button_click_pause_manual(self, index):
        if index == 0:
            save = sv.saveLoad()
            save.saveGame(self.matrix, self.player_pos, self.player_aimbitation, self.player_step, self.time)
        elif index == 1:
            print("SOUND")
            # menu.Menu().turn_sound_on_off()
        elif index == 2:
            print("CHANGE SOUND")
            # menu.Menu().change_sound()
        elif index == 3:
            print("CHANGE THEME")
        elif index == 4:
            self.run_pause = False

    def handle_pause_manual_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                self.handle_key_events_pause_manual(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_events_pause_manual()
    
    def run_pause_manual(self):
        pause_time = pygame.time.get_ticks()
        while self.run_pause:
            self.handle_pause_manual_events()
            self.draw_pause_manual()
            seconds = (pygame.time.get_ticks() - pause_time) / 1000
            print(seconds)
        return seconds
    
class Pause_auto:
    def __init__(self, matrix, player_pos, player_aimbitation):
        self.matrix = matrix
        self.player_pos = player_pos
        self.player_aimbitation = player_aimbitation
        self.run_pause = True
        self.button_pause_auto = [
        {"text": "SAVE", "pos_x": 840, "pos_y": 184},
        {"text": "CHANGE ALGORITHM", "pos_x": 840, "pos_y": 264},
        {"text": "SOUND OFF", "pos_x": 840, "pos_y": 344},
        {"text": "CHANGE SOUND", "pos_x": 840, "pos_y": 424},
        {"text": "CHANGE THEME", "pos_x": 840, "pos_y": 504},
        {"text": "RESUME", "pos_x": 840, "pos_y": 584}]
        self.selected_button_pause_auto = 0
    def draw_pause_auto(self):
        for i, button in enumerate(self.button_pause_auto):
            color = (0, 0, 0) if i == self.selected_button_pause_auto else (0, 0, 255)
            mg.Initialization().draw_text(button["text"], 36, color, button["pos_x"], button["pos_y"])
        pygame.display.flip()

    def handle_key_events_pause_auto(self, event):
        if event.key == pygame.K_UP:
            self.selected_button_pause_auto = (self.selected_button_pause_auto - 1) % len(self.button_pause_auto)
        elif event.key == pygame.K_DOWN:
            self.selected_button_pause_auto = (self.selected_button_pause_auto + 1) % len(self.button_pause_auto)
        elif event.key == pygame.K_RETURN:
            self.handle_button_click_pause_auto(self.selected_button_pause_auto)

    def handle_mouse_events_pause_auto(self):
        mouse_pos = pygame.mouse.get_pos()
        for i, button in enumerate(self.button_pause_auto):
            text_rect = mg.Initialization().draw_text(button["text"], 36, (255, 255, 0), button["pos_x"], button["pos_y"])
            if text_rect.collidepoint(mouse_pos):
                self.handle_button_click_pause_auto(i)

    def handle_button_click_pause_auto(self, index):
        if index == 0:
            print("SAVED")
        elif index == 1:
            print("CHANGE ALGORITHM")
        elif index == 2:
            print("SOUND")
            # self.sound_on = not self.sound_on
            # if self.sound_on == True:
            #     self.background_musics[self.selected_music].play(-1)
            #     mg.Initialization().draw_text("SOUND ON", 36, 'White', 840, 264)
            # else:   
            #     self.background_musics[self.selected_music].stop()
            #     mg.Initialization().draw_text("SOUND OFF", 36, 'White', 840, 264)
        elif index == 3:
            print("SOUND CHANGE")
            # if self.sound_on:
            #     self.background_musics[self.selected_music].stop()
            #     self.selected_music += 1
            #     if self.selected_music > 4:
            #         self.selected_music = 0
            #     self.background_musics[self.selected_music].play(-1)
        elif index == 4:
            print("CHANGE ALGORITHM")
        elif index == 5:
            self.run_pause = False

    def handle_pause_auto_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                self.handle_key_events_pause_auto(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_events_pause_auto()
    def run_pause_auto(self):
        pause_time = pygame.time.get_ticks()
        while self.run_pause:
            self.handle_pause_auto_events()
            self.draw_pause_auto()


