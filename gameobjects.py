import pygame
from imageloader import *
class Background(pygame.sprite.Sprite):
    def __init__(self,image,width,height):
        self.orgimage = pygame.image.load(image)
        self.image = pygame.transform.scale(self.orgimage,(width,height))
        self.rect = self.image.get_rect()

    def update(self):
        return

class player(pygame.sprite.Sprite):
    def __init__(self,image,size,clip):
        self.asset = imageLoader(image,size,clip)
        self.image = self.asset
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 200
        self.velocityx = 0
        self.velocityy = 0
        self.accelerationx = 0
        self.accelerationy = 0
        self.thrust = 0.5
        self.angle = 0
        self.damp = 0.3
        self.maxvelocity = 8
        self.collision = False
        self.collisionGroup =[]

    def update(self):
        #process player Input
        input = self.getPlayerInput()

        angle = self.processcontrols(input)
        self.image = pygame.transform.rotate(self.asset,self.angle)

        # update the physics
        self.updatephysics()

        # collision detectioin here
        self.collisionDetectionHere()

    def collisionDetectionHere(self):
        for gameobjects in self.collisionGroup:
            self.collision = self.rect.colliderect(gameobjects.rect)
            if self.collision:
                break

    def getPlayerInput(self):
        up = pygame.key.get_pressed()[pygame.K_UP]
        down = pygame.key.get_pressed()[pygame.K_DOWN]
        right = pygame.key.get_pressed()[pygame.K_RIGHT]
        left = pygame.key.get_pressed()[pygame.K_LEFT]

        return (up ,down , right  ,left)
    def processcontrols(self,control):
        self.angle = 0
        if control[0]==1 and control[1]==0 and control[2]==0 and control[3]==0:
           self.angle = 0
        elif control[0]==1 and control[1]==0 and control[2]==1 and control[3]==0:

            self. angle = 315
        elif control[0]==0 and control[1]==0 and control[2]==1 and control[3]==0:

            self.angle = 270
        elif control[0]==1 and control[1]==0 and control[2]==0 and control[3]==1:

            self.angle = 45
        elif control[0]==0 and control[1]==0 and control[2]==0 and control[3]==1:

            self.angle = 90
        elif control[0]==0 and control[1]==1 and control[2]==0 and control[3]==0:

            self.angle = 180
        elif control[0]==0 and control[1]==1 and control[2]==1 and control[3]==0:

            self.angle = 225
        elif control[0]==0 and control[1]==1 and control[2]==0 and control[3]==1:


            self.angle = 135
        else:
            self.velocityx = 0
            self.velocityy = 0

        self.accelerationx = self.thrust*(control[2] - control[3])
        self.accelerationy = self.thrust*(control[1] - control[0])


    def updatephysics(self):
        self.velocityx += self.accelerationx
        self.velocityy += self.accelerationy

        #damping of speed here
        if (self.velocityx < 0- self.damp):
            self.velocityx += self.damp
        elif (self.velocityx > 0 +self.damp):
            self.velocityx -= self.damp
        else:
            self.velocityx = 0

        if (self.velocityy < 0 - self.damp):
            self.velocityy += self.damp
        elif (self.velocityy > 0 + self.damp):
            self.velocityy -= self.damp
        else:
            self.velocityy = 0

        # capping the max speed of the ship
        if (self.velocityx > self.maxvelocity):
            self.velocityx =self.maxvelocity
        elif (self.velocityx <(self.maxvelocity * -1)):
            self.velocityx= self.maxvelocity * -1
        elif(self.velocityy > self.maxvelocity):
            self.velocityy =self.maxvelocity
        elif (self.velocityy <(self.maxvelocity * -1)):
            self.velocityy= self.maxvelocity * -1


        #defination of boundry here
        if(self.rect.x >=760):
            self.rect.x = 755
        elif(self.rect.x <=0):
            self.rect.x =2
        if(self.rect.y >= 560):
            self.rect.y = 555
        elif(self.rect.y <= 0):
            self.rect.y =2
        self.rect.x += self.velocityx
        self.rect.y += self.velocityy








class enemy(pygame.sprite.Sprite):
    def __init__(self, image, size, clip):
        self.image = imageLoader(image, size, clip)
        #colorkey is used to make the background transparent by giving the hex code of that colour
        self.image.set_colorkey(0x454e5b)
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 100
        self.velocityx = 5
        self.velocityy = 5
        self.accelerationx = 0
        self.accelerationy = 0

    def update(self):
        self.velocityx += self.accelerationx
        self.velocityy += self.accelerationy
        self.rect.x += self.velocityx
        self.rect.y += self.velocityy


class astroid(pygame.sprite.Sprite):
    def __init__(self, image, size, clip):
        self.image = imageLoader(image, size, clip)
        self.image.set_colorkey(0x454e5b)
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 200
        self.velocityx = 0
        self.velocityy = 0
        self.accelerationx = 0
        self.accelerationy = 0

    def update(self):
        self.velocityx += self.accelerationx
        self.velocityy += self.accelerationy
        self.rect.x += self.velocityx
        self.rect.y += self.velocityy
