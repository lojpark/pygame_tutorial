class Player:
    def __init__(self, pygame):
        # 플레이어 초기화
        self.image = pygame.image.load('image\\player.png')
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        
        self.x = 400;
        self.y = 500;
        self.alive = True
        
        self.angle = 0
        self.loaded = 0
        self.fire_delay = 5

    def move(self, key, bullet):
        # 플레이어 이동
        if key.up:
            self.y -= 5
        if key.down:
            self.y += 5
        if key.left:
            self.x -= 5
        if key.right:
            self.x += 5
        # 장전된 총 발사
        if self.loaded > 0:
            self.fire_delay -= 1
            if self.fire_delay <= 0:
                bullet.append(self.x - 5, self.y, -110, 10, 'player')
                bullet.append(self.x, self.y, -90, 10, 'player')
                bullet.append(self.x + 5, self.y, -70, 10, 'player')
                self.angle += 20
                self.loaded -= 1
                self.fire_delay = 5

    def crash(self, enemy, bullet):
        # 플레이어와 적이 충돌
        for e in enemy.enemies:
            up = e.y - e.height / 2
            down = e.y + e.height / 2
            left = e.x - e.width / 2
            right = e.x + e.width / 2
            if up <= self.y and self.y <= down:
                if left <= self.x and self.x <= right:
                    self.alive = False
                    break
        # 플레이어와 적 총알이 충돌
        for b in bullet.bullets:
            if b.who == 'enemy':
                up = self.y - self.height / 2
                down = self.y + self.height / 2
                left = self.x - self.width / 2
                right = self.x + self.width / 2
                if up <= b.y and b.y <= down:
                    if left <= b.x and b.x <= right:
                        self.alive = False
                        break

    def print(self, screen):
        # 플레이어 그리기
        screen.blit(self.image, (self.x - self.width / 2, self.y - self.height / 2))
