import pygame
import sys
import random

pygame.init()

clock = pygame.time.Clock()

running = True
menu_active = True
game_over = False
game_active = False

user_score = 0
ai_score = 0

large_font = pygame.font.Font('font.otf', 42)
small_font = pygame.font.Font('font.otf', 32)

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 450

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("pong-app")

class Player:
    def __init__(self):
        self.paddle_rect = pygame.Rect(50, 200, 10, 100)
        self.paddle_speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w] and game_active:
            self.paddle_rect.y -= self.paddle_speed
    
        if keys[pygame.K_s] and game_active:
            self.paddle_rect.y += self.paddle_speed
        
        if self.paddle_rect.y < 0:
            self.paddle_rect.y = 0

        if self.paddle_rect.y > 350:
            self.paddle_rect.y = 350

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 100, 255), self.paddle_rect)

class Ball:
    def __init__(self, x, y, radius, speed_x, speed_y):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def bounce(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        if self.y - self.radius <= 0 or self.y + self.radius >= SCREEN_HEIGHT:
            self.speed_y *= -1
        if self.x - self.radius <= 0 or self.y + self.radius >= SCREEN_WIDTH:
            self.speed_x *= -1

    def check_out_bounds(self, SCREEN_WIDTH):
        return self.x - self.radius <= 0 or self.x + self.radius >= SCREEN_WIDTH

    def reset(self, SCREEN_WIDTH, SCREEN_HEIGHT ):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.speed_x = random.choice([-5, 5])
        self.speed_y = random.choice([-5, 5])

    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

    def check_collisions(self, player):
        global user_score, ai_score
        ball_rect = self.get_rect()
        if ball_rect.colliderect(player.paddle_rect):
            self.speed_x *= -1

        if ball_rect.x <= 0:
            ai_score +=1

        if ball_rect.x >= 450:
            player_score +=1

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 100, 255), (self.x, self.y), self.radius)

class AI:
    def __init__(self)
        self.ai_rect = pygame.Rect(50, 200, 10, 100)
        self.ai_speed = 5

    def update(self, ball):
        
        if self.paddle_rect.y < 0:
            self.paddle_rect.y = 0

        if self.paddle_rect.y > 350:
            self.paddle_rect.y = 350

        if ball.get

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 100, 255), self.paddle_rect)

player = Player()
ai = AI()
ball = Ball(400, 225, 10, 5, 5)

def game():
    player.draw(screen)
    player.update()
    ball.move()
    ball.check_collisions(player)
    ball.bounce(WINDOW_WIDTH, WINDOW_HEIGHT)
    if ball.check_out_bounds(WINDOW_WIDTH):
        ball.reset(WINDOW_WIDTH, WINDOW_HEIGHT)
    ball.draw(screen)

def menu():
    screen.fill((0, 0, 0))
    line_one = large_font.render("Pong", True, (255, 100, 255))
    line_two = small_font.render("ENTER to begin", True, (255, 100, 255))
    screen.blit(line_one, ((WINDOW_WIDTH - line_one.get_width()) // 2, ((WINDOW_HEIGHT - line_one.get_height()) // 2)))
    screen.blit(line_two, ((WINDOW_WIDTH - line_two.get_width()) // 2, ((WINDOW_HEIGHT - line_two.get_height()) // 2 + 50)))

def game_over_screen():
    screen.fill((0, 0, 0))
    line_one_B = large_font.render("WON OR LOST", True, (255, 100, 255))
    line_two_B = small_font.render("ENTER to retry", True, (255, 100, 255))
    screen.blit(line_one_B, ((WINDOW_WIDTH - line_one_B.get_width()) // 2, ((WINDOW_HEIGHT - line_one_B.get_height()) // 2)))
    screen.blit(line_two_B, ((WINDOW_WIDTH - line_two_B.get_width()) // 2, ((WINDOW_HEIGHT - line_two_B.get_height()) // 2 + 50)))

while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        if event.type == pygame.KEYDOWN and menu_active:
            if event.key == pygame.K_RETURN:
                menu_active = False
                game_active = True

        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                game_over = False
                game_active = True
    
    if menu_active:
        menu()

    if game_over:
        game_over()

    if game_active:
        game()

    clock.tick(60)
    pygame.display.update()

pygame.quit()        