import pygame
from pygame.sprite import  Sprite

class Paddle(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.color = (50, 0, 50)
        self.width = self.settings.paddle_width
        self.height = self.settings.paddle_height
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= 10

        self.moving_right = False

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        if self.moving_right:
            self.rect.x += 1