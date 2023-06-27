import pygame , sys
from imageloader import *
iu = pygame.image.load("images/iu.bmp")
iutrans = pygame.transform.scale(iu,(600,900))
#x,y=iutrans.get_width(),iutrans.get_height()
screen = pygame.display.set_mode((600,750))
surface = pygame.Surface((600 ,750))
surface.blit(iutrans,(0,0),(0,125,600,700))
#bird = imageLoader("images/bird1.bmp",4,(0,0,60,35))
#surface = pygame.Surface((30,30))
#bird.set_colorkey((247,247,246,255))
#screen.blit(bird,(300,300))

iuPixelArray = pygame.PixelArray(surface)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    for x in range(0,surface.get_width()):
        for y in range(0,surface.get_height()):
            pixel = iuPixelArray[x,y]
            if pixel > 0x444444:
                iuPixelArray[x,y] = 0xFFFFFF
    screen.blit(iuPixelArray.make_surface(),(0,0))



    # for edges
    #screen.blit(pygame.transform.laplacian(surface),(0,0))
    #for filling the screen with average color of the image
    #screen.fill(pygame.transform.average_color(surface))
    pygame.display.flip()
