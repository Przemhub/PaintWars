from math import fabs

from model.Bullet import Bullet


class PlayerService:
    def __init__(self, player, collision_service):
        self.player = player
        self.collision_service = collision_service
        self.jump_iter = 0
        self.jump_height = 1
        self.JUMPS = 8
        self.NEXT_MOVE = 3
        self.frames = 0
        self.bullets_shot = []
        self.SHOT_RANGE = 350

    def jumping_player_event(self):
        if self.player.jumped:
            self.jumps_anim()
            if self.jump_iter < self.JUMPS:
                self.player.move(0, -self.jump_height)
                self.jump_height -= 0.1
                self.jump_iter += 1
            else:
                self.jump_iter = 0
                self.jump_height = 3
                self.player.jumped = False

    def jumps_anim(self):
        self.frames += 1
        if self.frames == self.NEXT_MOVE:
            if self.player.looks_right:
                self.player.jump_right()
                self.frames = 0
            else:
                self.player.jump_left()
                self.frames = 0

    def idle(self):
        if self.player.looks_right:
            self.player.image = self.player.stand_right
        elif self.player.looks_left:
            self.player.image = self.player.stand_left
        # print("image idle")

    def runs_right(self):
        self.frames += 1
        if self.frames == self.NEXT_MOVE:
            self.player.move(1, 0)
            if not self.player.jumped:
                self.player.run_right()
            self.frames = 0

    def runs_left(self):
        self.frames += 1
        if self.frames == self.NEXT_MOVE:
            self.player.move(-1, 0)
            if not self.player.jumped:
                self.player.run_left()
            self.frames = 0

    def can_jump(self):
        if not self.player.jumped and self.collision_service.collides_with_floor(self.player):
            return True
        return False

    def bullets_event(self):
        bullets_to_delete = []
        for bullet in self.bullets_shot:
            if bullet.shoot_right:
                bullet.rect = bullet.rect.move(20, 0)
            else:
                bullet.rect = bullet.rect.move(-20, 0)
            if fabs(bullet.rect.x - self.player.rect.x) > self.SHOT_RANGE:
                bullets_to_delete.append(bullet)
        for bullet_delete in bullets_to_delete:
            self.bullets_shot.remove(bullet_delete)

    def shoots(self):
        self.frames += 1
        if self.frames == self.NEXT_MOVE:
            bullet = Bullet(self.player.rect.x, self.player.rect.y + 20)
            if self.player.looks_right:
                self.player.shoot_right()
                bullet.shoot_right = True
                bullet.rect = bullet.rect.move(50, 0)
            else:
                self.player.shoot_left()
            if not self.player.shot:
                self.bullets_shot.append(bullet)
            self.frames = 0
