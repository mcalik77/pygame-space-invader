import pygame
import random
import math

# initialize pygame
pygame.init()

# create a screen
screen = pygame.display.set_mode((800, 600))

# change the title
pygame.display.set_caption('Space Invaders')

# add background image
background = pygame.image.load('pygame/background.png')
# change the icon
icon = pygame.image.load('pygame/ufo.png')
pygame.display.set_icon(icon)

# loading player image
playerImage = pygame.image.load('pygame/space-invaders.png')
playerX = 370
playerY = 480
playerX_change = 0

#list to store enemies
enemyImage = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

# loading enemy image
for i in range(num_of_enemies):
    enemyImage.append(pygame.image.load('pygame/enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(3)
    enemyY_change.append(30)

# loading bullet image
# ready state - you cant see the bullet on the screen
# fire state - the bullet is currently moving
bulletImage = pygame.image.load('pygame/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('pygame/Roboto-Light.ttf',32)

textX = 10
textY = 10

#text score
def show_score(x,y):
    score = font.render("Score :" + str(score_value),True, (255,255,255))
    screen.blit(score, (x, y))

# player
def player(x, y):
    screen.blit(playerImage, (x, y))

# enemy


def enemy(x, y, i):
    screen.blit(enemyImage[i], (x, y))

# bullet


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImage, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) +
                         (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game loop
running = True
while running:
    # Screen color
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # if keystroke pressed whether check left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = - 5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # player moving on x coordinate
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # enemy moving on x coordinate
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = - 3
            enemyY[i] += enemyY_change[i]

        # collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        
        enemy(enemyX[i], enemyY[i], i)

    # bullet state
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    # bullet movement
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # calling player and enemy function to print on screen
    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
