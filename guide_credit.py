import pygame
import mazeGeneration as mg
class Guide_Credit:
    def __init__(self):
        self.buttons_menu_guide_credits = [
        {"text": "BACK", "pos_x": 840, "pos_y": 384}
        ]
        self.selected_button_guide_credits = 0
        self.run_guide = False
        self.run_credits = False

    # Guide
    def draw_menu_guide(self):
        # Vẽ nút
        for i, button in enumerate(self.buttons_menu_guide_credits):
            color = (255, 255, 255) if i == self.selected_button_guide_credits else (255, 255, 0)
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
    def run_menu_guide(self):
        self.run_guide = True
        while self.run_guide:
            self.handle_menu_events_guide()
            self.draw_menu_credits()

    # Credits   
    def draw_menu_credits(self):
        # Vẽ nút
        for i, button in enumerate(self.buttons_menu_guide_credits):
            color = (255, 255, 255) if i == self.selected_button_guide_credits else (255, 255, 0)
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
    def run_menu_credits(self):
        self.run_credits = True
        while self.run_credits:
            self.handle_menu_events_credits()
            self.draw_menu_credits()