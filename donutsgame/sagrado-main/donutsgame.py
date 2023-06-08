import pygame
import sys
import random 

ancho = 800
alto = 600
HOMER_SPEED = 10
DONUT_SPEED = 5
FPS = 60

pygame.init()

clock = pygame.time.Clock()

pygame.mixer.music.load("./assets/sounds/ouch.mp3")
# pygame.mixer.music.set_pos(0.4)
Score = 0

flag_donut = True
flag_donut2 = True



font = pygame.font.Font("./assets/fonts/simpsons.ttf", 48)



screen=pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Donuts Game")

donut = pygame.image.load("./assets/images/dona.png").convert_alpha()
donut = pygame.transform.scale(donut, (60, 60))
rect_donut = donut.get_rect()
x_donut = random.randrange(30, ancho -30)
rect_donut.midtop = (x_donut // 2, 0)

fondo = pygame.image.load("./assets/images/background.jpg").convert()
fondo = pygame.transform.scale(fondo ,(ancho, alto))
homer_R = pygame.image.load("./assets/images/homer_right.png").convert_alpha()
homer_R = pygame.transform.scale(homer_R, (150, 200))
homer_L = pygame.image.load("./assets/images/homer_left.png").convert_alpha()
homer_L = pygame.transform.scale(homer_L, (150,200))

homer = homer_L
rect_homer = homer_L.get_rect()
rect_homer.midbottom = (ancho // 2, alto)
donut = pygame.image.load("./assets/images/dona.png").convert_alpha()
donut = pygame.transform.scale(donut, (60, 60))
rect_donut = donut.get_rect()
x_donut = random.randrange(30, ancho -30)
rect_donut.midtop = (x_donut // 2, 0)


while True:
    
    screen.blit(fondo, (0, 0))
    
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        if rect_homer.right <= ancho: 
          rect_homer.x += HOMER_SPEED 
          homer = homer_R      
           
               

    if keys[pygame.K_LEFT]:
        if rect_homer.left >= 0:
          rect_homer.x -= HOMER_SPEED    
          homer = homer_L    
               
    if flag_donut2: 
       donut = pygame.image.load("./assets/images/dona.png").convert_alpha()
       donut = pygame.transform.scale(donut, (60, 60))
       rect_donut = donut.get_rect()
       rect_donut.x = random.randrange(30, ancho -30)
       flag_donut2 = False
       flag_donut = True
   
   
   
   
    if rect_donut.bottom <= alto:
       rect_donut.y += DONUT_SPEED

       if rect_donut.colliderect(rect_homer):
          if flag_donut:
           pygame.mixer.music.play()
           Score += 1
           flag_donut2 = True
           flag_donut = False
          

    texto = font.render("Score=" + str(Score) , True, (0, 0, 0))


    screen.blit(texto, (30, 30))
    screen.blit(homer, rect_homer)        
    if flag_donut:
     screen.blit(donut, rect_donut)

    pygame.display.flip()
