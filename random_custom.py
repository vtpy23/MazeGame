import pygame
import mazeGeneration as mg 
from humanMode import gameManually
from autoMode import gameAutomatically
import random

class Random_custom:
    def __init__(self):
        self.buttons_menu_random_custom = [
        {"text": "RANDOM", "pos_x": 840, "pos_y": 304},
        {"text": "CUSTOM", "pos_x": 840, "pos_y": 384},
        {"text": "BACK", "pos_x": 840, "pos_y": 464}    
        ]
        self.selected_button_random_custom = 0
        self.run_random_custom = False

    # RANDOM / CUSTOM
    def draw_menu_random_custom(self):
        for i, button in enumerate(self.buttons_menu_random_custom):
            color = (255, 255, 255) if i == self.selected_button_random_custom else (255, 255, 0)
            mg.Initialization().draw_text(button["text"], 36, color, button["pos_x"], button["pos_y"])
        if self.selected_button_random_custom == 0:
            mg.Initialization().draw_text("START POINT AND", 42, 'Black', 384, 324)
            mg.Initialization().draw_text("END POINT WILL BE", 42, 'Black', 384, 384)
            mg.Initialization().draw_text("GENERATED RANDOMLY", 42, 'Black', 384, 444)
        elif self.selected_button_random_custom == 1:
            mg.Initialization().draw_text("YOU CAN SELECT START", 42, 'Black', 384, 324)
            mg.Initialization().draw_text("POINT AND END POINT", 42, 'Black', 384, 384)
            mg.Initialization().draw_text("WITH THE MOUSE", 42, 'Black', 384, 444)
        pygame.display.flip()
    def handle_key_events_random_custom(self, event, sizemap, mode):
        if event.key == pygame.K_UP:
            mg.Initialization().input_image_background("image/floor_bg.png")
            self.selected_button_random_custom = (self.selected_button_random_custom - 1) % len(self.buttons_menu_random_custom)
        elif event.key == pygame.K_DOWN:
            mg.Initialization().input_image_background("image/floor_bg.png")
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
                    size = 20
                    matrix = mg.mazeGeneration().createMaze(size)
                    player_pos = (0, 0) #Vi tri co the thay doi
                    player_aimbitation = (size - random.randint(1, size // 2), size - random.randint(1, size // 2))
                    play = gameManually(size, matrix, player_pos, player_aimbitation)
                    play.mode_play = 0
                    play.drawMaze()
                    play.creatingMaze()
                    mg.Initialization().draw_floor_background()
                    mg.Initialization().draw_to_delete("")
                    mg.Initialization().draw_text("START POINT - END POINT", 48, (255, 255, 0), 384, 42)
                elif sizemap == 1: # map: 40x40, mode: manual, start point - end point: random
                    size = 40
                    matrix = mg.mazeGeneration().createMaze(size)
                    player_pos = (0,0) #Vi tri co the thay doi
                    player_aimbitation = (size - random.randint(1, size // 2), size - random.randint(1, size // 2))
                    play = gameManually(size, matrix, player_pos, player_aimbitation)
                    play.mode_play = 0
                    play.drawMaze()
                    play.creatingMaze()
                    mg.Initialization().draw_floor_background()
                    mg.Initialization().draw_to_delete("")
                    mg.Initialization().draw_text("START POINT - END POINT", 48, (255, 255, 0), 384, 42)
                elif sizemap == 2: # map: 100x100, mode: manual, start point - end point: random
                    size = 100
                    matrix = mg.mazeGeneration().createMaze(size)
                    player_pos = (0,0) #Vi tri co the thay doi
                    player_aimbitation = (size - random.randint(1, size // 2), size - random.randint(1, size // 2))
                    play = gameManually(size, matrix, player_pos, player_aimbitation)
                    play.mode_play = 0
                    play.drawMaze()
                    play.creatingMaze()
                    mg.Initialization().draw_floor_background()
                    mg.Initialization().draw_to_delete("")
                    mg.Initialization().draw_text("START POINT - END POINT", 48, (255, 255, 0), 384, 42)
            elif mode == 1:
                if sizemap == 0: # map: 20x20, mode: auto, start point - end point: random
                    play = gameAutomatically(20)
                    play.mode_play = 0
                    play.drawMaze()
                    play.creatingMaze()
                    mg.Initialization().draw_floor_background()
                    mg.Initialization().draw_to_delete("")
                    mg.Initialization().draw_text("START POINT - END POINT", 48, (255, 255, 0), 384, 42)                    
                elif sizemap == 1: # map: 40x40, mode: auto, start point - end point: random
                    play = gameAutomatically(40)
                    play.mode_play = 0
                    play.drawMaze()
                    play.creatingMaze()
                    mg.Initialization().draw_floor_background()
                    mg.Initialization().draw_to_delete("")
                    mg.Initialization().draw_text("START POINT - END POINT", 48, (255, 255, 0), 384, 42)                    
                elif sizemap == 2: # map: 100x100, mode: auto, start point - end point: random
                    play = gameAutomatically(100)
                    play.mode_play = 0
                    play.drawMaze()
                    play.creatingMaze()
                    mg.Initialization().draw_floor_background()
                    mg.Initialization().draw_to_delete("")
                    mg.Initialization().draw_text("START POINT - END POINT", 48, (255, 255, 0), 384, 42)                    
        elif index == 1:
            if mode == 0:
                if sizemap == 0: # map: 20x20, mode: manual, start point - end point: custom
                    size = 20
                    matrix = mg.mazeGeneration().createMaze(size)
                    player_pos = (0,0) #Vi tri co the thay doi
                    player_aimbitation = (size - random.randint(1, size // 2), size - random.randint(1, size // 2))
                    play = gameManually(size, matrix, player_pos, player_aimbitation)
                    play.mode_play = 1
                    play.drawMaze()
                    play.choose_start_end_point(20)
                    play.creatingMaze()
                    mg.Initialization().draw_floor_background()
                    mg.Initialization().draw_to_delete("")
                    mg.Initialization().draw_text("START POINT - END POINT", 48, (255, 255, 0), 384, 42)
                elif sizemap == 1: # map: 40x40, mode: manual, start point - end point: custom
                    size = 40
                    matrix = mg.mazeGeneration().createMaze(size)
                    player_pos = (0,0) #Vi tri co the thay doi
                    player_aimbitation = (size - random.randint(1, size // 2), size - random.randint(1, size // 2))
                    play = gameManually(size, matrix, player_pos, player_aimbitation)
                    play.mode_play = 1
                    play.drawMaze()
                    play.choose_start_end_point(40)
                    play.creatingMaze()
                    mg.Initialization().draw_floor_background()
                    mg.Initialization().draw_to_delete("")
                    mg.Initialization().draw_text("START POINT - END POINT", 48, (255, 255, 0), 384, 42)                   
                elif sizemap == 2: # map: 100x100, mode: manual, start point - end point: custom
                    size = 100
                    matrix = mg.mazeGeneration().createMaze(size)
                    player_pos = (0,0) #Vi tri co the thay doi
                    player_aimbitation = (size - random.randint(1, size // 2), size - random.randint(1, size // 2))
                    play = gameManually(size, matrix, player_pos, player_aimbitation)
                    play.mode_play = 1
                    play.drawMaze()
                    play.choose_start_end_point(100)
                    play.creatingMaze()
                    mg.Initialization().draw_floor_background()
                    mg.Initialization().draw_to_delete("")
                    mg.Initialization().draw_text("START POINT - END POINT", 48, (255, 255, 0), 384, 42)
            elif mode == 1:
                if sizemap == 0: # map: 20x20, mode: auto, start point - end point: custom
                    play = gameAutomatically(20)
                    play.mode_play = 1
                    play.drawMaze()
                    play.choose_start_end_point(20)
                    play.creatingMaze()
                    mg.Initialization().draw_floor_background()
                    mg.Initialization().draw_to_delete("")
                    mg.Initialization().draw_text("START POINT - END POINT", 48, (255, 255, 0), 384, 42)                    
                elif sizemap == 1: # map: 20x20, mode: auto, start point - end point: custom
                    play = gameAutomatically(40)
                    play.mode_play = 1
                    play.drawMaze()
                    play.choose_start_end_point(40)
                    play.creatingMaze()
                    mg.Initialization().draw_floor_background()
                    mg.Initialization().draw_to_delete("")
                    mg.Initialization().draw_text("START POINT - END POINT", 48, (255, 255, 0), 384, 42)                    
                elif sizemap == 2: # map: 20x20, mode: auto, start point - end point: custom
                    play = gameAutomatically(100)
                    play.mode_play = 1
                    play.drawMaze()
                    play.choose_start_end_point(100)
                    play.creatingMaze()
                    mg.Initialization().draw_floor_background()
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
    
    def run_menu_random_custom(self, sizemap, mode):
        self.run_random_custom = True
        while self.run_random_custom:
            self.handle_menu_events_random_custom(sizemap, mode)
            self.draw_menu_random_custom()
    

