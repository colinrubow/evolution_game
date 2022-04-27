import sys, pygame
pygame.init()

SIZE = width, height = (320, 240)
BACKGROUND_COLOR = (255, 255, 255) # white
SCREEN = pygame.display.set_mode(SIZE)
SCREEN.fill(BACKGROUND_COLOR)
RECT = pygame.Rect(50, 50, 10, 10)

num_turns = 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('number of turns: ', num_turns)
            sys.exit()

    pygame.draw.rect(SCREEN, (35, 199, 40), RECT)
    pygame.display.flip()