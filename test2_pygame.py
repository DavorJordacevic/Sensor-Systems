import pygame   # za grafiku
import sys
from pygame import time
from pygame.locals import *
import random

# visina i sirina se mogu menjati i to nece uticati na crtanje 
screen_width  = 800
screen_height = 800
size=[screen_width,screen_height]
# definisemo boje
white = (255,255,255)
black = (0,0,0)
red   = (255,0,0)
green = (0,255,0)
blue  = (0,0,255)
yellow = (255,255,0)
ball_size = 25

class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0

def create_ball():
    ball = Ball()
    ball.x = random.randrange(ball_size, screen_width - ball_size-10)
    ball.y = random.randrange(ball_size, screen_height - ball_size-10)
    ball.change_x = random.randrange(-2, 3)
    ball.change_y = random.randrange(-2, 3)
    return ball

def main():
    pygame.init()
    screen = pygame.display.set_mode(size)
    done = False
    clock = pygame.time.Clock()
    ball_list = []
    ball = create_ball()
    ball_list.append(ball)
 
    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ball = create_ball()
                    ball_list.append(ball)
 
        for ball in ball_list:
            ball.x += ball.change_x
            ball.y += ball.change_y
 
            if ball.y > screen_height - ball_size -10 or ball.y < ball_size:
                ball.change_y *= -1
            if ball.y < 10 + ball_size or ball.y < ball_size:
                ball.change_y *= -1
            if ball.x > screen_width - ball_size -10 or ball.x < ball_size:
                ball.change_x *= -1
            if ball.x < 10 + ball_size or ball.x < ball_size:
                ball.change_x *= -1   

        screen.fill(black)

        pygame.draw.rect(screen,red,(0,screen_height-10,screen_width,screen_height),0)
        pygame.draw.rect(screen,red,(0,0,10,screen_height),0)
        pygame.draw.rect(screen,red,(screen_width-10,0,screen_width,screen_height),0)
        pygame.draw.rect(screen,red,(0,0,screen_width,10),0)

        for ball in ball_list:
            pygame.draw.circle(screen, white, [ball.x, ball.y], ball_size)

        clock.tick(60)
 
        pygame.display.flip()
 
    pygame.quit()
 
if __name__ == "__main__":
    main()
