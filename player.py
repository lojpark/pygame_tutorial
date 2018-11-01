class Player:
    def __init__(self, pygame):
        # 플레이어 초기화
        self.image = pygame.image.load('image\\player.png')
        self.x = 320;
        self.y = 300;
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.alive = True

    def move(self, key):
        # 플레이어 이동
        if key.up:
            self.y -= 5
        if key.down:
            self.y += 5
        if key.left:
            self.x -= 5
        if key.right:
            self.x += 5

    def crash(self, enemy):
        # 플레이어와 적이 충돌
        return

    def print(self, screen):
        # 플레이어 그리기
        screen.blit(self.image, (self.x - self.width / 2, self.y - self.height / 2))
