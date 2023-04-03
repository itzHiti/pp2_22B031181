import pygame, sys, random, time
from pygame.locals import *

pygame.init()

res = w, h = 1080, 720

FPS = 360 # FPS depends on speed of sprites
FramePerSec = pygame.time.Clock()
 
# Predefined some colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SPEED = 5
SCORE = 0
# Constant of coin counter
COIN_COUNTER = 0
# Constant of player speed
PLAYER_SPEED = 5.5

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load("tsis8/media/AnimatedStreet.png")
bg = pygame.transform.scale(background, (res))
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((res))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("kCHau")
 
# New class Coin which will inherit pygame's Sprite's class properties and methods 
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Take image from /media/ folder and scale it 75x100
        self.image = pygame.transform.scale(pygame.image.load("tsis8/media/Coin.png").convert_alpha(), (75, 100))
        # Creating HitBoxes of this image
        self.rect = self.image.get_rect()
        # Make it spawn randomly as enemy car
        self.rect.center = (random.randint(30, w-30),0) 
    # Move function
    def move(self):
        # Make it move the same initial speed as enemy car
        self.rect.move_ip(0, 5)
        # When it reaches top it will respawn...
        if (self.rect.top > h):
            self.rect.top = 0
            # ...also randomly
            self.rect.center = (random.randint(30, w-30), 0)
    # Gotcoin function
    def gotcoin(self):
        # When player collects (collides with coin's hitboxes)
        # Coin will respawn at the top
        self.rect.top = 0
        # at random position in x
        self.rect.center = (random.randint(30, w-30), 0)


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        # I was using my own sprites, because I didn't see sources of images before part3
        self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("tsis8/media/Enemy.png"), (100, 200)), 180)
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(30, w-30),0) 

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > h):
            SCORE+=1
            self.rect.top = 0
            self.rect.center = (random.randint(30, w-30), 0)
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.transform.scale(pygame.image.load("tsis8/media/Player.png"), (100, 200))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
 
    def move(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, PLAYER_SPEED)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0, PLAYER_SPEED)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-PLAYER_SPEED, 0)
        if self.rect.right < w:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(PLAYER_SPEED, 0)  
 
         
P1 = Player()
E1 = Enemy()
# New constant C
C = Coin()
 
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C)
 
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#Game Loop
while True:
    
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.25
           
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    scores = font_small.render("SCORE: " + str(SCORE), True, BLACK)
    txt = font_small.render("COINS: " + str(COIN_COUNTER), True, BLACK)
    fps = font_small.render("FPS: " + str(FPS), True, BLACK)
    DISPLAYSURF.blit(bg, (0, 0))
    DISPLAYSURF.blit(scores, (30,30))
    DISPLAYSURF.blit(txt, (w-150,30))
    DISPLAYSURF.blit(fps, (w-150,60))
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('tsis8/media/crash.wav').play()
          time.sleep(0.5)
                    
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (350,300))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()   
    #To be run if collision occurs between Player and Coin
    if pygame.sprite.spritecollideany(P1, coins):
        # Run function "gotcoin"
        C.gotcoin()
        # Add +1 to coin counter
        COIN_COUNTER+=1
        # Player speed will change to +0.25 when user will collect coins, so he can move faster and avoid crashes faster
        PLAYER_SPEED = 0.25 + PLAYER_SPEED

         
    pygame.display.update()
    FramePerSec.tick(FPS)