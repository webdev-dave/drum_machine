import pygame
from pygame import mixer
init_result = pygame.init()

WIDTH = 1200
HEIGHT = 800

black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)
green = (0, 255, 0)
gold = (212, 175, 55)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Drum Machine')
label_font = pygame.font.Font('freesansbold.ttf', 32)

fps = 60
timer = pygame.time.Clock()
beats = 8
instrumentRows = 6
instrumentRowHight = 100
sideMenuWidth = 200
bottomMenuHeight = 200

boxes = []
clicked = [[-1 for _ in range(beats)] for _ in range(instrumentRows)]

def draw_grid(clicks):
    left_box = pygame.draw.rect(screen, gray, (0, 0, sideMenuWidth, HEIGHT - bottomMenuHeight), 5)
    bottom_box = pygame.draw.rect(screen, gray, (0, HEIGHT - bottomMenuHeight, WIDTH, bottomMenuHeight), 5)
    boxes = []
    colors = [gray, white, gray]
    hi_hat_text = label_font.render('Hi Hat', True, white)
    screen.blit(hi_hat_text, (30, 30))
    snare_text = label_font.render('Snare', True, white)
    screen.blit(snare_text, (30, 130))
    kick_text = label_font.render('Kick', True, white)
    screen.blit(kick_text, (30, 230))
    crash_text = label_font.render('Crash', True, white)
    screen.blit(crash_text, (30, 330))
    clap_text = label_font.render('Clap', True, white)
    screen.blit(clap_text, (30, 430))
    floor_tom_text = label_font.render('Floor Tom', True, white)
    screen.blit(floor_tom_text, (30, 530))
    # draw border lines between horizontal racks/channels
    for i in range(6):
       pygame.draw.line(screen, gray, (0, (instrumentRowHight * i)+instrumentRowHight), (sideMenuWidth-1, (instrumentRowHight * i)+instrumentRowHight), 3)
    # draw in boxes
    for i in range(beats):
        for j in range(instrumentRows):
            if clicks[j][i] == -1:
                color = gray
            else:
                color = green
            
            rectFiller = pygame.draw.rect(screen, color, [i * ((WIDTH - sideMenuWidth) // beats) + (sideMenuWidth+5), (j * instrumentRowHight)+5, ((WIDTH - sideMenuWidth)//beats)-10, ((HEIGHT - bottomMenuHeight)//instrumentRows) -10], 0, 3)
            
            rectFillerFrame = pygame.draw.rect(screen, gold, [i * ((WIDTH - sideMenuWidth) // beats) + (sideMenuWidth), (j * instrumentRowHight), (WIDTH - sideMenuWidth)//beats, ((HEIGHT - bottomMenuHeight)//instrumentRows)], 5, 5)
            
            oldRect = pygame.draw.rect(screen, black, [i * ((WIDTH - sideMenuWidth) // beats) + (sideMenuWidth), (j * instrumentRowHight), (WIDTH - sideMenuWidth)//beats, ((HEIGHT - bottomMenuHeight)//instrumentRows)], 3, 5)
            
            
            boxes.append((rectFiller, (i, j)))
    return boxes

run = True
while run:
    timer.tick(fps)
    screen.fill(black)
    boxes = draw_grid(clicked)
    
    
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
                            # check if mouse click is inside any of the boxes
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(boxes)):
                currentRect = boxes[i][0]
                coords = boxes[i][1]
                if currentRect.collidepoint(event.pos):
                    clicked[coords[1]][coords[0]] += -1
                
    # draw to screen
    pygame.display.flip()

# backup in case code reaches this point
pygame.quit()