import pygame.font
HEIGHT = 500
WIDTH = 800
pygame.font.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
class Startbutton:
    def __init__(self, text):
        self.screen = screen
        self.width = 250
        self.height = 100
        self.button_color = (176, 110, 35)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font(None, 50)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (400, 250)
        self._display_text(text)

    def _display_text(self, text):
        self.text_image = self.font.render(text, True, self.text_color, self.button_color)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.text_image, self.text_image_rect)