import pygame
import datetime

res = w, h = 1080, 720

pygame.init() # This kicks things off. It initializes all the modules required for PyGame.
done = False
image = pygame.image.load("tsis7/imgs/mickeyclock.jpeg")
img = pygame.transform.scale(image, (res))
screen = pygame.display.set_mode(res) # resolution of image
clock = pygame.time.Clock() # time control (in milliseconds), creates object Clock which helps to control time


# right hand - minutes

# left hand - seconds


while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        screen.fill((255, 255, 255))
        
        screen.blit(img, (0, 0))
        
        pygame.display.flip()