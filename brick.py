import pygame
from pygame.sprite import  Sprite

class Brick(Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = "Black"
        self.width = self.settings.brick_width
        self.height = self.settings.brick_height
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.topleft = (x,y)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)