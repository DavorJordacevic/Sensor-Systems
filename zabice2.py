# za grafiku
import pygame
# omogucava pristup nekim promenljivama koje koristi ili odrzava prevodilac
import sys
# za komunikaciju preko serijskog porta
import serial
# za generisanje random brojeva
import random

from pygame import time
from pygame.locals import *

# otvaramo port 'com3' i podesavamo baud rate na 9600 bauda
ser = serial.Serial("com3", 9600)
# set timeout to x seconds (float allowed) returns immediately when the requested number of bytes 
# are available, otherwise wait until the timeout expires and return all bytes that were received until then.
ser.timeout = 0.5

# podesavamo parametre za ekran na kome ce se prikazivati, i inizijalizujemo sam pygame
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
# velicina loptice
ball_size = 50
# pozicije po kvadrantima
position = [0,1,2,3]
# tacne koordinate centra tacaka po kvadrantima
positions= [[200,200],[600,200],[200,600],[600,600]]

# cuvanje broja iteracija programa koji ce se pokretati
iteration = 0
score = 0

# draw_circle se koristi za crtanje loptice na ekranu
# pygame.draw sadrzi funkciju za crtanje kruga kojoj treba proslediti na kom ekranu crta,
# boju, poziciju centra kruga, i poluprecnik.
def draw_circle(_color,_random_state):
	if _color == 0:
		# za random_state koje je u opsegu [0,3] uzimamo poziju kvadranta, i na osnovu toga poziciju u tom kvadrantu
		pygame.draw.circle(screen, blue, positions[position[_random_state]], 50)
	elif _color == 1 :
		pygame.draw.circle(screen, green, positions[position[_random_state]], 50)
	else:
		pygame.draw.circle(screen, red, positions[position[_random_state]], 50)

# draw_text sluzi za ispisivanje teksta na ekran
# tekst ce biti rezultat koji je korisnik ostvario
# iz pygame.font uzimamo font, i velicinu fonta
# nakon cega renderujemo tekst i postavljamo ga na ekran na poziciji (10,10)
def draw_text(_score,_text_size):
    _font = pygame.font.Font('freesansbold.ttf',_text_size)
    _text = _font.render(_score, True,white,red)
    screen.blit(_text,(10,10))

def read(ser):
    #while True:
        #ser.write(b'S')
    # procitatnu vrednost je potrebno dekodovati i iseci deo koji sluzi za prelazak u naredni red
    x_y = ser.readline().decode().strip('\r\n')
        #x_y = int(x_y)
        #x_y = x_y.decode()
        #x_y = x_y[:len(x_y)-2]
        #x_y = x_y.split(";")
        #print(x_y)
        #if(x_y==''):
            #continue
        #break;
    #x_y = ord(x_y)
        
    return(x_y)

def main():
	# petlja ce se izvrsavati sve dok je done ne bude true
    done = False
    #clock = pygame.time.Clock()
    global iteration
    global score
    while not done:
    	# popunjavamo ekran crnom bojom
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
	    # generisanje random broja u opsegu [0,3] kao i boje [0,2]
	    random_state = random.randint(0,3)
	    random_color = random.randint(0,2)
	    # poziva se funkcija za ispis rezultata i crtanje kruga
	    draw_text(str(score),36)
	    draw_circle(random_color,random_state)

	    # vrsi se provera u kojoj proveravamo da li je doslo do kraja programa
	    # u tom slucaju zatvaramo pygame
	    for event in pygame.event.get():
	        if event.type == QUIT:
	            pygame.quit()
	            sys.exit()
	    # ukoliko je provera prosla, updejtujemo display
	    pygame.display.flip()


	    #x_y = read(ser)
	    #x_y = [1,3]

	    #if x_y[0]==1 and x_y[1]==3:
	    	#temp_position = 0
	    #else:
	    	#if x_y[0]==2 and x_y[1]==3:
	    		#temp_position = 1
	    	#else:
	    		#if x_y[0]==1 and x_y[1]==4:
	    			#temp_position = 2
	    		#else:
	    			#if x_y[0]==2 and x_y[1]==4:
	    				#temp_position = 3
	    			#else:
	    				#temp_position = 4
	    # citamo poziciju joysticka koju smo kroz arduino prosledili na serijski port
	    temp_position = read(ser)
	    # pretvaramo random_state u string
	    random_state = str(random_state)
	    
	    print(random_state,"  ",temp_position)
	    # ako je pozicija joystick-a jednaka random poziciji na kojoj je lopta
	    # potrebno je povecati rezultat
	    if temp_position == random_state:
	    	score += 1
	    	# ukoliko je broj iteracija 50
	    	# postavljamo done=true sto ce znaciti kraj petlje i ispisujemo
	    	# tekst za rezultatom koji zadrzavamo na ekranu 5 sekundi
	    	if iteration == 50:
	    		done = True
	    		draw_text(str(score),128)
	    		time.delay(5000)
	    	# ako broj ponavljanja petlje nije 50, potrebno je povecati taj broj
	    	iteration += 1
	    	time.delay(1000)
	    	# pomocu continue skacemo na narednu iteraciju i deo ispod njega se nece izvrsiti
	    	continue
	    else:
	    	# i ukoliko je promasena pozicija, potrebno je proveriti broj iteracija petlje
	    	if iteration == 50:
	    		done = True
	    	iteration += 1
	    	# potrebno je i smanjiti rezultat
	    	score-= 1 
	    #clock.tick(60)
	    time.delay(1000)
    
    # izlazak iz pygame-a
    pygame.quit()

#  By doing the main check, you can have that code only execute when you want to run the module as 
# a program and not have it execute when someone just wants to import your module and call your functions themselves.
if __name__ == "__main__":
    main()
