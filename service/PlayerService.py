class PlayerService:
    def __init__(self, player, collision_service):
        self.player = player
        self.collision_service = collision_service
        self.jump_iter = 0
        self.jump_height = 3
        self.jumps = 8

    def jumping_player_event(self):
        if self.player.jumped:
            if self.jump_iter < self.jumps:
                self.player.move(0, -self.jump_height)
                self.jump_height -= 0.1
                self.jump_iter += 1
            else:
                self.jump_iter = 0
                self.jump_height = 3
                self.player.jumped = False

    def can_jump(self):
        if not self.player.jumped and self.collision_service.collides_with_floor(self.player):
            return True
        return False
