from typing import Any
import mazeGeneration as mg
import menu
import pygame
import saveLoad as sv

class Pause_auto:
    def __init__(self):
        self.run_pause = True
        self.button_pause_auto = [
        {"text": "CHANGE", "pos_x": 896, "pos_y": 209},
        {"text": "SOUND OFF", "pos_x": 896, "pos_y": 304},
        {"text": "CHANGE SOUND", "pos_x": 896, "pos_y": 384},
        {"text": "CHANGE THEME", "pos_x": 896, "pos_y": 464},
        {"text": "RESUME", "pos_x": 896, "pos_y": 544}]
        self.selected_button_pause_auto = 0
    def draw_pause_auto(self):
        for i, button in enumerate(self.button_pause_auto):
            color = (255, 255, 0) if i == self.selected_button_pause_auto else (0, 0, 0)
            mg.Initialization().draw_text(button["text"], 36, color, button["pos_x"], button["pos_y"])
            if i == 0:
                mg.Initialization().draw_text("ALGORITHM", 36, color, 896, 239)
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
        if index == 0 :
            print("CHANGE ALGORITHM")
        elif index == 1:
            print("SOUND")
        elif index == 2:
            print("SOUND CHANGE")
        elif index == 3:
            print("CHANGE THEME")
        elif index == 4:
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