import pygame
from settings import Settings
from brick import Brick
from paddle import Paddle
from ball import Ball

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((
            self.settings.screen_width,
            self.settings.screen_height
            ))
        pygame.display.set_caption("Brick Breaker")
        
        self.paddle = Paddle(self)
        self.ball = Ball(self)
        self.bricks = pygame.sprite.Group()
        self.running  = True
        self._create_level()

    def _create_level(self):
        self.brick = Brick(self, 800, 100)
        

    def run(self):
        """Runs the main loop"""
        while self.running:
            self._check_events()
            self._update_screen()
            self._draw_screen()


    def _check_events(self):
        """Checking for events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                """All keydown events"""
                if event.key == pygame.K_RIGHT:
                    self.paddle.moving_right = True

            if event.type == pygame.KEYUP:
                """All keyup events"""
                if event.key == pygame.K_RIGHT:
                    self.paddle.moving_right = False

    def _update_screen(self):
        """Update"""
        self.paddle.update()
        self.ball.update()

    def _draw_screen(self):
        """Draw Screen"""
        self.screen.fill(self.settings.bg_color)
        self.brick.draw()
        self.paddle.draw()
        self.ball.draw()
        
        pygame.display.flip()

game = Game()
game.run()
