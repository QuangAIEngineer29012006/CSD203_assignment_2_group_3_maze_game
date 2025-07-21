import pygame

def init_window(width, height, title="Maze Game"):
    pygame.init()
    pygame.display.set_caption(title) 
    screen = pygame.display.set_mode((width, height))
    return screen
