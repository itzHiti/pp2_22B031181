import pygame

res = w, h = 1080, 720

pygame.init() # This kicks things off. It initializes all the modules required for PyGame.
done = False
screen = pygame.display.set_mode(res) # resolution of image
screen.fill((255, 255, 255)) # White background
red = (255, 0, 0) # Red color RGB code

radius = 25
bx = 0
borderx = 0
by = 0
bordery = 0
pygame.draw.circle(screen, red, (w/2,h/2), radius)

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYUP: # key released
                    if event.key == pygame.K_ESCAPE:
                        exit()
                if event.type == pygame.KEYDOWN:
                    if -25 <= borderx <= 25 and -16 <= bordery <= 16:
                        if event.key == pygame.K_LEFT and borderx!=25:
                            bx+=20
                            borderx+=1
                            screen.fill((255, 255, 255))
                            pygame.draw.circle(screen, red, (w/2-bx,h/2-by), radius)
                        elif event.key == pygame.K_RIGHT and borderx!=-25:
                            bx-=20
                            borderx-=1
                            screen.fill((255, 255, 255))
                            pygame.draw.circle(screen, red, (w/2-bx,h/2-by), radius)
                        elif event.key == pygame.K_UP and bordery!=16:
                            by+=20
                            bordery+=1
                            screen.fill((255, 255, 255))
                            pygame.draw.circle(screen, red, (w/2-bx,h/2-by), radius)    
                        elif event.key == pygame.K_DOWN and bordery!=-16:
                            by-=20
                            bordery-=1
                            screen.fill((255, 255, 255))
                            pygame.draw.circle(screen, red, (w/2-bx,h/2-by), radius)  
        pygame.display.update()

