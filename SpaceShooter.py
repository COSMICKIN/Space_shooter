import pygame ,sys
from gameobjects import *
from imageloader import *
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))

gameObjects =[]

background = Background("images/Nebula1.bmp",screen.get_width(),screen.get_height())
#screen.blit(background.image,(0,0))

player = player("images/Hunter1.bmp",2,(25,1,23,23))
gameObjects.append(player)
#playerRotated = pygame.transform.rotate(player.image,30)
#screen.blit(player.image,(0,0))



enemy =enemy("images/SpacStor.bmp",1,(101,13,91,59))
#screen.blit(enemy.image,(400,300))
gameObjects.append(enemy)
player.collisionGroup.append(enemy)

astroid = astroid("images/Rock2a.bmp",1,(6,3,80,67))
#screen.blit(astroid.image,(700,150))
gameObjects.append(astroid)
player.collisionGroup.append(astroid)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    #update object


    for gameobject in gameObjects:
        gameobject.update()

    #rendering logic
    if player.collision:
        screen.fill((255,0,0))
    else:
        screen.blit(background.image ,(0,0))
    for gameobject in gameObjects:
        screen.blit(gameobject.image, (gameobject.rect.x, gameobject.rect.y))

    pygame.display.flip()
    #waste extra work
    clock.tick(60)