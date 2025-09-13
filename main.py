import pygame
import sys
import random

pygame.init()

clock = pygame.time.Clock()

running = True
menu_active = True
game_active = False
easy_mode = False
hard_mode = False
user_won = False
ai_won = False

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
        
        if self.paddle_rect.y < 35:
            self.paddle_rect.y = 35

        if self.paddle_rect.y > 350:
            self.paddle_rect.y = 350

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.paddle_rect)

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
        if self.y - self.radius <= 35:
            self.y = 35 + self.radius
            self.speed_y *= -1
        if self.y + self.radius >= SCREEN_HEIGHT - 35:
            self.y = SCREEN_HEIGHT - 35 - self.radius
            self.speed_y *= -1
        if self.x - self.radius <= 0 or self.x + self.radius >= SCREEN_WIDTH:
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

    def check_collisions(self, player, AI):
        global user_score, ai_score
        ball_rect = self.get_rect()
        if ball_rect.colliderect(player.paddle_rect):
            self.speed_x *= -1

        if ball_rect.colliderect(AI.ai_rect):
            self.speed_x *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 100, 255), (self.x, self.y), self.radius)

class AI:
    def __init__(self, y):
        self.ai_rect = pygame.Rect(850, y, 10, 100)
        self.ai_speed = 0

    def update(self, ball):
        if easy_mode:
            self.ai_speed = 4
        if hard_mode:
            self.ai_speed = 4.5

        if self.ai_rect.y < 35:
            self.ai_rect.y = 35

        if self.ai_rect.y > 350:
            self.ai_rect.y = 350

        if ball.y < self.ai_rect.y:
            self.ai_rect.y -= self.ai_speed 
        
        if ball.y > self.ai_rect.y + self.ai_rect.height:
            self.ai_rect.y += self.ai_speed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.ai_rect)

player = Player()
ai = AI(200)
ball = Ball(400, 225, 10, 5, 5)

def ai_won_screen():
    screen.fill((0, 0, 0))
    lost_txt = large_font.render("You LOST", True, (255, 0, 0))
    lost_prompt = small_font.rendr("ENTER 1 - easy mode or 2 - hard mode")
    screen.blit(lost_txt, ((WINDOW_WIDTH - lost_txt.get_width()) // 2, ((WINDOW_HEIGHT - lost_txt.get_height()) // 2)))
    screen.blit(lost_prompt, ((WINDOW_WIDTH - lost_prompt.get_width()) // 2, ((WINDOW_HEIGHT - lost_prompt.get_height()) // 2)))
def game():
    global user_score, ai_score
    player.draw(screen)
    player.update()
    ball.move()
    ball.check_collisions(player, ai)
    ball.bounce(WINDOW_WIDTH, WINDOW_HEIGHT)

    if ball.x - ball.radius <= 0:
        ai_score += 1
        ball.reset(WINDOW_WIDTH, WINDOW_HEIGHT)
    elif ball.x + ball.radius >= WINDOW_WIDTH:
        user_score += 1
        ball.reset(WINDOW_WIDTH, WINDOW_HEIGHT)

    ball.draw(screen)
    ai.update(ball)
    ai.draw(screen)

    user_score_txt = small_font.render(f"{user_score}PTS", True, (0, 255, 0))
    ai_score_txt = small_font.render(f"{ai_score}PTS", True, (255, 0, 0))
    screen.blit(user_score_txt, (10, 10))
    screen.blit(ai_score_txt, ((WINDOW_WIDTH -ai_score_txt.get_width() - 10 ), 10)) 

    if user_score = 10 and ai_score < 10:
        user_won = True
        user_won_screen()
    if ai_score = 10 and user_score < 10:
        ai_won = True
        ai_won_screen()

def menu():
    screen.fill((0, 0, 0))
    line_one = large_font.render("Pong", True, (255, 100, 255))
    line_two = small_font.render("ENTER 1 - easy mode or 2 - hard mode", True, (255, 100, 255))
    screen.blit(line_one, ((WINDOW_WIDTH - line_one.get_width()) // 2, ((WINDOW_HEIGHT - line_one.get_height()) // 2)))
    screen.blit(line_two, ((WINDOW_WIDTH - line_two.get_width()) // 2, ((WINDOW_HEIGHT - line_two.get_height()) // 2 + 50)))


while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        if event.type == pygame.KEYDOWN and menu_active:
            if event.key == pygame.K_1:
                menu_active = False
                game_active = True
                easy_mode = True
            if event.key == pygame.K_2:
                menu_active = False
                game_active = True
                hard_mode = True

        if event.type == pygame.KEYDOWN and ai_won or event.type == pygame.KEYDWON and user_won:
            if event.key == pygame.K_1:
                menu_active = False
                game_active = True
                easy_mode = True
                ai_won = False
                user_won = False
            if event.key == pygame.K_2:
                menu_active = False
                game_active = True
                hard_mode = True
                ai_won = False
                user_won = False
    
    if menu_active:
        menu()
        
    if game_active:
        game()

    clock.tick(60)
    pygame.display.update()

pygame.quit()        