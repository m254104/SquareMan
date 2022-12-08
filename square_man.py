import pygame
SPEED = 2
WIDTH = 800
HEIGHT = 500
pygame.mixer.init()
death = pygame.mixer.Sound('assets/death.mp3')
import time
import sys
class SquareMan(pygame.sprite.Sprite):

    def __init__(self, position):
        super().__init__()
        self.no_hit_image = pygame.image.load('assets/Square_man.png')
        self.one_hit_image = pygame.image.load('assets/SM_Hit1.png')
        self.two_hit_image = pygame.image.load('assets/SM_Hit2.png')
        self.three_hit_image = pygame.image.load('assets/SM_Dead.png')
        self.image = self.no_hit_image
        self.rect = self.image.get_rect()
        self.rect.center = position
        y = self.rect.y
        x = self.rect.x
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        self.health = 0
    def update(self):
        if self.moving_left and self.rect.x > 0:
            self.rect.x -= SPEED
        if self.moving_right and self.rect.x < WIDTH:
            self.rect.x += SPEED
        if self.moving_up and self.rect.y > 50:
            self.rect.y -= SPEED
        if self.moving_down and self.rect.y < HEIGHT - 50:
            self.rect.y += SPEED
        if self.health < 15:
            self.image = self.no_hit_image
        if self.health > 15:
            self.image = self.one_hit_image
        if self.health > 30:
            self.image = self.two_hit_image
        if self.health > 45:
            self.image = self.three_hit_image
            time.sleep(1)
            pygame.mixer.music.stop()
            time.sleep(0.75)
            pygame.mixer.Sound.play(death)
            time.sleep(1)
            sys.exit()



