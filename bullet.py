import pygame
import random
SPEED = 3.2
WIDTH = 800
HEIGHT = 500
class Arrow(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 45))
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.moving = True

    def update(self):
        if self.moving:
            self.rect.x -= SPEED
        if self.rect.x < (0-self.rect.width):
            self.rect.x = WIDTH
            self.rect.y = random.randint(0 + self.rect.height, HEIGHT - self.rect.height)
