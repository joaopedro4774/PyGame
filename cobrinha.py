import pygame, random
from pygame.locals import *

# Helper functions
def on_grid_random():
    x = random.randint(0,59)
    y = random.randint(0,59)
    return (x * 10, y * 10)

def c(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

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

font = pygame.font.Font('freesansbold.ttf', 18)
score = 0

game_over = False
while not game_over:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_UP and movimento_cobra != DOWN:
                movimento_cobra = UP
            if event.key == K_DOWN and movimento_cobra != UP:
                movimento_cobra = DOWN
            if event.key == K_LEFT and movimento_cobra != RIGHT:
                movimento_cobra = LEFT
            if event.key == K_RIGHT and movimento_cobra != LEFT:
                movimento_cobra = RIGHT

    if c(cobra[0], possicao_fruta):
        possicao_fruta = on_grid_random()
        cobra.append((0,0))
        score = score + 1
        
    # Check if cobra collided with boundaries
    if cobra[0][0] == 600 or cobra[0][1] == 600 or cobra[0][0] < 0 or cobra[0][1] < 0:
        game_over = True
        break
    
    # Check if the cobra has hit itself
    for i in range(1, len(cobra) - 1):
        if cobra[0][0] == cobra[i][0] and cobra[0][1] == cobra[i][1]:
            game_over = True
            break

    if game_over:
        break
    
    for i in range(len(cobra) - 1, 0, -1):
        cobra[i] = (cobra[i-1][0], cobra[i-1][1])
        
    # Actually make the cobra move.
    if movimento_cobra == UP:
        cobra[0] = (cobra[0][0], cobra[0][1] - 10)
    if movimento_cobra == DOWN:
        cobra[0] = (cobra[0][0], cobra[0][1] + 10)
    if movimento_cobra == RIGHT:
        cobra[0] = (cobra[0][0] + 10, cobra[0][1])
    if movimento_cobra == LEFT:
        cobra[0] = (cobra[0][0] - 10, cobra[0][1])
    
    screen.fill((0,0,0))
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

while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 75)
    game_over_screen = game_over_font.render('Fim de Jogo', True, (255, 255, 255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (600 / 2, 10)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            exit()
