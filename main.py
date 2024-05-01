import pygame
from settings import Settings
from brick import Brick
from paddle import Paddle

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
        self.bricks = pygame.sprite.Group()
        self.running  = True
        self._create_level()

    def _create_level(self):
        self.brick = Brick(self, 800, 100)
        

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            ####Draw Screen
            self.screen.fill(self.settings.bg_color)
            self.brick.draw()
            self.paddle.draw()
            pygame.display.flip()

game = Game()
game.run()
