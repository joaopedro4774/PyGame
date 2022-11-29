import pygame, random
from pygame.locals import *

def on_grid_random():
    x = random.randint(0,59)
    y = random.randint(0,59)
    return (x * 10, y * 10)

def c(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


UP = 0
RIGHT = 1
DOWN=2
LEFT=3

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Maciel A Cobrinha')

cobra = [(200, 200), (210, 200), (220,200)]
design_cobra = pygame.Surface((10,10))
design_cobra.fill((0,0,255)) #Azul

possicao_fruta = on_grid_random()
fruta = pygame.Surface((10,10))
fruta.fill((255,0,0))

movimento_cobra = LEFT

clock = pygame.time.Clock()


game_over = False
while not game_over:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()


if movimento_cobra == UP:
        cobra[0] = (cobra[0][0], cobra[0][1] - 10)
if movimento_cobra == DOWN:
        cobra[0] = (cobra[0][0], cobra[0][1] + 10)
if movimento_cobra == RIGHT:
        cobra[0] = (cobra[0][0] + 10, cobra[0][1])
if movimento_cobra == LEFT:
        cobra[0] = (cobra[0][0] - 10, cobra[0][1])
    
screen.fill((0,0,0))
<<<<<<< HEAD
screen.blit(fruta, possicao_fruta)

for x in range(0, 600, 10): # Draw vertical lines
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 600))
for y in range(0, 600, 10): # Draw vertical lines
        pygame.draw.line(screen, (40, 40, 40), (0, y), (600, y))
    
score_font = font.render('Pontuação: %s' % (score), True, (255, 255, 255))
score_rect = score_font.get_rect()
score_rect.topleft = (600 - 120, 10)
screen.blit(score_font, score_rect)
    
for pos in cobra:
        screen.blit(design_cobra,pos)

pygame.display.update()
=======
screen.blit(fruta, possicao_fruta)
>>>>>>> b7f09c0f465847e0ffe27653dae1e9538ba2374e
