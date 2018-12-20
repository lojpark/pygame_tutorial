class Key:
    def __init__(self):
        # 키 초기화
        self.left = False
        self.right = False
        self.up = False
        self.down = False

    def set_down(self, pygame, key, player, bullet):
        # 키보드 버튼을 눌렀을 때
        if key == pygame.K_UP:
            self.up = True
        if key == pygame.K_DOWN:
            self.down = True
        if key == pygame.K_LEFT:
            self.left = True
        if key == pygame.K_RIGHT:
            self.right = True
        if key == pygame.K_SPACE:
            player.loaded = 3

    def set_up(self, pygame, key):
        # 키보드 버튼을 눌렀을 때
        if key == pygame.K_UP:
            self.up = False
        if key == pygame.K_DOWN:
            self.down = False
        if key == pygame.K_LEFT:
            self.left = False
        if key == pygame.K_RIGHT:
            self.right = False
