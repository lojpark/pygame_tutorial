import random
import math

class Enemy:
    def __init__(self, pygame, x, y, etype):
        # 적 초기화
        if etype == 'typeA':
            self.image = pygame.image.load('image\\enemyA.png')
            self.hp = 3
            self.fire_delay = 50
            
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.x = x
        self.y = y
        self.type = etype
        self.time = 0

    def move(self, bullet, player):
        # 적 이동
        self.y += 3
        self.time += 1
        if self.time >= self.fire_delay and self.y < player.y:
            self.time = 0
            
            if self.type == 'typeA':
                bullet.append(self.x, self.y, 90, 10, 'enemy')
                
    def print(self, screen):
        # 적 그리기
        screen.blit(self.image, (self.x - self.width / 2, self.y - self.height / 2))

class Enemies:
    def __init__(self, pygame):
        # 적 초기화
        self.pygame = pygame
        self.enemies = []

    def append(self):
        # 적 추가
        if random.randint(1, 100) <= 1:
            x, y = random.randint(0, 800), -50
            self.enemies.append(Enemy(self.pygame, x, y, 'typeA'))

    def move(self, bullet, player):
        # 적 이동
        for enemy in self.enemies:
            enemy.move(bullet, player)

    def crash(self, bullet):
        # 적과 총알이 충돌
        for i in reversed(range(len(self.enemies))):
            up = self.enemies[i].y - self.enemies[i].height / 2
            down = self.enemies[i].y + self.enemies[i].height / 2
            left = self.enemies[i].x - self.enemies[i].width / 2
            right = self.enemies[i].x + self.enemies[i].width / 2
            for j in reversed(range(len(bullet.bullets))):
                if bullet.bullets[j].who == 'player':
                    x = bullet.bullets[j].x
                    y = bullet.bullets[j].y
                    if up <= y and y <= down:
                        if left <= x and x <= right:
                            self.enemies[i].hp -= 1
                            del bullet.bullets[j]
                            if self.enemies[i].hp <= 0:
                                del self.enemies[i]
                                break

    def print(self, screen):
        # 적 그리기
        for enemy in self.enemies:
            enemy.print(screen)
