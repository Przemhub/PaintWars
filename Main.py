import sys

import pygame

from controller.PlayerController import PlayerController
from repository.MapRepository import MapRepository
from service.CollisionService import CollisionService


class Game():
    def __init__(self):
        pygame.init()
        self.init_screen()
        self.init_repositories()
        self.init_services()
        self.init_controllers()
        self.main_loop()

    def init_services(self):
        self.collision_service = CollisionService(self.map_repository)

    def init_repositories(self):
        self.map_repository = MapRepository(self.screen)

    def init_controllers(self):
        self.player_controller = PlayerController(self.collision_service)

    def init_screen(self):
        pygame.display.init()
        self.res_list = [
            (1600, 900),
            (1440, 900),
            (1360, 768),
            (1280, 720),
            (800, 600)
        ]
        self.res_option = 4
        self.full_screen = False
        self.current_res = self.res_list[self.res_option]
        self.screen = pygame.display.set_mode(self.current_res)
        self.clock = pygame.time.Clock()

    def draw(self):
        self.screen.blit(self.player_controller.player.image, self.player_controller.player.rect)
        self.map_repository.floor.draw(self.screen)
        for bullet in self.player_controller.player_service.bullets_shot:
            self.screen.blit(bullet.image, bullet.rect)

    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
            self.screen.fill((155, 232, 255))
            self.player_controller.move_event()
            self.player_controller.player_service.jumping_player_event()
            self.player_controller.shoot_event()
            self.player_controller.player_service.bullets_event()
            self.draw()
            self.clock.tick(45)
            pygame.display.flip()


if __name__ == "__main__":
    Game()
