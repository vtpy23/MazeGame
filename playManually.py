import mazeGeneration as mG
import playAutomatically as pA
import pygame
import saveLoad as sv

screen = mG.screen
Walls = mG.mazeGeneration().createMaze()
WINDOW_WIDTH = mG.WINDOW_WIDTH
WINDOW_HEIGHT = mG.WINDOW_HEIGHT
cell_size = mG.cell_size

class playManually:
    def __init__(self) -> None:
        self.size = mG.size
        self.player_pos = (0, 0) #Vi tri co the thay doi
        self.player_aimbitation = (5, 0) #Vi tri dich co the thay doi va chuong trinh se tu dong tat sau khi dat den vi tri nay
        self.player_past = None
    
    def run(self):
        text = pygame.font.Font('font/Pixeltype.TTF', 50).render("Nhấn P để hiện hướng dẫn đường đi!", True, (0, 0, 0))
        screen.blit(text, (420, 720))
        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()   
                elif event.type == pygame.KEYDOWN:
                    while event.key != pygame.KEYUP: 
                        if event.key == pygame.K_UP:
                            self.Move(-1, 0)
                    if event.key == pygame.K_DOWN:
                        self.Move(1, 0)
                    elif event.key == pygame.K_LEFT:
                        self.Move(0, -1)
                    elif event.key == pygame.K_RIGHT:
                        self.Move(0, 1)
                    elif event.key == pygame.K_p:
                        play = pA.playAutomatically().Maze_bfs_solving()
                        play.Bfs(self.player_pos, self.player_aimbitation)
                        path = play.Truyvet()
                        mG.mazeGeneration().mazeApplication(Walls, path, (255, 0, 0))
                    elif event.key == pygame.K_s:
                        save = sv.saveLoad()
                        save.saveGame(Walls, self.player_pos, self.player_aimbitation)
            if(self.player_pos == self.player_aimbitation): 
                running = False 

    def Move(self, dx, dy):
        # Kiểm tra xem người chơi có thể di chuyển đến ô mới không
        new_x = self.player_pos[0] + dx
        new_y = self.player_pos[1] + dy
        move = [(1,0), (0,1), (-1,0), (0,-1)]
        k = move.index((dx, dy))
        print(self.player_pos)
        if 0 <= new_x < self.size and 0 <= new_y < self.size:
            # Kiểm tra xem ô mới có là tường không
            if  Walls[self.player_pos[0]][self.player_pos[1]][k] == 0:
                # Cập nhật vị trí mới của người chơi
                self.player_past = self.player_pos
                self.player_pos = (new_x, new_y)
                # Vẽ lại màn hình với vị trí mới của người chơi
                self.draw_player()

    def draw_player(self):
        # Vẽ hình vuông đại diện cho người chơi
        start_x = (WINDOW_WIDTH - self.size * cell_size) // 2 + 3
        start_y = (WINDOW_HEIGHT - self.size * cell_size) // 2 + 3
        player_x = start_x + self.player_pos[1] * cell_size #Hoanh do
        player_y = start_y + self.player_pos[0] * cell_size
        player_x_past = start_x + self.player_past[1] * cell_size
        player_y_past = start_y + self.player_past[0] * cell_size
        pygame.draw.rect(screen, (255, 255, 255), (player_x_past, player_y_past, cell_size - 5, cell_size - 5))
        pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, cell_size - 5, cell_size - 5))
        pygame.display.flip()