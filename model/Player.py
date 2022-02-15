import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 7
        self.jumped = False
        self.image = pygame.image.load("resources/character/player_run1.png")
        self.running = [
            pygame.image.load("resources/character/player_run1.png"),
            pygame.image.load("resources/character/player_run2.png"),
            pygame.image.load("resources/character/player_run3.png")
        ]
        self.run_frame = 0
        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())


    def move(self, x, y):
        self.rect = self.rect.move(x * self.speed, y * self.speed)

    def run(self):
        self.image = self.running[self.run_frame]
        self.run_frame += 1

