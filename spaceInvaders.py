import pygame

# initialize the game 
pygame.init()

#create a screen
screen = pygame.display.set_mode((800,600))

#display windows name
pygame.display.set_caption('Space Invaders')

#load the image
playerImage = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480
playerX_change = 0

# def enemy(x,y):
#     screen.blit(enemyImage,(x,y))

def player(x,y):
    screen.blit(playerImage,(x,y))
    

running = True

while running:
    # Screen color RGB - Red - Green - Blue 
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change -= 0.3 
            if event.key == pygame.K_RIGHT:
                playerX_change += 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    #movement of player     
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736

    #place the image on game windows
    player(playerX,playerY)
    pygame.display.update()
