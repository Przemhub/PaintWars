import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 9
        self.jumped = False
        self.looks_left = False
        self.looks_right = True
        self.stand_right = pygame.image.load("resources/character/player_stand.png")
        self.stand_left = pygame.transform.flip(self.stand_right, True, False)
        self.running_right = [
            pygame.image.load("resources/character/player_run1.png"),
            pygame.image.load("resources/character/player_run2.png"),
            pygame.image.load("resources/character/player_run3.png"),
            pygame.image.load("resources/character/player_run4.png"),
            pygame.image.load("resources/character/player_run5.png"),
            pygame.image.load("resources/character/player_run6.png")
        ]
        self.running_left = [pygame.transform.flip(image, True, False) for image in self.running_right]
        self.jumping_right = [
            pygame.image.load("resources/character/player_jump1.png"),
            pygame.image.load("resources/character/player_jump2.png"),
            pygame.image.load("resources/character/player_jump3.png"),
            pygame.image.load("resources/character/player_jump4.png"),
        ]
        self.jumping_left = [pygame.transform.flip(image, True, False) for image in self.jumping_right]
        self.image = self.stand_right
        self.run_frame = 0
        self.jump_frame = 0
        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())

    def move(self, x, y):
        self.rect = self.rect.move(x * self.speed, y * self.speed)

    def run_right(self):
        self.looks_left = False
        self.looks_right = True
        self.image = self.running_right[self.run_frame]
        print("image run")
        self.run_frame += 1
        if self.run_frame > 5:
            self.run_frame = 0

    def run_left(self):
        self.looks_left = True
        self.looks_right = False
        self.image = self.running_left[self.run_frame]
        print("image run")
        self.run_frame += 1
        if self.run_frame > 5:
            self.run_frame = 0

    def jump_right(self):
        self.looks_right = True
        self.looks_left = False
        self.image = self.jumping_right[self.jump_frame]
        print("image jump")
        self.jump_frame += 1
        if self.jump_frame > 3:
            self.jump_frame = 0
