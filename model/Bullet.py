import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 10, 10)
        self.image = pygame.image.load("resources/props/bullet.png")
        self.shoot_right = False
