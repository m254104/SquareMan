import pygame
SPEED = 3
WIDTH = 1000
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load('assets/bigbadwall.png')
        self.image = pygame.transform.scale(self.image, (25, 200))
        self.rect = self.image.get_rect()
        self.rect.midbottom = position
        self.moving = True

    def update(self):
        if self.moving:
            self.rect.x -= SPEED
        if self.rect.x < (0-self.rect.width):
            self.rect.x = WIDTH

