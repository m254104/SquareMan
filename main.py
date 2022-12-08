import pygame
import sys
import time
from square_man import SquareMan
from bullet import Arrow
from pew import Pellet
from obstacle import Obstacle
import random


HEIGHT = 500
WIDTH = 800
pygame.mixer.init()
music = pygame.mixer.music.load('assets/music.mp3')
square_man = SquareMan((250, 250))
arrow1 = Arrow((WIDTH, random.randint(60, 400)))
arrow2 = Arrow((WIDTH, random.randint(60, 400)))
pellet = Pellet((WIDTH, random.randint(60, 400)))
obstacle1 = Obstacle((WIDTH + 500, 450))
obstacle2 = Obstacle((WIDTH, 250))
gameobjects = pygame.sprite.Group(square_man, arrow1, arrow2, pellet, obstacle1, obstacle2)
gameprojectiles = pygame.sprite.Group(arrow1, arrow2, obstacle1, obstacle2)


wall = pygame.image.load('assets/tile_0034.png')
wall_rect = wall.get_rect()

ground = pygame.surface.Surface((WIDTH, 50))

pygame.init()
pygame.mixer.music.play(-1)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen_rect = screen.get_rect()
tiles = screen_rect.width//wall_rect.width

pygame.display.set_caption("Squareman")

clock = pygame.time.Clock()
def background():
    for y in range(tiles):
        for x in range(tiles):
            screen.blit(wall, (x * wall_rect.width, y * wall_rect.height))

def key_check():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            square_man.moving_left = True
        if event.key == pygame.K_RIGHT:
            square_man.moving_right = True
        if event.key == pygame.K_UP:
            square_man.moving_up = True
        if event.key == pygame.K_DOWN:
            square_man.moving_down = True
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            square_man.moving_right = False
        if event.key == pygame.K_LEFT:
            square_man.moving_left = False
        if event.key == pygame.K_UP:
            square_man.moving_up = False
        if event.key == pygame.K_DOWN:
            square_man.moving_down = False

def crash():
    if pygame.sprite.spritecollideany(square_man, gameprojectiles):
        square_man.health += 1
    elif pygame.sprite.collide_rect(square_man, pellet):
        square_man.health -= 5
        pellet.rect.x = WIDTH + 800

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or square_man.health == 45:
            sys.exit()

    background()
    square_man.update()
    arrow1.update()
    arrow2.update()
    pellet.update()
    obstacle1.update()
    obstacle2.update()
    crash()
    gameobjects.draw(screen)
    screen.blit(ground, (0, HEIGHT-50))
    screen.blit(ground, (0, 0))
    key_check()
    pygame.display.flip()
    clock.tick(75)
