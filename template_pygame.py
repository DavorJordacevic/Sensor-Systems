import pygame   # za grafiku
import sys
from pygame.locals import *

# inicijalizujemo pygame, odnosno kanvas na kome cemo iscrtavati
pygame.init()
# visina i sirina se mogu menjati i to nece uticati na crtanje 
width  = 700
height = 700
# u svim funkcijama za crtanje u pygamu, uvek se prvo podesava sirina pa visina
canvas = pygame.display.set_mode((width,height))
# definisemo boje
white = (255,255,255)
black = (0,0,0)
red   = (255,0,0)
green = (0,255,0)
blue  = (0,0,255)

while True:
    # popunjavamo kanvas crnom bojom
    canvas.fill(black)
    
    """
		U ovom delu ce se nalaziti sve sto ima veze sa iscrtavanjem


		# Funkcije treba definisati van tela petlje, te i u petlji samo pozivati!
    """

    # bitno je proveravati i stanje pygame displeja
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # ukoliko ne dodje do prekida, potrebno je updejtovati trenutno stanje displeja
    pygame.display.update()
