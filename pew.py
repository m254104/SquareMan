import pygame
import random
SPEED = 4
WIDTH = 800
HEIGHT = 500

class Pellet(pygame.sprite.Sprite):
    """A little powerup icon that runs across the screen"""
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load('assets/powerup.png')
        self.image = pygame.transform.scale(self.image, (15, 15))
        self.rect = self.image.get_rect()
        self.moving = True

    def update(self):
        if self.moving:
            self.rect.x -= SPEED
        if self.rect.x < (0-self.rect.width):
            self.rect.x = WIDTH + 800
            self.rect.y = random.randint(0 + self.rect.height, HEIGHT - self.rect.height)

