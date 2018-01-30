# Computer Programming 1
# Unit 11 - Graphics
#
# A scene that uses loops to make stars and make a picket fence.


# Imports
import pygame
import random

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Sunny Day"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

#Images
PICTURE = pygame.image.load('ending.png')
cloud_pic = pygame.image.load('Meteor.png')

# Colors
GREEN = (9, 91, 22)
WHITE = (255, 255, 255)
BLUE = (75, 200, 255)
YELLOW = (255, 255, 175)
GREY = (110, 112, 117)
GREYbLUE = (177, 185, 206)
RED = (237, 40, 40)

# Make stars #
stars = []
for i in range(200):
    x = random.randrange(0, 800)
    y = random.randrange(0, 800)
    r = random.randrange(1, 5)
    s = [x, y, r, r]
    stars.append(s)


# Make clouds
num_clouds = 60
clouds = []
for i in range(num_clouds):
    x = random.randrange(-800, 100)
    y = random.randrange(50, 200)
    loc = [x, y]
    clouds.append(loc)

daytime = True
lights_on = False

def draw_cloud(loc):
    x = loc[0]
    y = loc[1]

    if daytime:
        pygame.draw.ellipse(screen, WHITE, [x, y + 20, 40 , 40])
        pygame.draw.ellipse(screen, WHITE, [x + 60, y + 20, 40 , 40])
        pygame.draw.ellipse(screen, WHITE, [x + 20, y + 10, 25, 25])
        pygame.draw.ellipse(screen, WHITE, [x + 35, y, 50, 50])
        pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 60, 40])

    else:
        screen.blit(cloud_pic, (x,y))

   
# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                daytime = not daytime
     # google 'pygame key constants' for more keys

    # Game logic
    for c in clouds:
        c[0] += 4

        if c[0] > 1000:
           c[0] = random.randrange(-800, -100)
           c[1] = random.randrange(-300, 200)

    for s in stars:
        s[0] += 2
        s[1] += 4

        if s[1] > 1000:
           s[0] = random.randrange(-800, 20)
           s[1] = random.randrange(-1600, 40)

   
    # Drawing code\
    ''' sky '''
    if daytime:
        screen.fill(BLUE)

    else:
        screen.blit(PICTURE, (0, 0))



    ''' sun '''
    if daytime:
        pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])

    else:
        pygame.draw.ellipse(screen, RED, [575, 75, 100, 100])


    ''' clouds '''
    if daytime:
        for c in clouds:
            draw_cloud(c)

    else:
       for c in clouds:
           screen.blit(cloud_pic, (x, y))


    ''' stars '''
    for s in stars:
        pygame.draw.ellipse(screen, YELLOW, s)

    ''' grass '''
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])

    ''' stars '''
    if daytime:
        for s in stars:
            pygame.draw.ellipse(screen, YELLOW, s)
    else:
        for s in stars:
            pygame.draw.ellipse(screen, RED, s)
        
    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, WHITE, [0, 410], [800, 410], 5)


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
