import pygame
def init_window(width, height, title="Maze Game"):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(title)
    return screen

