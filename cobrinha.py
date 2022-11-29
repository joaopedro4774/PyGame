import pygame, random
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Maciel A Cobrinha')

clock = pygame.time.Clock()


game_over = False
while not game_over:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()