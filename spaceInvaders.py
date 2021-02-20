import pygame

# initialize the game 
pygame.init()

#create a screen
screen = pygame.display.set_mode((800,600))

#display windows name
pygame.display.set_caption('Space Invaders')

#load the image
playerImage = pygame.image.load('pygame/space-invaders.png')


def player(x,y):
    screen.blit(playerImage,(x,y))


running = True
while running:
    # Screen color
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #place the image on game windows
    player(370,480)
    pygame.display.update()