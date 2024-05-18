import pygame
import mazeGeneration as mg 
from sizemap import Sizemap

class Mode:
    def __init__(self):
        self.buttons_menu_start = [
        {"text": "MANUAL", "pos_x": 840, "pos_y": 304},
        {"text": "AUTOMATIC", "pos_x": 840, "pos_y": 384},
        {"text": "BACK", "pos_x": 840, "pos_y": 464}
        ]
        self.selected_button_start = 0
        self.run_start = False

    # Start - CHOOSE MODE
    def draw_menu_start(self):
        # Vẽ nút
        for i, button in enumerate(self.buttons_menu_start):
            color = (255, 255, 255) if i == self.selected_button_start else (255, 255, 0)
            mg.Initialization().draw_text(button["text"], 36, color, button["pos_x"], button["pos_y"])
        if self.selected_button_start == 0:
            mg.Initialization().input_image_background("image/arrow.png")
        elif self.selected_button_start == 1:
            mg.Initialization().input_image_background("image/algorithm.png")
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
                Sizemap().handle_menu_events_sizemap(index)
                Sizemap().draw_menu_sizemaze()
            mg.Initialization().draw_floor()
            mg.Initialization().draw_to_delete("CHOOSE MODE")
        elif index == 1:
            mg.Initialization().draw_to_delete("CHOOSE SIZE MAP")
            self.run_sizemap = True
            while self.run_sizemap:
                Sizemap().handle_menu_events_sizemap(index)
                Sizemap().draw_menu_sizemaze()
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