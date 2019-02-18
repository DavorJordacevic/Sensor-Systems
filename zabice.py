import pygame
import sys
import serial
import random
from pygame import time
from pygame.locals import *

ser = serial.Serial()
ser.timeout = 1
ser.port = 'com3' 
ser.open()

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

position = [0,1,2,3]
positions= [[200,200],[600,200],[200,600],[600,600]]

iteration = 0
score = 0

def draw_circle(_color,_random_state):
	if _color == 0:
		pygame.draw.circle(screen, blue, positions[position[_random_state]], 50)
	elif _color == 1 :
		pygame.draw.circle(screen, green, positions[position[_random_state]], 50)
	else:
		pygame.draw.circle(screen, red, positions[position[_random_state]], 50)

def draw_text(_score,_text_size):
    _font = pygame.font.Font('freesansbold.ttf',_text_size)
    _text = _font.render(_score, True,white,red)
    screen.blit(_text,(10,10))

def read(ser):
    x_y = ser.readline()
    x_y = x_y.decode()
    x_y = x_y[:len(x_y)-2]
    x_y = x_y.split(";")
    if len(x_y)!=2 or ("" in x_y):
        return(False)
    return(x_y)

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
	    pygame.draw.rect(screen,red,[0,screen_height//2 -5,screen_width,10],0)
	    pygame.draw.rect(screen,red,[screen_width//2 -5,0,10,screen_height],0)

	    # crtanje kruga
	    random_state = random.randint(0,3)
	    random_color = random.randint(0,2)
	    draw_text(str(score),36)
	    draw_circle(random_color,random_state)

	    for event in pygame.event.get():
	    	if event.type == QUIT:
	            pygame.quit()
	            sys.exit()
	    pygame.display.flip()

	    x_y = read(ser)
	    temp_position = 0 if x_y[0]==1 and x_y[1]==3
	    temp_position = 1 if x_y[0]==2 and x_y[1]==3
	    temp_position = 2 if x_y[0]==1 and x_y[1]==4
	    temp_position = 3 if x_y[0]==2 and x_y[1]==4

	    if temp_position == random_state:
	    	score += 2
	    	if iteration == 20:
	    		done = True
	    		draw_text(str(score),128)
	    		time.delay(5000)
	    	iteration += 1
	    	continue
	    else:
	    	if iteration == 20:
	    		done = True
	    	iteration += 1
	    	score-= 1 
	
	    clock.tick(60)
	    time.delay(1000)

    pygame.quit()

if __name__ == "__main__":
    main()