import pygame
import random

# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 패들 설정
paddle_width = 400
paddle_height = 10
paddle_speed = 5
paddle = pygame.Rect(screen_width // 2 - paddle_width // 2, screen_height - 30, paddle_width, paddle_height)

# 공 설정
ball_size = 10
ball_speed_x = 3
ball_speed_y = 3
ball = pygame.Rect(screen_width // 2 - ball_size // 2, screen_height // 2 - ball_size // 2, ball_size, ball_size)

# 블록 설정
block_width = 60
block_height = 20
blocks = []
for i in range(6):
    for j in range(5):
        block = pygame.Rect(i * (block_width + 10) + 35, j * (block_height + 10) + 35, block_width, block_height)
        blocks.append(block)

# 점수 설정
score = 0
font = pygame.font.Font(None, 36)

# 게임 루프
running = True
while running:
    screen.fill(BLACK)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 패들 움직임
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < screen_width:
        paddle.x += paddle_speed

    # 공 움직임
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # 공이 화면 경계를 벗어나면 반대 방향으로 튕김
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x = -ball_speed_x
    if ball.top <= 0:
        ball_speed_y = -ball_speed_y

    # 공이 바닥에 닿으면 게임 오버
    if ball.bottom >= screen_height:
        running = False

    # 패들과 충돌하면 공 튕김
    if ball.colliderect(paddle):
        ball_speed_y = -ball_speed_y

    # 블록과 충돌하면 공 튕기고 블록 제거
    for block in blocks[:]:
        if ball.colliderect(block):
            blocks.remove(block)
            ball_speed_y = -ball_speed_y
            score += 10

    # 게임 종료 조건 (모든 블록 제거)
    if not blocks:
        running = False

    # 화면에 그리기
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.ellipse(screen, RED, ball)
    for block in blocks:
        pygame.draw.rect(screen, GREEN, block)

    # 점수 표시
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # 화면 업데이트
    pygame.display.flip()

    # FPS 설정
    pygame.time.Clock().tick(60)

# 게임 종료 후 pygame 종료
pygame.quit()
