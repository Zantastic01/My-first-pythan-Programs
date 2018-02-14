# Imports
import pygame
import random

shot_fired = False

# Initialize game engine
pygame.init()

# Image
ship = pygame.image.load('ship.png')
bad = pygame.image.load('bad.png')
# Window
SIZE = (800, 600)
TITLE = "Galaga Screen"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Sound Effects
pygame.mixer.music.load("game.ogg")

# Colors
GREEN = (0, 150, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 200)
BLUE = (75, 200, 255)
GREY = (110, 112, 117)
GREYbLUE = (177, 185, 206)
RED = (237, 40, 40)
star_colors = [YELLOW, BLUE, RED, WHITE]

# Block
ship_loc = [400, 450]
vel = [0, 0]
speed = 10

# Make stars #
stars = []
for i in range(200):
    x = random.randrange(800, 1600)
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


lightning_timer = 0

daytime = True
lights_on = False

stormy = True

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
        screen.blit(bad, (x, y))

def draw_spaceship(loc):
    x = ship_loc[0]
    y = ship_loc[1]
    
    screen.blit(ship, (x, y))
    
# Make Bullets
bullets = []

def draw_bullet(loc):
    x = loc[0]
    y = loc[1]

    pygame.draw.rect(screen, WHITE, [x, y, 5, 15])

 
# Game loop
pygame.mixer.music.play(-1)
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                vel[0] = speed
            if event.key == pygame.K_LEFT:
                vel[0] =-1 *  speed
            if event.key == pygame.K_SPACE:
                daytime = not daytime
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                vel[0] = 0
            if event.key == pygame.K_LEFT:
                vel[0] = 0
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    shot_fired = True
                
    # Game logic
    ship_loc[0] += vel[0]

    if ship_loc[0] < -40:
        ship_loc[0] = 840
    if ship_loc[0] > 840:
        ship_loc[0] = -40\

    if shot_fired == True:
        bullets.append([ship_loc[0] + 64, ship_loc[1]])
        shot_fired = False
        
    for b in bullets:
        b[1] -= 24

    for c in clouds:
        c[0] += 4

        if c[0] > 1000:
           c[0] = random.randrange(-800, -100)
           c[1] = random.randrange(-300, 200)

    for s in stars: 
        if daytime: 
            s[0] -= 1
            s[1] += 4

            if s[1] > 1000:
               s[0] = random.randrange(0, 1000)
               s[1] = random.randrange(-100, 0)
        else:
            s[1] += 3
            
            if s[1] > 1000:
               s[0] = random.randrange(0, 1000)
               s[1] = random.randrange(-100, 0)

    ''' flash lighting '''
    if stormy:
        if random.randrange(0, 150) == 0:
            lightning_timer = 5
        else:
            lightning_timer -= 1


    # Drawing code
    ''' sky '''
    if daytime:
        if lightning_timer > 0:
            screen.fill(WHITE)
        else:
            screen.fill(BLUE)
    else:
        screen.fill(BLACK)


    ''' ship '''
    draw_spaceship(ship_loc)
    
    for b in bullets:
        draw_bullet(b)

    ''' sun '''
    if daytime:
        pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])

    else:
        pygame.draw.ellipse(screen, WHITE, [575, 75, 100, 100])
 

    ''' clouds '''
    if daytime:
        for c in clouds:
            draw_cloud(c)
    else:
        for i, c in enumerate(clouds):
            if i % 3 == 0:
                screen.blit(bad, c)
            
    ''' Rain / stars '''
    if daytime:
        for s in stars:
            pygame.draw.ellipse(screen, YELLOW, s)
    else:
        for s in stars:
            color = random.choice(star_colors)
            pygame.draw.ellipse(screen, color, s)
        

    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
