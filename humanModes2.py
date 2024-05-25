import pygame
import sys
from random import randint
from old_mg import mazeGeneration
from old_md import Maze_bfs_solving
import math
import random
import mazeGeneration as mg
class DrawEvents:
    def __init__(self, maze, screen, camera_offset, wall, lava_image, door) -> None:
        self.maze = maze
        self.screen = screen
        self.solvedMaze = Maze_bfs_solving(self.maze, (1,1), (len(maze) - 2, len(maze) - 2))
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
        self.break_loop = 5 # using for lava spreading
    def castle_draw(self, screen):
        castle = pygame.image.load('graphics/castle.png')
        castle_rect = castle.get_rect()
        castle_rect.center = (1024 // 2, 768 // 2)
        screen.blit(castle, castle_rect)
        pygame.display.flip()
        pygame.time.wait(1500)
        screen.fill((113, 221, 238))
    def opening_guide(self, screen):
        castle = pygame.image.load('graphics/fire_maze.jpg')
        castle_rect = castle.get_rect()
        castle_rect.center = (1024 // 2, 768 // 2)
        screen.blit(castle, castle_rect)
    def opening_guide2(self, screen):
        castle = pygame.image.load('graphics/horror_maze.jpg')
        castle_rect = castle.get_rect()
        castle_rect.center = (1024 // 2, 768 // 2)
        screen.blit(castle, castle_rect)
    def opening_guide3(self, screen):
        castle = pygame.image.load('graphics/key_maze.jpg')
        castle_rect = castle.get_rect()
        castle_rect.center = (1024 // 2, 768 // 2)
        screen.blit(castle, castle_rect)
    def closing_guide(self, screen):
        castle = pygame.image.load('graphics/win.jpg')
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
    def draw_arrow(self, surface, start, end, color, camera_offset):
        adjusted_start = (start[0] - camera_offset.x, start[1] - camera_offset.y)
        adjusted_end = (end[0] - camera_offset.x, end[1] - camera_offset.y)
        
        pygame.draw.line(surface, color, adjusted_start, adjusted_end, 5)
        
        angle = math.atan2(adjusted_end[1] - adjusted_start[1], adjusted_end[0] - adjusted_start[0])
        arrow_head_length = 20
        arrow_head_angle = math.pi / 6
        
        arrow_point1 = (
            adjusted_end[0] - arrow_head_length * math.cos(angle - arrow_head_angle),
            adjusted_end[1] - arrow_head_length * math.sin(angle - arrow_head_angle)
        )
        arrow_point2 = (
            adjusted_end[0] - arrow_head_length * math.cos(angle + arrow_head_angle),
            adjusted_end[1] - arrow_head_length * math.sin(angle + arrow_head_angle)
        )
        
        pygame.draw.line(surface, color, adjusted_end, arrow_point1, 5)
        pygame.draw.line(surface, color, adjusted_end, arrow_point2, 5)

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
    def drawlastgame(self):
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                if cell == 'x':
                    wall_rect = self.wall.get_rect(topleft=(710 + (x * 40) - self.camera_offset.x, 1112 + (y * 40) - self.camera_offset.y))
                    self.screen.blit(self.wall, wall_rect)
        self.door_rect = self.door.get_rect(topleft=(1530 + (x * 40), 1900 + (y * 40)))
        door_rect = self.door.get_rect(topleft=(1530 + (x * 40) - self.camera_offset.x, 1900 + (y * 40) - self.camera_offset.y))
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
        if(self.lava_pos < len(self.searching_area) and self.break_loop % 5 == 0):
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
    #Round 3
    def random_door_key(self, maze):
        solved = Maze_bfs_solving(maze, (1,1), (len(maze) - 2, len(maze) - 2))
        way = solved.Truyvet()
        self.selected_door = []
        self.selected_key = []
        begin = 0
        end = len(way) // 3 - 1
        for i in range(3):
            self.selected_door.append(random.choice(way[begin:end]))
            begin = end
            end = end + len(way) // 3 - 1
        self.door_game_rect = []
        self.key_rect = []
        for y, x in self.selected_door:
            cure_rect = self.wall.get_rect(topleft=(710 + (x * 40), 1112 + (y * 40)))
            self.door_game_rect.append(cure_rect)
        random_key_area = []
        count = 0
        begin = (1,1)
        for pos in self.searching_area:
            random_key_area.append(pos)
            if(pos in self.selected_door):
                while(True):
                    key = random.choice(random_key_area)
                    end = key
                    way_to_key = Maze_bfs_solving(maze, begin, end).Truyvet()
                    if pos not in way_to_key:
                        count += 1
                        begin = pos
                        random_key_area = []
                        self.selected_key.append(key)
                        break
            if(count == 3): break   
        for y, x in self.selected_key:
            cure_rect = self.wall.get_rect(topleft=(710 + (x * 40), 1112 + (y * 40)))
            self.key_rect.append(cure_rect) 
    def draw_door(self):
        for y, x in self.selected_door:
            door_rect = self.wall.get_rect(topleft=(710 + (x * 40) - self.camera_offset.x, 1112 + (y * 40) - self.camera_offset.y))
            self.screen.blit(door_ingame, door_rect)
    def check_collision_door(self,rect, key):
        if key != 0: return False
        if self.door_game_rect:
            for door in self.door_game_rect:
                if rect.colliderect(door):
                    return True
        return False
    def draw_key(self):
        for y, x in self.selected_key:
            key_rect = key.get_rect(topleft=(710 + (x * 40) - self.camera_offset.x, 1112 + (y * 40) - self.camera_offset.y))
            self.screen.blit(key, key_rect)
    def check_collecting_key(self, rect):
        if self.key_rect: 
            for key in self.key_rect:
                if rect.colliderect(key):
                    self.key_rect.remove(key)
                    self.selected_key.remove(((key.y - 1112) // 40, (key.x - 710) // 40))
                    return True
        return False
    def check_door_condition(self, rect, key):
        if key != 0:
            if self.door_game_rect:
                for door in self.door_game_rect:
                    if rect.colliderect(door):
                        print(True)
                        #Delete wall and wall rect
                        self.door_game_rect.remove(door)
                        self.selected_door.remove(((door.y - 1112) // 40, (door.x - 710) // 40))
                        return True
        return False
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
        A = DrawEvents(self.maze, screen, self.camera_offset, wall, lava_image, door)
        A.castle_draw(screen)
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
                A.draw_opening_circle(screen)
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
            if self.win_status == True:
                A.draw_arrow(screen, (self.player_rect.centerx, self.player_rect.centery), (3000,3300), (0, 255, 0), camera_offset)
            if A.checkQuit(self.player_rect):
                print('quit dong 153')
                A.draw_opening_circle(screen)
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
        self.win_game2 = False
    def gameplay(self):
        self.maze[0][1] = 'o'
        start_time = 120
        A = DrawEvents(self.maze, screen, self.camera_offset, wall, lava_image, door)
        A.select_points(A.searching_area)
        opening_guide = True
        while opening_guide:
            A.opening_guide2(screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    opening_guide = False
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
            if seconds <= 0 and self.win_game2 == False:
                seconds = 0
                #Them man hinh thua
                A.draw_lose2(screen)
                pygame.display.flip()
                pygame.time.wait(3000)
                A.draw_opening_circle(screen)
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
            if self.win_game2 == False:
                A.game_events(princess)#Sau nay thay doi thanh princess
            #Check collecting Cure
            A.check_collecting_cure(self.player_rect)
            # Check win
            if A.check_win(self.player_rect) and A.count_cure == 5:
                self.win_game2 = True
                self.maze[len(self.maze) - 1][len(self.maze) - 2] = 'o'
                self.maze[0][1] = 'x'
               # ra duoc khoi me cung ve man hinh thang cuu duoc cong chua
            if A.checkQuit(self.player_rect):
                A.draw_opening_circle(screen)
                break
            if(self.win_game2 == True and A.checkNextRound(self.player_rect) == True):
                C = findWayOut()
                C.gameplay()
                break
            # Draw player
            scaled_player_image = pygame.transform.scale(player_image, (int(self.player_rect.width), int(self.player_rect.height)))
            player_rect_scaled = scaled_player_image.get_rect(center=screen.get_rect().center)
            screen.blit(scaled_player_image, player_rect_scaled)
            # Draw princess Move
            if self.win_game2 == True:
                A.draw_arrow(screen, (self.player_rect.centerx, self.player_rect.centery), (3000,3300), (0, 255, 0), camera_offset)
                princess_rect = princess.get_rect(topleft=(1024//2 - 40 - self.camera_offset.x, 768//2 - 30 - self.camera_offset.y))
                screen.blit(princess, princess_rect)
            mg.Initialization().draw_rectangle_with_text(824, 20, 140,f"time: {seconds: .2f}")
            pygame.display.flip()
            clock.tick(60)
class findWayOut(gameGeneral):
    def __init__(self) -> None:
        super().__init__()
        self.player_rect = player_image.get_rect(center=(677, 712))
        self.win_all = False
        self.key_collection = 0
    def gameplay(self):
        self.maze[0][1] = 'o'
        start_time = 60
        A = DrawEvents(self.maze, screen, self.camera_offset, wall, lava_image, door)
        opening_guide = True
        while opening_guide:
            A.opening_guide3(screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    opening_guide = False
        A.draw_opening_circle(screen)
        start_ticks = pygame.time.get_ticks()
        A.random_door_key(self.maze)
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
            if A.check_collision(self.player_rect) or A.check_collision_door(self.player_rect, self.key_collection):
                self.player_rect = player_rect_backup  # Restore the previous position if there is a collision
            
            # Check for run out time
            if seconds <= 0 and self.win_all == False:
                seconds = 0
                #Them man hinh thua
                A.draw_lose2(screen)
                pygame.display.flip()
                pygame.time.wait(3000)
                A.draw_opening_circle(screen)
                break
            # Calculate camera offset to keep player in the center
            camera_offset = pygame.Vector2(self.player_rect.center) - pygame.Vector2(screen.get_rect().center)

            # Draw ground
            screen.fill((113, 221, 238))  # Light blue
            ground_rect = ground_image.get_rect(topleft=(0 - camera_offset.x, 0 - camera_offset.y))
            screen.blit(ground_image, ground_rect)
            A.drawlastgame()
            A.draw_door()
            A.draw_key()
            # Draw walls based on the maze
            A.camera_offset = camera_offset
            if A.check_collecting_key(self.player_rect):
                self.key_collection += 1
            #Check collect key
            if self.win_all == False:
                A.game_events(bed)
            if A.check_door_condition(self.player_rect, self.key_collection):
                self.key_collection = 0
            if A.check_win(self.player_rect) and self.win_all == False:
                closing_guide = True
                while closing_guide:
                    A.closing_guide(screen)
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            closing_guide = False
                self.win_all = True
            # Check win
            # Mo ra duoc 3 cua va den dich
            # ra duoc khoi me cung ve man hinh thang cuu duoc cong chua
            if A.checkQuit(self.player_rect):
                A.draw_opening_circle(screen)
                break
            # Draw player
            scaled_player_image = pygame.transform.scale(player_image, (int(self.player_rect.width), int(self.player_rect.height)))
            player_rect_scaled = scaled_player_image.get_rect(center=screen.get_rect().center)
            screen.blit(scaled_player_image, player_rect_scaled)
            # Draw princess Move
            if self.win_all == True: 
                A.draw_arrow(screen, (self.player_rect.centerx, self.player_rect.centery), (3000,3300), (0, 255, 0), camera_offset)
                self.maze[len(self.maze) - 1][len(self.maze) - 2] = 'o'
                self.maze[0][1] = 'x'
            princess_rect = princess.get_rect(topleft=(1024//2 - 40 - self.camera_offset.x, 768//2 - 30 - self.camera_offset.y))
            screen.blit(princess, princess_rect)
            mg.Initialization().draw_rectangle_with_text(824, 20, 140,f"time: {seconds: .2f}")
            pygame.display.flip()
            clock.tick(60)

# Main Program Executiona
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
key = pygame.image.load('graphics/key.png').convert_alpha()
door_ingame = pygame.image.load('graphics/door_ingame.jpg').convert_alpha()
