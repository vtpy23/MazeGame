import pygame
import mazeGeneration as mg 
from random_custom import Random_custom

class Sizemap:
    def __init__(self):
        self.buttons_menu_sizemap = [
        {"text": "MAP", "pos_x": 840, "pos_y": 219},
        {"text": "MAP", "pos_x": 840, "pos_y": 319},
        {"text": "MAP", "pos_x": 840, "pos_y": 419},
        {"text": "BACK", "pos_x": 840, "pos_y": 534}
        ]
        self.selected_button_sizemap = 0
        self.run_sizemap = False
    
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

        if self.selected_button_sizemap == 0:
            mg.Initialization().input_image_background("image/20x20.jpg")
        elif self.selected_button_sizemap == 1:
            mg.Initialization().input_image_background("image/40x40.jpg")
        elif self.selected_button_sizemap == 2:
            mg.Initialization().input_image_background("image/100x100.jpg")
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
            mg.Initialization().input_image_background("image/floor_bg.png")
            Random_custom().run_menu_random_custom(index, mode)
            mg.Initialization().draw_floor()
            mg.Initialization().draw_to_delete("CHOOSE SIZE MAP")
        elif index == 1: # 40 x 40
            mg.Initialization().draw_to_delete("")
            mg.Initialization().draw_text("START POINT - END POINT", 48, (255, 255, 0), 384, 42)
            mg.Initialization().input_image_background("image/floor_bg.png")
            Random_custom().run_menu_random_custom(index, mode)
            mg.Initialization().draw_floor()
            mg.Initialization().draw_to_delete("CHOOSE SIZE MAP")
        elif index == 2: # 100 x 100
            mg.Initialization().draw_to_delete("")
            mg.Initialization().draw_text("START POINT - END POINT", 48, (255, 255, 0), 384, 42)
            mg.Initialization().input_image_background("image/floor_bg.png")
            Random_custom().run_menu_random_custom(index, mode)
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
    
    def run_menu_sizemap(self, mode):
        self.run_sizemap = True
        while self.run_sizemap:
            self.handle_menu_events_sizemap(mode)
            self.draw_menu_sizemaze()
