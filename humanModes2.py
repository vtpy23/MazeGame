import pygame
import sys
from random import randint
from old_mg import mazeGeneration
from old_md import Maze_bfs_solving
class DrawMaze:
    def __init__(self, maze, screen, camera_offset, wall, lava_image, door) -> None:
        self.maze = maze
        self.screen = screen
        self.solvedMaze = Maze_bfs_solving(self.maze)
        self.searching_area = self.solvedMaze.Bfs()
        self.camera_offset = camera_offset
        self.wall = wall
        self.door = door
        self.lava_image = lava_image
        self.ambitation_rect = None
        self.door_rect = None
        self.lava_rect = []
        self.lava_pos = 0
        self.break_loop = 7 # using for lava spreading
    def draw(self):
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                if cell == 'x':
                    wall_rect = self.wall.get_rect(topleft=(710 + (x * 40) - self.camera_offset.x, 1112 + (y * 40) - self.camera_offset.y))
                    self.screen.blit(self.wall, wall_rect)
        self.door_rect = self.wall.get_rect(topleft=(1530 + (x * 40), 1900 + (y * 40)))
        door_rect = self.wall.get_rect(topleft=(1530 + (x * 40) - self.camera_offset.x, 1900 + (y * 40) - self.camera_offset.y))
        self.screen.blit(self.door, door_rect)

    def check_collision(self, rect):
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                if cell == 'x':
                    wall_rect = self.wall.get_rect(topleft=(710 + (x * 40), 1112 + (y * 40)))
                    if rect.colliderect(wall_rect):
                        return True
        return False
    def check_game_starting(self, rect):
        begin_rect = self.wall.get_rect(topleft=(710 + (1 * 40), 1112 + (1 * 40)))
        if(rect.colliderect(begin_rect)): return True
        return False
    def check_lava_collision(self, rect):
        if self.lava_rect:
            for lava in self.lava_rect:
                if rect.colliderect(lava):
                    return True
        return False

    def check_win(self, rect):
        if rect.colliderect(self.ambitation_rect):
            return True
        return False
    def checkQuit(self, rect):
        if rect.colliderect(self.door_rect):
            return True
        return False
    def game_events(self, reward_image):
        i_placing = len(self.maze) - 2
        j_placing = len(self.maze) - 2
        ambitation_rect = reward_image.get_rect(topleft=(710 + (j_placing * 40) - self.camera_offset.x, 1112 + (i_placing * 40) - self.camera_offset.y))
        self.ambitation_rect = reward_image.get_rect(topleft=(710 + (j_placing * 40), 1112 + (i_placing * 40)))
        self.screen.blit(reward_image, ambitation_rect)
    
    def lavaSpreading(self):
        if(self.lava_pos < len(self.searching_area) and self.break_loop % 7 == 0):
            for i in range(self.lava_pos + 1):
                top = self.searching_area[i]
                lava_rect = self.lava_image.get_rect(topleft=(710 + (top[1] * 40) - self.camera_offset.x, 1112 + (top[0] * 40) - self.camera_offset.y))
                self.screen.blit(self.lava_image, lava_rect)
            lava_check_collisions = self.lava_image.get_rect(topleft=(710 + (self.searching_area[self.lava_pos][1] * 40), 1112 + (self.searching_area[self.lava_pos][0] * 40)))
            self.lava_rect.append(lava_check_collisions)
            self.lava_pos += 1
        self.break_loop += 1
    def draw_lava_continuous(self):
        for i in range(self.lava_pos + 1):
                top = self.searching_area[i]
                lava_rect = self.lava_image.get_rect(topleft=(710 + (top[1] * 40) - self.camera_offset.x, 1112 + (top[0] * 40) - self.camera_offset.y))
                self.screen.blit(self.lava_image, lava_rect)

class gameGeneral:
    def __init__(self) -> None:
        self.player_rect = player_image.get_rect(center=(677, 712))
        self.player_speed = 10
        self.maze = mazeGeneration().createMaze()
        self.camera_offset = pygame.Vector2()
        self.begin_lava_spreading = False
        self.win_status = False
        self.time = None
    def gameplay(self):
        self.maze[0][1] = 'o'
        A = DrawMaze(self.maze, screen, self.camera_offset, wall, lava_image, door)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            keys = pygame.key.get_pressed()
            # Store the current position
            player_rect_backup = self.player_rect.copy()
            # Draw ambitation pos
            if keys[pygame.K_UP]:
                self.player_rect.y -= self.player_speed
            elif keys[pygame.K_DOWN]:
                self.player_rect.y += self.player_speed
            if keys[pygame.K_LEFT]:
                self.player_rect.x -= self.player_speed
            elif keys[pygame.K_RIGHT]:
                self.player_rect.x += self.player_speed

            # Check for collision
            if A.check_collision(self.player_rect):
                self.player_rect = player_rect_backup  # Restore the previous position if there is a collision
            
            # Check for lava collision
            if A.check_lava_collision(self.player_rect):
                print('Chết vì dung nham dong 117')
                break
                #them man hinh thua
            # Check for game starting
            if A.check_game_starting(self.player_rect) == True and self.time is None:
                self.time = pygame.time.get_ticks()
            try:
                if(pygame.time.get_ticks() - self.time > 1000 and self.win_status == False): self.begin_lava_spreading = True
            except:
                self.time = None
            if(self.win_status == True):
                self.begin_lava_spreading = False
    
            # Calculate camera offset to keep player in the center
            camera_offset = pygame.Vector2(self.player_rect.center) - pygame.Vector2(screen.get_rect().center)

            # Draw ground
            screen.fill((113, 221, 238))  # Light blue
            ground_rect = ground_image.get_rect(topleft=(0 - camera_offset.x, 0 - camera_offset.y))
            screen.blit(ground_image, ground_rect)
            A.game_events(bed)

            # Draw walls based on the maze
            A.camera_offset = camera_offset
            A.draw()
            if self.begin_lava_spreading == True:
                A.lavaSpreading()
                A.draw_lava_continuous()
            # Check win
            if A.check_win(self.player_rect):
                print('Chiến thắng dong 147')
                self.win_status = True
                self.maze[len(self.maze) - 1][len(self.maze) - 2] = 'o'
                self.maze[0][1] = 'x'
                break
            if A.checkQuit(self.player_rect):
                print('quit dong 153')
                break

            # Draw player
            scaled_player_image = pygame.transform.scale(player_image, (int(self.player_rect.width), int(self.player_rect.height)))
            player_rect_scaled = scaled_player_image.get_rect(center=screen.get_rect().center)
            screen.blit(scaled_player_image, player_rect_scaled)

            pygame.display.flip()
            clock.tick(60)

# Main Program Execution
pygame.init()
screen = pygame.display.set_mode((1024, 768))
clock = pygame.time.Clock()

# Load images
player_image = pygame.image.load('graphics/merchant.png').convert_alpha()
ground_image = pygame.image.load('graphics/ground.png').convert_alpha()
tree_image = pygame.image.load('graphics/tree.png').convert_alpha()
wall = pygame.image.load('graphics/wall.png').convert_alpha()
bed = pygame.image.load('graphics/bed.png').convert_alpha()
lava_image = pygame.image.load('graphics/lava.png').convert_alpha()
door = pygame.image.load('graphics/door.png').convert_alpha()
