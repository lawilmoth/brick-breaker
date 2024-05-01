class Settings:
    def __init__(self):
        self.bg_color = (100,100,100)
        self.screen_width = 1000
        self.screen_height = 600

        #Brick Settings
        self.brick_height = 30
        self.brick_width = self.screen_width//20 

        #Paddle Settings
        self.paddle_width = 200
        self.paddle_height = 30