import pygame, math, datetime

res = w, h = 1080, 720

pygame.init() # This kicks things off. It initializes all the modules required for PyGame.
done = False
image = pygame.image.load("tsis7/imgs/mickeyclock.png") # imgs by Arukame Suzuya (https://vk.com/arukame)
img = pygame.transform.scale(image, (res))
screen = pygame.display.set_mode(res) # resolution of image

# right hand - minutes
minutes = pygame.image.load("tsis7/imgs/righthand.png")
# left hand - seconds
seconds = pygame.image.load("tsis7/imgs/lefthand.png")

clck = dict(zip(range(60), range(0, 360, 6))) # for minutes and seconds

def clock_seconds(clock_dict, second): # to seconds points last finger
    scndnewpos = pygame.transform.rotate(seconds, -(clock_dict[second]+50))    
    screen.blit(scndnewpos, (w/2 - int(scndnewpos.get_width() / 2), h/2 - int(scndnewpos.get_height() / 2)))
def clock_minutes(clock_dict, minute): # with minutes it much easier
    mntnewpos = pygame.transform.rotate(minutes, -(clock_dict[minute]-59))    
    screen.blit(mntnewpos, (w/2 - int(mntnewpos.get_width() / 2), h/2 - int(mntnewpos.get_height() / 2)))


while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        screen.fill((255, 255, 255))
        
        screen.blit(img, (0, 0))

        t = datetime.datetime.now()
        mnt, scnd = t.minute, t.second
        clock_seconds(clck, scnd)
        clock_minutes(clck, mnt)

        pygame.display.flip()