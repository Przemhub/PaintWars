import pygame

from model.MapObject import MapObject


class CollisionService:
    def __init__(self, map_repository):
        self.map_repository = map_repository

    def object_collided(self, sprite1, sprite2):
        if pygame.sprite.spritecollide(sprite1, sprite2, False):
            return True
        return False

    def collides_with_map(self, sprite):
        if pygame.sprite.spritecollide(sprite, self.map_repository.map, False):
            return True
        return False

    def collides_with_floor(self, sprite):
        if pygame.sprite.spritecollide(sprite, self.map_repository.floor, False):
            return True
        return False
