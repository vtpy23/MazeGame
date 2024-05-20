import pygame
import sys
from random import randint
from old_mg import mazeGeneration
from old_md import Maze_bfs_solving
import math
import random
import mazeGeneration as mg
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
        self.next_door_rect = None
        self.lava_rect = []
        self.cure_rect = []
        self.lava_pos = 0
        self.cure_points = None
        self.count_cure = 0
        self.break_loop = 7 # using for lava spreading
    def opening_guide(self, screen):
        castle = pygame.image.load('graphics/castle.png')
        castle_rect = castle.get_rect()
        castle_rect.center = (1024 // 2, 768 // 2)
        screen.blit(castle, castle_rect)
    def opening_guide2(self, screen):
        castle = pygame.image.load('graphics/castle.png')
        castle_rect = castle.get_rect()
        castle_rect.center = (1024 // 2, 768 // 2)
        screen.blit(castle, castle_rect)
    def draw_opening_circle(self, screen):
        max_radius = max(1024, 768) // 2
        for radius in range(0, max_radius + 1, 5):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            screen.fill((0,0,0))
            pygame.draw.circle(screen, (255,255,255), (1024 // 2, 768 // 2), radius)
            pygame.display.flip()
            clock.tick(60)
    def draw_lose1(self, screen):
        castle = pygame.image.load('graphics/lose1.png')
        castle_rect = castle.get_rect()
        castle_rect.center = (1024 // 2, 768 // 2)
        screen.blit(castle, castle_rect)
    def draw_lose2(self, screen):
        castle = pygame.image.load('graphics/lose2.png')
        castle_rect = castle.get_rect()
        castle_rect.center = (1024 // 2, 768 // 2)
        screen.blit(castle, castle_rect)
    def draw(self):
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                if cell == 'x':
                    wall_rect = self.wall.get_rect(topleft=(710 + (x * 40) - self.camera_offset.x, 1112 + (y * 40) - self.camera_offset.y))
                    self.screen.blit(self.wall, wall_rect)
        self.door_rect = self.door.get_rect(topleft=(1530 + (x * 40), 1900 + (y * 40)))
        door_rect = self.door.get_rect(topleft=(1530 + (x * 40) - self.camera_offset.x, 1900 + (y * 40) - self.camera_offset.y))
        self.screen.blit(self.door, door_rect)
        self.next_door_rect = self.door.get_rect(topleft=(1700 + (x * 40), 1900 + (y * 40)))
        next_door_rect = self.door.get_rect(topleft=(1700 + (x * 40) - self.camera_offset.x, 1900 + (y * 40) - self.camera_offset.y))
        self.screen.blit(self.door, next_door_rect)

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
    def checkNextRound(self, rect):
        if(rect.colliderect(self.next_door_rect)): 
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
    #Round 2
    def distance(self, p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    def select_points(self,points, num_points=5, min_distance=3):
        selected_points = []
        while len(selected_points) < num_points:
            candidate = random.choice(points)
            if all(self.distance(candidate, sp) >= min_distance for sp in selected_points):
                selected_points.append(candidate)
        self.cure_points = selected_points
        for y, x in self.cure_points:
            cure_rect = self.wall.get_rect(topleft=(710 + (x * 40), 1112 + (y * 40)))
            self.cure_rect.append(cure_rect)
    def draw_selected_point(self):
        for y, x in self.cure_points:
            cure_rect = self.wall.get_rect(topleft=(710 + (x * 40) - self.camera_offset.x, 1112 + (y * 40) - self.camera_offset.y))
            self.screen.blit(cure, cure_rect)
    
    def check_collecting_cure(self, rect):
        if self.cure_rect:
            for cure in self.cure_rect:
                if rect.colliderect(cure):
                    self.cure_rect.remove(cure)
                    self.cure_points.remove(((cure.y - 1112) // 40, (cure.x - 710) // 40))
                    self.count_cure += 1

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
        opening_guide = True
        while opening_guide:
            A.opening_guide(screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    opening_guide = False
        A.draw_opening_circle(screen)
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
                A.draw_lose1(screen)
                pygame.display.flip()
                pygame.time.wait(3000)
                break
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
                self.win_status = True
                self.maze[len(self.maze) - 1][len(self.maze) - 2] = 'o'
                self.maze[0][1] = 'x'
            # Check win status and next part
            if(self.win_status == True and A.checkNextRound(self.player_rect) == True):
                B = savePrincess()
                B.gameplay()
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

class savePrincess(gameGeneral):
    def __init__(self) -> None:
        super().__init__()
        self.player_rect = player_image.get_rect(center=(677, 712))
        self.collecting_cure = False
        self.win_all = False
    def gameplay(self):
        self.maze[0][1] = 'o'
        start_time = 2
        A = DrawMaze(self.maze, screen, self.camera_offset, wall, lava_image, door)
        A.select_points(A.searching_area)
        A.draw_opening_circle(screen)
        start_ticks = pygame.time.get_ticks()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            seconds = start_time - (pygame.time.get_ticks() - start_ticks) / 1000
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
            
            # Check for run out time
            if seconds <= 0 and self.win_all == False:
                seconds = 0
                #Them man hinh thua
                A.draw_lose2(screen)
                pygame.display.flip()
                pygame.time.wait(5000)
                break
            # Calculate camera offset to keep player in the center
            camera_offset = pygame.Vector2(self.player_rect.center) - pygame.Vector2(screen.get_rect().center)

            # Draw ground
            screen.fill((113, 221, 238))  # Light blue
            ground_rect = ground_image.get_rect(topleft=(0 - camera_offset.x, 0 - camera_offset.y))
            screen.blit(ground_image, ground_rect)

            # Draw walls based on the maze
            A.camera_offset = camera_offset
            A.draw()
            A.draw_selected_point()
            if self.win_all == False:
                A.game_events(princess)#Sau nay thay doi thanh princess
            #Check collecting Cure
            A.check_collecting_cure(self.player_rect)
            # Check win
            if A.check_win(self.player_rect) and A.count_cure == 5:
                self.win_all = True
                self.maze[len(self.maze) - 1][len(self.maze) - 2] = 'o'
                self.maze[0][1] = 'x'
               # ra duoc khoi me cung ve man hinh thang cuu duoc cong chua
            if A.checkQuit(self.player_rect):
                break

            # Draw player
            scaled_player_image = pygame.transform.scale(player_image, (int(self.player_rect.width), int(self.player_rect.height)))
            player_rect_scaled = scaled_player_image.get_rect(center=screen.get_rect().center)
            screen.blit(scaled_player_image, player_rect_scaled)
            # Draw princess Move
            if self.win_all == True:
                princess_rect = princess.get_rect(topleft=(1024//2 - 40 - self.camera_offset.x, 768//2 - 30 - self.camera_offset.y))
                screen.blit(princess, princess_rect)
            mg.Initialization().draw_rectangle_with_text(824, 20, 140,f"time: {seconds: .2f}")
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
cure = pygame.image.load('graphics/cure.png').convert_alpha()
princess = pygame.image.load('graphics/princess.png').convert_alpha()

