import pygame
import mazeGeneration as mg 
import saveLoad as sv
from humanMode import gameManually

screen = mg.screen

class Load:
    def __init__(self):
        self.buttons_menu_load = [
        {"text": "BACK", "pos_x": 840, "pos_y": 384}
        ]
        self.file_save_name = sv.saveLoad().takeNameFile()
        self.buttons_file_load = [
            {"text": name, "pos_x": 384, "pos_y": 200 + 40 * i}
            for i, name in enumerate(self.file_save_name)
        ]
        self.selected_button_load_file = 0
        self.selected_load = False # chon giua load ben trai va ben phai
        self.selected_button_load = 0
        self.run_load = False

    # Load
    ###Cac bien duoc dat o day khi nao lam xong se sua
    #self.file_save_name = sv.saveLoad().takeNameFile()
    def draw_menu_load(self):
        # Vẽ nút
        self.file_save_name = sv.saveLoad().takeNameFile()
        self.buttons_file_load = [
            {"text": name, "pos_x": 384, "pos_y": 200 + 40 * i}
            for i, name in enumerate(self.file_save_name)
        ]
        for i, button in enumerate(self.buttons_menu_load ):
            color = (255, 255, 255) if self.selected_load == False else (255, 255, 0)
            mg.Initialization().draw_text(button["text"], 36, color, button["pos_x"], button["pos_y"])
        pygame.display.flip()
        #Ve game save
        for i, button in enumerate(self.buttons_file_load):
            color = (0, 255, 0) if i == self.selected_button_load_file else (0, 0, 255)
            mg.Initialization().draw_text(button["text"], 30, color, button["pos_x"], button["pos_y"])
        pygame.display.flip()
    def handle_key_events_load(self, event):
        if self.selected_load == False:
            if event.key == pygame.K_RETURN:
                self.handle_button_click_load_right(self.selected_button_load)

        elif self.selected_load == True and len(self.buttons_file_load) != 0:
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
            text_rect = mg.Initialization().draw_text(button["text"], 30, (0, 0, 255), button["pos_x"], button["pos_y"])
            if text_rect.collidepoint(mouse_pos):
                self.handle_button_click_load_left(i)
    def handle_button_click_load_right(self, index):
        if index == 0:
            self.run_load = False

    def handle_button_click_load_left(self, index):
        mode, matrix, size, player_pos, player_aimbitation, time_start = sv.saveLoad().loadGame(index)
        cell_size = ((768)**2 / (size) ** 2) ** 0.5
        play = gameManually(size, matrix, player_pos, player_aimbitation, time_start)
        play.mode_play = mode
        play.drawMaze()
        pygame.draw.rect(screen, (255, 0, 0), (0 + 3 + player_pos[1] * cell_size 
                                            ,0 + 3 + player_pos[0] * cell_size, cell_size - 5, cell_size - 5))
        pygame.draw.rect(screen, (0, 0, 255), (0 + 3 + player_aimbitation[1] * cell_size 
                                            ,0 + 3 + player_aimbitation[0] * cell_size, cell_size - 5, cell_size - 5))
        pygame.display.flip()
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

    def run_menu_load(self):
        self.run_load = True
        mg.Initialization().draw_rectangle(84, 84, 600, 600, "White")
        mg.Initialization().draw_text("MAP   POINT    TIME       DATE     ", 32, "Black", 384, 150)
        while self.run_load:
            self.handle_menu_events_load()
            self.draw_menu_load()