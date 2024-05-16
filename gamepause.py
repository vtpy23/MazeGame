from typing import Any
import mazeGeneration as mg
import menu
import pygame
import saveLoad as sv

# class Pause:
#     def __init__(self, matrix, player_pos, player_aimbitation, player_step, time):
#         self.run_pause = True
#         self.run_exit = False
#         self.button_pause_manual = [
#         {"text": "SAVE", "pos_x": 896, "pos_y": 184},
#         {"text": "SOUND OFF", "pos_x": 896, "pos_y": 264},
#         {"text": "CHANGE SOUND", "pos_x": 896, "pos_y": 344},
#         {"text": "CHANGE THEME", "pos_x": 896, "pos_y": 424},
#         {"text": "RESUME", "pos_x": 896, "pos_y": 504},
#         {"text": "EXIT", "pos_x": 896, "pos_y": 584}]
#         self.buttons_menu_exit= [
#         {"text": "Yes", "pos_x": 448, "pos_y": 420},
#         {"text": "No", "pos_x": 576, "pos_y": 420}]
#         self.selected_button_pause_manual = 0
#         self.selected_button_exit = 0

#     def draw_pause_manual(self):
#         for i, button in enumerate(self.button_pause_manual):
#             color = (0, 0, 0) if i == self.selected_button_pause_manual else (0, 0, 255)
#             mg.Initialization().draw_text(button["text"], 36, color, button["pos_x"], button["pos_y"])
#         pygame.display.flip()

#     def handle_key_events_pause_manual(self, event):
#         if event.key == pygame.K_UP:
#             self.selected_button_pause_manual = (self.selected_button_pause_manual - 1) % len(self.button_pause_manual)
#         elif event.key == pygame.K_DOWN:
#             self.selected_button_pause_manual = (self.selected_button_pause_manual + 1) % len(self.button_pause_manual)
#         elif event.key == pygame.K_RETURN:
#             self.handle_button_click_pause_manual(self.selected_button_pause_manual)

#     def handle_mouse_events_pause_manual(self):
#         mouse_pos = pygame.mouse.get_pos()
#         for i, button in enumerate(self.button_pause_manual):
#             text_rect = mg.Initialization().draw_text(button["text"], 36, (255, 255, 0), button["pos_x"], button["pos_y"])
#             if text_rect.collidepoint(mouse_pos):
#                 self.handle_button_click_pause_manual(i)

#     def handle_button_click_pause_manual(self, index):
#         if index == 0:
#             save = sv.saveLoad()
#             save.saveGame(self.matrix, self.player_pos, self.player_aimbitation, self.player_step, self.time)
#         elif index == 1:
#             print("SOUND")
#         elif index == 2:
#             print("CHANGE SOUND")
#         elif index == 3:
#             print("CHANGE THEME")
#         elif index == 4:
#             self.run_pause = False
#         elif index == 5:
#             mg.Initialization().draw_rectangle(384, 320, 256, 128, (0, 0, 0))
#             mg.Initialization().draw_rectangle(392, 320, 248, 120, (255, 255, 255))
#             mg.Initialization().draw_text("Do you want", 28, (0, 0, 0), 512, 344)
#             mg.Initialization().draw_text("to save?", 28, (0, 0, 0), 512, 374)
#             self.run_exit = True
#             while self.run_exit:
#                 self.handle_menu_events_exit()
#                 self.draw_menu_exit()
#             self.run_pause = False

#     def handle_pause_manual_events(self):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 exit()
#             elif event.type == pygame.KEYDOWN:
#                 self.handle_key_events_pause_manual(event)
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 self.handle_mouse_events_pause_manual()
    
#     def run_pause_manual(self):
#         pause_time = pygame.time.get_ticks()
#         while self.run_pause:
#             self.handle_pause_manual_events()
#             self.draw_pause_manual()
#             seconds = (pygame.time.get_ticks() - pause_time) / 1000
#         return seconds
    
#     def draw_menu_exit(self):
#         # Vẽ nút
#         for i, button in enumerate(self.buttons_menu_exit):
#             color = (0, 255, 0) if i == self.selected_button_exit else (255, 0, 0)
#             mg.Initialization().draw_text(button["text"], 24, color, button["pos_x"], button["pos_y"])
#         pygame.display.flip()
#     def handle_key_events_exit(self, event):
#         if event.key == pygame.K_LEFT:
#             self.selected_button_exit = (self.selected_button_exit - 1) % len(self.buttons_menu_exit)
#         elif event.key == pygame.K_RIGHT:
#             self.selected_button_exit = (self.selected_button_exit + 1) % len(self.buttons_menu_exit)
#         elif event.key == pygame.K_RETURN:
#             self.handle_button_click_exit(self.selected_button_exit)
#     def handle_mouse_events_exit(self):
#         mouse_pos = pygame.mouse.get_pos()
#         for i, button in enumerate(self.buttons_menu_exit):
#             text_rect = mg.Initialization().draw_text(button["text"], 24, (0, 255, 0), button["pos_x"], button["pos_y"])
#             if text_rect.collidepoint(mouse_pos):
#                 self.handle_button_click_exit(i)
#     def handle_button_click_exit(self, index):
#         if index == 0: # i want to save before exit
#             save = sv.saveLoad()
#             save.saveGame(self.matrix, self.player_pos, self.player_aimbitation, self.player_step, self.time)
#             self.run_exit = False
#         elif index == 1: # i dont want to save before exit
#             self.run_exit = False
#     def handle_menu_events_exit(self):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 exit()
#             elif event.type == pygame.KEYDOWN:
#                 self.handle_key_events_exit(event)
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 self.handle_mouse_events_exit()
    
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