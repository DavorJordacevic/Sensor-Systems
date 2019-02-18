import pygame
import sys
#import serial
import random
from pygame import time
from pygame.locals import *

# visina i sirina se mogu menjati i to nece uticati na crtanje 
screen_width  = 800
screen_height = 800
size=[screen_width,screen_height]
pygame.init()
screen = pygame.display.set_mode(size)
# definisemo boje
white = (255,255,255)
black = (0,0,0)
red   = (255,0,0)
green = (0,255,0)
blue  = (0,0,255)
yellow= (255,255,0)
ball_size = 50

position = [0,1,2,3,4,5,6,7,8]
positions= [[135,135],[395,135],[660,135],[135,405],[395,405],[660,405],[135,675],[395,675],[660,675]]

iteration = 0
score = 0

def random_position():
	return random.randint(0,8)

def draw_circle(_color,_random_state):
	if _color == 0:
		pygame.draw.circle(screen, blue, positions[position[_random_state]], 50)
	elif _color == 1 :
		pygame.draw.circle(screen, green, positions[position[_random_state]], 50)
	else:
		pygame.draw.circle(screen, red, positions[position[_random_state]], 50)

def main():
    done = False
    clock = pygame.time.Clock()
    global iteration
    global score
    while not done:

	    screen.fill(black)
	    # crtanje okvira
	    pygame.draw.rect(screen,red,(0,screen_height-10,screen_width,screen_height),0)
	    pygame.draw.rect(screen,red,(0,0,10,screen_height),0)
	    pygame.draw.rect(screen,red,(screen_width-10,0,screen_width,screen_height),0)
	    pygame.draw.rect(screen,red,(0,0,screen_width,10),0)
	    # crtanje linija
	    pygame.draw.rect(screen,red,[0,screen_height//3 -5,screen_width,5],0)
	    pygame.draw.rect(screen,red,[0,2*screen_height//3 -5,screen_width,5],0)
	    pygame.draw.rect(screen,red,[screen_width//3 -5,0,5,screen_height],0)
	    pygame.draw.rect(screen,red,[2*screen_width//3 -5,0,5,screen_width],0)

	    # crtanje kruga
	    random_state = random_position()
	    draw_circle(0,random_state)
	    pygame.display.flip()

	    #	prssed
	    #	CITANJE SA SERIJSKOG PORTA
	    #

	    

	    if iteration == 20:
	    	done = True
	    iteration += 1
	    clock.tick(60)
	    time.delay(1000)

    pygame.quit()
 
if __name__ == "__main__":
    main()