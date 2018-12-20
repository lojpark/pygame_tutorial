import math

class Bullet:
    def __init__(self, pygame, x, y, angle, speed, who):
        # 총알 초기화
        if who == 'player':
            self.image = pygame.image.load('image\\bulletA.png')
        else:
            self.image = pygame.image.load('image\\bulletB.png')
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.x, self.y, self.angle, self.speed, self.who = x, y, angle, speed, who
        self.ox, self.oy = self.x, self.y
        self.r = 0
        
    def move(self):
        # 총알 이동
        self.x = self.ox + math.cos(self.angle * math.pi / 180) * self.r
        self.y = self.oy + math.sin(self.angle * math.pi / 180) * self.r
        self.r += self.speed

    def print(self, screen):
        # 총알 그리기
        screen.blit(self.image, (self.x - self.width / 2, self.y - self.height / 2))

class Bullets:
    def __init__(self, pygame):
        self.pygame = pygame
        self.bullets = []

    def append(self, x, y, angle, speed, who):
        self.bullets.append(Bullet(self.pygame, x, y, angle, speed, who))

    def move(self):
        # 총알 이동
        for i in reversed(range(0, len(self.bullets))):
            self.bullets[i].move()
            if self.bullets[i].y < -20 or self.bullets[i].y > 620:
                del self.bullets[i]

    def print(self, screen):
        # 총알 그리기
        for bullet in self.bullets:
            bullet.print(screen)
