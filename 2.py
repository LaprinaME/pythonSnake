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

# Инициализация окна игры
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Змейка')

# Функция отрисовки текста на экране
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

# Функция стартового экрана
def start_screen():
    while True:
        screen.fill(GRAY)
        draw_text("Нажмите SPACE для начала игры", pygame.font.Font(None, 36), WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return

# Основной игровой цикл
def game_loop():
    # Параметры змейки
    snake = [(200, 200), (210, 200), (220, 200)]
    snake_direction = 'LEFT'

    # Параметры еды
    food = (random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
            random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE)

    # Параметры игры
    score = 0
    game_over = False

    # Главный цикл игры
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake_direction != 'RIGHT':
                    snake_direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and snake_direction != 'LEFT':
                    snake_direction = 'RIGHT'
                elif event.key == pygame.K_UP and snake_direction != 'DOWN':
                    snake_direction = 'UP'
                elif event.key == pygame.K_DOWN and snake_direction != 'UP':
                    snake_direction = 'DOWN'

        # Движение змейки
        head = list(snake[0])
        if snake_direction == 'LEFT':
            head[0] -= BLOCK_SIZE
        elif snake_direction == 'RIGHT':
            head[0] += BLOCK_SIZE
        elif snake_direction == 'UP':
            head[1] -= BLOCK_SIZE
        elif snake_direction == 'DOWN':
            head[1] += BLOCK_SIZE

        # Проверка столкновений змейки с границами экрана
        if head[0] < 0 or head[0] >= SCREEN_WIDTH or head[1] < 0 or head[1] >= SCREEN_HEIGHT:
            game_over = True
            break

        # Проверка столкновений змейки с самой собой
        if head in snake[1:]:
            game_over = True
            break

        # Добавление новой головы змейки
        snake.insert(0, tuple(head))

        # Проверка столкновения змейки с едой
        if snake[0] == food:
            score += 1
            food = (random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
                    random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE)
        else:
            snake.pop()

        # Отрисовка экрана
        screen.fill(GRAY)
        pygame.draw.rect(screen, NEON_YELLOW, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))

        for segment in snake:
            pygame.draw.rect(screen, NEON_GREEN, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))

        # Отображение счета с рамкой
        score_font = pygame.font.Font(None, 36)
        text_surface = score_font.render(f"Счет: {score}", True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (10, 10)
        pygame.draw.rect(screen, RED, (text_rect.left - 5, text_rect.top - 5, text_rect.width + 10, text_rect.height + 10), 2)
        screen.blit(text_surface, text_rect)

        pygame.display.update()
        pygame.time.Clock().tick(10)  # Скорость змейки

    # Показ экрана проигрыша
    screen.fill(GRAY)
    draw_text("Game Over", pygame.font.Font(None, 72), RED, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
    draw_text(f"Ваш счет: {score}", pygame.font.Font(None, 36), WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    draw_text("Нажмите SPACE для рестарта", pygame.font.Font(None, 24), WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT * 3 // 4)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return

# Запуск игры
start_screen()
game_loop()

pygame.quit()
quit()