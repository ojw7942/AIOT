import pygame
import sys
import random

# 초기화
pygame.init()

# 게임 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
GRAY = (128, 128, 128)

class Paddle:
    def __init__(self, x, y):
        self.width = 100
        self.height = 10
        self.x = x
        self.y = y
        self.speed = 8
        
    def move_left(self):
        if self.x > 0:
            self.x -= self.speed
    
    def move_right(self):
        if self.x < SCREEN_WIDTH - self.width:
            self.x += self.speed
    
    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class Ball:
    def __init__(self, x, y):
        self.radius = 8
        self.x = x
        self.y = y
        self.speed_x = random.choice([-4, 4])
        self.speed_y = -4
        
    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
    
    def bounce_x(self):
        self.speed_x = -self.speed_x
    
    def bounce_y(self):
        self.speed_y = -self.speed_y
    
    def draw(self, screen):
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), self.radius)
    
    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, 
                          self.radius * 2, self.radius * 2)

class Brick:
    def __init__(self, x, y, color):
        self.width = 75
        self.height = 20
        self.x = x
        self.y = y
        self.color = color
        self.destroyed = False
    
    def draw(self, screen):
        if not self.destroyed:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
            pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height), 2)
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("벽돌깨기 게임")
        self.clock = pygame.time.Clock()
        
        # 게임 객체 초기화
        self.paddle = Paddle(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 30)
        self.ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.bricks = []
        self.create_bricks()
        
        # 게임 상태
        self.score = 0
        self.lives = 3
        self.font = pygame.font.Font(None, 36)
        self.game_over = False
        self.game_won = False
        
    def create_bricks(self):
        colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
        brick_rows = 6
        brick_cols = 10
        
        for row in range(brick_rows):
            for col in range(brick_cols):
                x = col * 80 + 10
                y = row * 25 + 50
                color = colors[row % len(colors)]
                brick = Brick(x, y, color)
                self.bricks.append(brick)
    
    def handle_collisions(self):
        # 벽과의 충돌
        if self.ball.x <= self.ball.radius or self.ball.x >= SCREEN_WIDTH - self.ball.radius:
            self.ball.bounce_x()
        
        if self.ball.y <= self.ball.radius:
            self.ball.bounce_y()
        
        # 바닥에 떨어짐
        if self.ball.y >= SCREEN_HEIGHT:
            self.lives -= 1
            if self.lives <= 0:
                self.game_over = True
            else:
                self.reset_ball()
        
        # 패들과의 충돌
        ball_rect = self.ball.get_rect()
        paddle_rect = self.paddle.get_rect()
        
        if ball_rect.colliderect(paddle_rect):
            # 패들의 어느 부분에 맞았는지에 따라 각도 조정
            hit_pos = (self.ball.x - self.paddle.x) / self.paddle.width
            self.ball.speed_x = (hit_pos - 0.5) * 10
            self.ball.bounce_y()
        
        # 벽돌과의 충돌
        for brick in self.bricks:
            if not brick.destroyed:
                brick_rect = brick.get_rect()
                if ball_rect.colliderect(brick_rect):
                    brick.destroyed = True
                    self.score += 10
                    self.ball.bounce_y()
                    
                    # 모든 벽돌을 깼는지 확인
                    if all(brick.destroyed for brick in self.bricks):
                        self.game_won = True
                    break
    
    def reset_ball(self):
        self.ball.x = SCREEN_WIDTH // 2
        self.ball.y = SCREEN_HEIGHT // 2
        self.ball.speed_x = random.choice([-4, 4])
        self.ball.speed_y = -4
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and (self.game_over or self.game_won):
                    self.restart_game()
        return True
    
    def restart_game(self):
        self.paddle = Paddle(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 30)
        self.ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.bricks = []
        self.create_bricks()
        self.score = 0
        self.lives = 3
        self.game_over = False
        self.game_won = False
    
    def update(self):
        if not self.game_over and not self.game_won:
            # 키 입력 처리
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.paddle.move_left()
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.paddle.move_right()
            
            # 공 이동
            self.ball.move()
            
            # 충돌 처리
            self.handle_collisions()
    
    def draw(self):
        self.screen.fill(WHITE)
        
        # 게임 객체 그리기
        self.paddle.draw(self.screen)
        self.ball.draw(self.screen)
        
        for brick in self.bricks:
            brick.draw(self.screen)
        
        # UI 그리기
        score_text = self.font.render(f"점수: {self.score}", True, BLACK)
        self.screen.blit(score_text, (10, 10))
        
        lives_text = self.font.render(f"생명: {self.lives}", True, BLACK)
        self.screen.blit(lives_text, (10, 50))
        
        # 게임 오버 또는 승리 메시지
        if self.game_over:
            game_over_text = self.font.render("게임 오버! R키를 눌러 재시작", True, RED)
            text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
            self.screen.blit(game_over_text, text_rect)
        
        elif self.game_won:
            win_text = self.font.render("축하합니다! 승리했습니다! R키를 눌러 재시작", True, GREEN)
            text_rect = win_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
            self.screen.blit(win_text, text_rect)
        
        # 조작법 안내
        if not self.game_over and not self.game_won:
            control_text = pygame.font.Font(None, 24).render("←→ 또는 A,D키로 패들 조작", True, GRAY)
            self.screen.blit(control_text, (10, SCREEN_HEIGHT - 30))
        
        pygame.display.flip()
    
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

# 게임 실행
if __name__ == "__main__":
    game = Game()
    game.run()
    
