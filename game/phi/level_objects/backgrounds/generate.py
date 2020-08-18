import pygame
import extra_data.images as ei

def generate_background(img,cx,cy):
    
    imge = pygame.surface.Surface((img.get_size()[0]*cx,img.get_size()[1]*cy))
    
    for x in range(cx):
        for y in range(cy):
            imge.blit(img,(x*img.get_size()[0],y*img.get_size()[1]))
    
    return imge