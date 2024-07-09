import pygame
import random

# Инициализация Pygame
pygame.init()

# Размеры экрана
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# Цвета
GRAY = (50, 50, 50)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
NEON_GREEN = (57, 255, 20)
NEON_YELLOW = (255, 255, 0)

# Размеры змейки и блока еды
BLOCK_SIZE = 20

# Создание экрана
dis = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
snake_speed = 10

font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, NEON_GREEN, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3])

def start_screen():
    while True:
        dis.fill(GRAY)
        draw_text("Press SPACE to start", pygame.font.Font(None, 36), WHITE, dis, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return

def game_over_screen():
    while True:
        dis.fill(GRAY)
        draw_text("Game Over! Press R to Restart or Q to Quit", pygame.font.Font(None, 36), WHITE, dis, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                if event.key == pygame.K_q:
                    return False

def gameLoop():
    game_over = False
    game_close = False

    x1 = SCREEN_WIDTH / 2
    y1 = SCREEN_HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    foody = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    score = 0

    while not game_over:

        while game_close:
            if not game_over_screen():
                game_over = True
                game_close = False
            else:
                gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -BLOCK_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = BLOCK_SIZE
                    x1_change = 0

        if x1 >= SCREEN_WIDTH or x1 < 0 or y1 >= SCREEN_HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(GRAY)
        pygame.draw.rect(dis, RED, [foodx, foody, BLOCK_SIZE, BLOCK_SIZE])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(BLOCK_SIZE, snake_List)
        draw_text(f"Score: {score}", score_font, NEON_YELLOW, dis, 50, 30)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            foody = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            Length_of_snake += 1
            score += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

start_screen()
gameLoop()
