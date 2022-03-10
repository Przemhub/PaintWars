class PlayerService:
    def __init__(self, player, collision_service):
        self.player = player
        self.collision_service = collision_service
        self.jump_iter = 0
        self.jump_height = 2
        self.JUMPS = 7
        self.NEXT_MOVE = 3
        self.frames = 0

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
            self.player.jump_right()
            self.frames = 0

    def idle(self):
        if self.player.looks_right:
            self.player.image = self.player.stand_right
        elif self.player.looks_left:
            self.player.image = self.player.stand_left
        print("image idle")

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
