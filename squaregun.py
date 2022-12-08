import pygame
HEIGHT = 500
WIDTH = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
SPEED = 5
class Squaregun(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load('assets/littlebullet.png')
        self.rect = self.image.get_rect()
        self.moving = False

    def fire(self):
        if self.moving == True:
            self.rect.x += SPEED
