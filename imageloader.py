import pygame
def imageLoader(image,scale,parameters):
    asset = pygame.image.load(image)
    assetSurface = pygame.Surface((parameters[2],parameters[3]))
    assetSurface.blit(asset,(0,0),parameters)
    assetTransform = pygame.transform.scale(assetSurface,(parameters[2]*scale, parameters[3]*scale))
    return assetTransform