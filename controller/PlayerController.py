import pygame

from model.Player import Player
from service.PlayerService import PlayerService


class PlayerController:
    def __init__(self, collision_service):
        self.player = Player(100, 100)
        self.collision_service = collision_service
        self.player_service = PlayerService(self.player, collision_service)

    def move_event(self):
        if pygame.key.get_pressed()[pygame.K_d]:
            self.player_service.runs_right()
        elif pygame.key.get_pressed()[pygame.K_a]:
            self.player_service.runs_left()
        elif not self.player.jumped:
            self.player_service.idle()
        if pygame.key.get_pressed()[pygame.K_w] and self.player_service.can_jump():
            self.player_service.jumps_anim()
            self.player.jumped = True

        if not self.collision_service.collides_with_floor(self.player):
            self.player.move(0, 1)
