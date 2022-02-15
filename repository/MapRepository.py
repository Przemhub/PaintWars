import pygame

from model.MapObject import MapObject


class MapRepository:
    def __init__(self,screen):
        self.screen = screen
        self.floor = pygame.sprite.Group(
            MapObject(0, self.screen.get_height() - self.screen.get_height() / 4,
                      pygame.image.load("resources/map/floor.png"),
                      pygame.image.load("resources/collision/floor.jpg")))
        self.map = pygame.sprite.Group(self.floor)