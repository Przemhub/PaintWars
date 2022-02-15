import pygame


class MapObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image, collision_image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.speed = 7
        self.collision_image = collision_image
        self.mask = pygame.mask.from_threshold(self.collision_image, (0, 0, 0, 255), (255, 255, 255, 255))
        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())


    def move(self, x, y):
        self.rect = self.rect.move(x * self.speed, y * self.speed)
