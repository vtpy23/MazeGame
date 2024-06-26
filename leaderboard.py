import pygame
import mazeGeneration as mg
import saveLoad as sv

class LeaderBoard:
    def __init__(self):
        self.buttons_menu_leader_board = [
        {"text": "20x20", "pos_x": 840, "pos_y": 264},
        {"text": "40x40", "pos_x": 840, "pos_y": 344},
        {"text": "100x100", "pos_x": 840, "pos_y": 424},
        {"text": "BACK", "pos_x": 840, "pos_y": 504}
        ]
        self.selected_button_leader_board = 0
        self.run_leader_board = False
        # LEADER BOARD
    def draw_menu_leader_board(self):
        # Vẽ nút
        for i, button in enumerate(self.buttons_menu_leader_board):
            color = (255, 255, 255) if i == self.selected_button_leader_board else (255, 255, 0)
            mg.Initialization().draw_text(button["text"], 36, color, button["pos_x"], button["pos_y"])
        pygame.display.flip()
    def handle_key_events_leader_board(self, event):
        if event.key == pygame.K_UP:
            self.selected_button_leader_board = (self.selected_button_leader_board - 1) % len(self.buttons_menu_leader_board)
        elif event.key == pygame.K_DOWN:
            self.selected_button_leader_board = (self.selected_button_leader_board + 1) % len(self.buttons_menu_leader_board)
        elif event.key == pygame.K_RETURN:
            self.handle_button_click_leader_board(self.selected_button_leader_board)
    def handle_mouse_events_leader_board(self):
        mouse_pos = pygame.mouse.get_pos()
        for i, button in enumerate(self.buttons_menu_leader_board):
            text_rect = mg.Initialization().draw_text(button["text"], 36, (255, 255, 0), button["pos_x"], button["pos_y"])
            if text_rect.collidepoint(mouse_pos):
                self.handle_button_click_leader_board(i)
    def handle_button_click_leader_board(self, index):
        text_size = 20
        if index == 0:
            self.bg_line()
            level_1 = sv.LeaderBoard().data_processing(20)
            for i, button in enumerate(level_1):
                rank = str(i + 1) + "."
                color = (0, 0, 0)
                mg.Initialization().draw_text_2(rank, text_size, color, 140, 265 + 71 * i)
                mg.Initialization().draw_text_2(str(button["username"]).encode('utf-8'), text_size, color, 170, 265 + 71 * i)
                mg.Initialization().draw_text_2(str(button["number"]).encode('utf-8'), text_size, color, 330, 265 + 71 * i)
                mg.Initialization().draw_text_2(str(button["total_time"])[:4].encode('utf-8'), text_size, color, 370, 265 + 71 * i)
                mg.Initialization().draw_text_2(str(button["total_step"]).encode('utf-8'), text_size, color, 440, 265 + 71 * i)
                mg.Initialization().draw_text_2(str(button["total_time"]//button["number"]).encode('utf-8'), text_size, color, 510, 265 + 71 * i)
                mg.Initialization().draw_text_2(str(button["total_step"]//button["number"]).encode('utf-8'), text_size, color, 580, 265 + 71 * i)
            pygame.display.flip()
        elif index == 1:
            self.bg_line()
            level_2 = sv.LeaderBoard().data_processing(40)
            for i, button in enumerate(level_2):
                rank = str(i + 1) + "."
                color = (0, 0, 0)
                mg.Initialization().draw_text_2(rank, text_size, color, 140, 265 + 71 * i)
                mg.Initialization().draw_text_2(str(button["username"]).encode('utf-8'), text_size, color, 170, 265 + 71 * i)
                mg.Initialization().draw_text_2(str(button["number"]).encode('utf-8'), text_size, color, 330, 265 + 71 * i)
                mg.Initialization().draw_text_2(str(button["total_time"])[:4].encode('utf-8'), text_size, color, 370, 265 + 71 * i)
                mg.Initialization().draw_text_2(str(button["total_step"]).encode('utf-8'), text_size, color, 440, 265 + 71 * i)
                mg.Initialization().draw_text_2(str(button["total_time"]//button["number"]).encode('utf-8'), text_size, color, 510, 265 + 71 * i)
                mg.Initialization().draw_text_2(str(button["total_step"]//button["number"]).encode('utf-8'), text_size, color, 580, 265 + 71 * i)
            pygame.display.flip()
        elif index == 2: 
            self.bg_line()
            level_3 = sv.LeaderBoard().data_processing(40)
            for i, button in enumerate(level_3):
                rank = str(i + 1) + "."
                color = (0, 0, 0)
                mg.Initialization().draw_text_2(rank, text_size, color, 140, 265 + 71 * i)
                mg.Initialization().draw_text_2(str(button["username"]).encode('utf-8'), text_size, color, 170, 265 + 71 * i)
                mg.Initialization().draw_text_2(str(button["number"]).encode('utf-8'), text_size, color, 330, 265 + 71 * i)
                mg.Initialization().draw_text_2(str(button["total_time"])[:4].encode('utf-8'), text_size, color, 370, 265 + 71 * i)
                mg.Initialization().draw_text_2(str(button["total_step"]).encode('utf-8'), text_size, color, 440, 265 + 71 * i)
                mg.Initialization().draw_text_2(str(button["total_time"]//button["number"]).encode('utf-8'), text_size, color, 510, 265 + 71 * i)
                mg.Initialization().draw_text_2(str(button["total_step"]//button["number"]).encode('utf-8'), text_size, color, 580, 265 + 71 * i)
            pygame.display.flip()
        elif index == 3:
            self.run_leader_board = False
    def handle_menu_events_leader_board(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                self.handle_key_events_leader_board(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_events_leader_board()  

    def run_menu_leader_board(self):
        self.bg_line()
        self.run_leader_board = True
        while self.run_leader_board:
            self.handle_menu_events_leader_board()
            self.draw_menu_leader_board()

    def bg_line(self):
        mg.Initialization().input_image_background("image/bg_line.png")
        mg.Initialization().draw_text("USER   NUMBER    TIME   STEP   AVG TIME    AVG STEP", 18, "Black", 384, 200)