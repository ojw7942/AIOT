import pygame

# 1. 초기화
pygame.init()

# 화면 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("파이썬 벽돌깨기")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# 2. 라켓 설정
paddle_width = 100
paddle_height = 20
paddle_x = (SCREEN_WIDTH - paddle_width) // 2
paddle_y = SCREEN_HEIGHT - 40
paddle_speed = 7
paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)

# 3. 공 설정
ball_radius = 10
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
ball_dx = 5  # x 방향 속도
ball_dy = -5 # y 방향 속도 (위로 시작)

# 4. 벽돌 설정
brick_rows = 5
brick_cols = 8
brick_width = 80
brick_height = 25
brick_padding = 5
bricks = []

for row in range(brick_rows):
    for col in range(brick_cols):
        brick_x = col * (brick_width + brick_padding) + 60 # 시작 위치 조정
        brick_y = row * (brick_height + brick_padding) + 50
        bricks.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))

# 게임 변수
score = 0
lives = 3
game_over = False
game_clear = False

# 폰트 설정
font = pygame.font.Font(None, 36)

# 게임 루프
running = True
clock = pygame.time.Clock() # 프레임 속도 제어

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle_rect.x -= paddle_speed
            if event.key == pygame.K_RIGHT:
                paddle_rect.x += paddle_speed
            # 게임 오버/클리어 후 재시작 키 (선택 사항)
            if (game_over or game_clear) and event.key == pygame.K_SPACE:
                # 게임 상태 초기화 로직
                pass

    # 라켓 경계 처리
    if paddle_rect.left < 0:
        paddle_rect.left = 0
    if paddle_rect.right > SCREEN_WIDTH:
        paddle_rect.right = SCREEN_WIDTH

    # 공 이동
    if not (game_over or game_clear):
        ball_x += ball_dx
        ball_y += ball_dy

    # 공 벽 충돌
    if ball_x <= ball_radius or ball_x >= SCREEN_WIDTH - ball_radius:
        ball_dx *= -1
    if ball_y <= ball_radius: # 상단 벽
        ball_dy *= -1
    
    # 공 바닥 충돌 (생명 감소 또는 게임 오버)
    if ball_y >= SCREEN_HEIGHT - ball_radius:
        lives -= 1
        if lives == 0:
            game_over = True
        else: # 공 위치 초기화
            ball_x = SCREEN_WIDTH // 2
            ball_y = SCREEN_HEIGHT // 2
            ball_dx = 5
            ball_dy = -5

    # 공 라켓 충돌
    ball_rect = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)
    if ball_rect.colliderect(paddle_rect) and ball_dy > 0: # 공이 아래로 내려올 때만 충돌 검사
        ball_dy *= -1
        # 라켓에 맞은 위치에 따라 공 튕기는 각도 조절 (선택 사항)
        # diff = (ball_x - (paddle_rect.x + paddle_width / 2))
        # ball_dx = diff * 0.1 # 적절한 계수 적용

    # 공 벽돌 충돌
    bricks_to_remove = []
    for brick in bricks:
        if ball_rect.colliderect(brick):
            ball_dy *= -1 # 공 튕김
            bricks_to_remove.append(brick)
            score += 10 # 점수 증가
            break # 한 번에 하나의 벽돌만 깨지도록

    for brick in bricks_to_remove:
        bricks.remove(brick)

    if not bricks and not game_over: # 모든 벽돌을 깼을 때
        game_clear = True

    # 화면 그리기
    screen.fill(BLACK) # 배경 채우기

    pygame.draw.rect(screen, BLUE, paddle_rect) # 라켓 그리기
    pygame.draw.circle(screen, WHITE, (int(ball_x), int(ball_y)), ball_radius) # 공 그리기

    for brick in bricks: # 벽돌 그리기
        pygame.draw.rect(screen, GREEN, brick)

    # 점수 및 생명 표시
    score_text = font.render(f"Score: {score}", True, WHITE)
    lives_text = font.render(f"Lives: {lives}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (SCREEN_WIDTH - lives_text.get_width() - 10, 10))

    # 게임 오버 / 게임 클리어 메시지
    if game_over:
        game_over_text = font.render("GAME OVER! Press SPACE to Restart", True, RED)
        text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(game_over_text, text_rect)
    
    if game_clear:
        game_clear_text = font.render("YOU WIN! Press SPACE to Play Again", True, GREEN)
        text_rect = game_clear_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(game_clear_text, text_rect)

    pygame.display.flip() # 화면 업데이트
    clock.tick(60) # 60 FPS 유지

pygame.quit()
input()
