import pygame
from pygame.sprite import Sprite


class Ball(Sprite):
    def __init__(self, game):
        super().__init__()
        self.settings = game.settings
        self.screen = game.screen
        self.paddle = game.paddle
        self.radius = self.settings.ball_radius
        self.color = self.settings.ball_color
        self.pos = (self.paddle.rect.midtop)
        self.pos = (self.pos[0], self.pos[1] - self.radius)
        
        
        self.x_speed = 0
        self.y_speed = -1

    
    def draw(self):
        self.circle = pygame.draw.circle(
            self.screen, 
            self.color, 
            self.pos,
            self.radius)
        
    def update(self):
        """updates the position of the ball"""
        #self.pos = (x, y) so we add the x_speed and y_speed
        self.pos = (self.pos[0] + self.x_speed, self.pos[1] + self.y_speed)