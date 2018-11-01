import pygame
from player import *
from bullet import *
from enemy import *
from key import *

# 게임 화면 초기화
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Space')
fps = pygame.time.Clock()

# 플레이어 초기화
player = Player(pygame)

# 총알 초기화
bullet = Bullet(pygame)

# 키 초기화
key = Key()

is_playing = True
is_alive = True
while is_playing:
    # 입력 이벤트 처리
    for event in pygame.event.get():
        # 종료 버튼을 눌렀을 때
        if event.type == pygame.QUIT:
            is_playing = False

        # 키보드 버튼을 눌렀을 때
        if event.type == pygame.KEYDOWN:
            key.set_down(pygame, event.key, player, bullet)

        # 키보드 버튼을 뗐을 때
        if event.type == pygame.KEYUP:
            key.set_up(pygame, event.key)

    # 플레이어 이동
    player.move(key)
    # 총알 이동
    bullet.move()

    # 화면 지우기
    screen.fill((0, 0, 0))

    # 총알 그리기
    bullet.print(screen)
    # 플레이어 그리기
    player.print(screen)

    # 화면 업데이트
    pygame.display.update()

    # 초당 프레임 수 설정
    fps.tick(60)

pygame.quit()
