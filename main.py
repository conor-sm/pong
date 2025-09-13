import pygame
import sys
import random

pygame.init()

clock = pygame.time.Clock()

running = True
menu_active = True
game_over = False
game_active = False

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
    def __init__(self):

class AI:
    def __init__(self):
        self.text = "Hello World"

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

player = Player()
ai = AI()
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
        player.draw(screen)
        player.update()

    clock.tick(60)
    pygame.display.update()

pygame.quit()        