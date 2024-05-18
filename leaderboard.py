import pygame
import mazeGeneration as mg
import saveLoad as sv

class LeaderBoard:
    def __init__(self):
        self.buttons_menu_leader_board = [
        {"text": "PLAYER", "pos_x": 840, "pos_y": 264},
        {"text": "AVERGAGE", "pos_x": 840, "pos_y": 329},
        {"text": "AVERGAGE", "pos_x": 840, "pos_y": 409},
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
            if i == 1:
                mg.Initialization().draw_text("TIME", 36, color, 840, 359)
            elif i == 2:
                mg.Initialization().draw_text("STEP", 36, color, 840, 439)
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
        if index == 0:
            print("information")
        elif index == 1:
            mg.Initialization().input_image_background("image/bg_line.png")
            mg.Initialization().draw_text_2("USER", 30, (0, 0, 0), 200, 190)
            mg.Initialization().draw_text_2("AVG_TIME", 30, (0, 0, 0), 500, 190)
            top_average_time = sv.LeaderBoard().get_top(sv.LeaderBoard().sort_average_time())
            for i, button in enumerate(top_average_time):
                rank = str(i + 1) + "."
                color = (0, 0, 0)
                mg.Initialization().draw_text_2(rank, 36, color, 150, 248 + 71 * i)
                mg.Initialization().draw_text_2(str(button["name"]).encode('utf-8'), 36, color, 200, 248 + 71 * i)
                mg.Initialization().draw_text_2(str(button["average_timer"])[:5].encode('utf-8'), 36, color, 500, 248 + 71 * i)
            pygame.display.flip()
        elif index == 2: 
            mg.Initialization().input_image_background("image/bg_line.png")
            mg.Initialization().draw_text_2("USER", 30, (0, 0, 0), 200, 190)
            mg.Initialization().draw_text_2("AVG_STEP", 30, (0, 0, 0), 500, 190)
            top_average_step = sv.LeaderBoard().get_top(sv.LeaderBoard().sort_average_step())
            for i, button in enumerate(top_average_step):
                rank = str(i + 1) + "."
                color = (0, 0, 0)
                mg.Initialization().draw_text_2(rank, 36, color, 150, 248 + 71 * i)
                mg.Initialization().draw_text_2(str(button["name"]).encode('utf-8'), 36, color, 200, 248 + 71 * i)
                mg.Initialization().draw_text_2(str(button["average_step"])[:5].encode('utf-8'), 36, color, 500, 248 + 71 * i)
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