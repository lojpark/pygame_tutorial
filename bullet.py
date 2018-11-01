class Bullet:
    def __init__(self, pygame):
        # 총알 초기화
        self.image = pygame.image.load('image\\bullet.png')
        self.bullets = []

    def append(self, x, y):
        self.bullets.append([x, y])

    def move(self):
        # 총알 이동
        for i in reversed(range(0, len(self.bullets))):
            self.bullets[i][1] -= 10
            if self.bullets[i][1] < 0:
                del self.bullets[i]

    def print(self, screen):
        # 총알 그리기
        for bullet in self.bullets:
            screen.blit(self.image, (bullet[0] - 8, bullet[1] - 8))
