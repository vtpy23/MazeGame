import pygame
import menu
import mazeGeneration as mg
from sys import exit

def run():
    run = menu.Menu()
    # Vẽ nền
    mg.Initialization().draw_floor()
    running = True
    while running:   
        run.handle_menu_events()
        run.draw_menu()

if __name__ == "__main__":
    run()

# Đổi tên thành MAZE GAME 
# ĐỔI GIAO DIỆN NHÌN CỔ ĐIỂN, PIXEL
# Thêm PAUSE