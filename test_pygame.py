import pygame   # za grafiku
import sys
from pygame import time
from pygame.locals import *

# inicijalizujemo pygame, odnosno kanvas na kome cemo iscrtavati
pygame.init()
# visina i sirina se mogu menjati i to nece uticati na crtanje 
width  = 600
height = 600
# u svim funkcijama za crtanje u pygamu, uvek se prvo podesava sirina pa visina
canvas = pygame.display.set_mode((width,height))
# definisemo boje
white = (255,255,255)
black = (0,0,0)
red   = (255,0,0)
green = (0,255,0)
blue  = (0,0,255)
yellow = (255,255,0)

while True:
    # popunjavamo kanvas crnom bojom
    canvas.fill(black)

    pygame.draw.rect(canvas,red,(0,0,width//2,height//3),0)
    pygame.draw.circle(canvas,red,(3*width//4,height//2-100),50,0)
    pygame.display.update()
    pygame.time.delay(1000);

    pygame.draw.rect(canvas,yellow,(0,height//3,width//2,height//3),0)
    pygame.draw.circle(canvas,yellow,(3*width//4,height//2),50,0)
    pygame.display.update()
    pygame.time.delay(1000);

    pygame.draw.rect(canvas,green,(0,2*height//3,width//2,height),0)
    pygame.draw.circle(canvas,green,(3*width//4,height//2+100),50,0)
    pygame.display.update()
    pygame.time.delay(1000);


    # bitno je proveravati i stanje pygame displeja
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # ukoliko ne dodje do prekida, potrebno je updejtovati trenutno stanje displeja
    pygame.display.update()
