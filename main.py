import pygame
from pygame import mixer
init_result = pygame.init()

WIDTH = 1200
HEIGHT = 600

black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Drum Machine')
label_font = pygame.font.Font('freesansbold.ttf', 32)

fps = 60
timer = pygame.time.Clock()



run = True
while run:
    timer.tick(fps)
    screen.fill(black)

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # draw to screen
    pygame.display.flip()

# backup in case code reaches this point
pygame.quit()