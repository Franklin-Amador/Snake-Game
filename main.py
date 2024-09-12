
import pygame
import time
import random
from snake import check_collision
from food import spawn_food, check_food_collision

# Inicializar Pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)

# Dimensiones de la ventana
WIDTH, HEIGHT = 600, 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Configuración del reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

# Tamaño de la serpiente y velocidad inicial
snake_block = 20
initial_speed = 10

# Fuente para el texto
font_style = pygame.font.SysFont("bahnschrift", 25)

# Cargar la imagen de la serpiente (snake.png)
snake_img = pygame.image.load('snake.png')
snake_img = pygame.transform.scale(snake_img, (snake_block, snake_block))  # Redimensionar la imagen de la serpiente

# Cargar la imagen de la comida (apple.png) y la comida especial (cat.jpg)
food_img = pygame.image.load('apple.png')
food_img = pygame.transform.scale(food_img, (snake_block, snake_block))  # Redimensionar la imagen de la comida

special_food_img = pygame.image.load('cat.jpg')
special_food_img = pygame.transform.scale(special_food_img, (snake_block * 2, snake_block * 2))  # Redimensionar la imagen de la comida especial

def display_score(score):
    """Muestra el puntaje en la pantalla"""
    value = font_style.render(f"Score: {score}", True, WHITE)
    window.blit(value, [0, 0])

def message(msg, color):
    """Muestra un mensaje en la pantalla"""
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [WIDTH / 6, HEIGHT / 3])

def draw_snake_with_image(window, snake_block, snake_list, snake_img):
    """Dibuja la serpiente usando la imagen snake.png"""
    for x, y in snake_list:
        window.blit(snake_img, (x, y))

def draw_food_with_image(window, food_x, food_y, food_img):
    """Dibuja la comida usando la imagen apple.png"""
    window.blit(food_img, (food_x, food_y))

def draw_special_food_with_image(window, special_food_x, special_food_y, special_food_img):
    """Dibuja la comida especial usando la imagen cat.jpg"""
    window.blit(special_food_img, (special_food_x, special_food_y))

def game_loop():
    """Lógica principal del juego"""
    game_over = False
    game_close = False

    # Posición inicial de la serpiente
    x, y = WIDTH / 2, HEIGHT / 2
    x_change, y_change = 0, 0

    snake_list = []
    length_of_snake = 1

    # Posición de la comida
    food_x, food_y = spawn_food(WIDTH, HEIGHT, snake_block)
    special_food = False
    special_food_x, special_food_y = None, None

    score = 0
    snake_speed = initial_speed

    while not game_over:
        while game_close:
            window.fill(BLACK)
            message("Game Over! Press Q-Quit or C-Play Again", RED)
            display_score(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change, y_change = -snake_block, 0
                elif event.key == pygame.K_RIGHT:
                    x_change, y_change = snake_block, 0
                elif event.key == pygame.K_UP:
                    y_change, x_change = -snake_block, 0
                elif event.key == pygame.K_DOWN:
                    y_change, x_change = snake_block, 0

        # Teletransportar al otro lado si la serpiente llega al borde
        if x >= WIDTH:
            x = 0
        elif x < 0:
            x = WIDTH - snake_block
        if y >= HEIGHT:
            y = 0
        elif y < 0:
            y = HEIGHT - snake_block

        x += x_change
        y += y_change
        window.fill(BLACK)

        # Dibujar la comida usando la imagen apple.png
        draw_food_with_image(window, food_x, food_y, food_img)

        # Comida especial cada 15 puntos
        if score > 0 and score % 15 == 0 and not special_food:
            special_food_x, special_food_y = spawn_food(WIDTH, HEIGHT, snake_block * 2)
            special_food = True

        # Dibujar la comida especial si está activa
        if special_food:
            draw_special_food_with_image(window, special_food_x, special_food_y, special_food_img)

        # Actualizar la serpiente
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        if check_collision(snake_list):
            game_close = True

        # Dibujar la serpiente con la imagen cargada
        draw_snake_with_image(window, snake_block, snake_list, snake_img)
        display_score(score)

        # Comprobar colisión con la comida normal
        if check_food_collision(x, y, food_x, food_y, snake_block):
            food_x, food_y = spawn_food(WIDTH, HEIGHT, snake_block)
            length_of_snake += 1
            score += 1
            snake_speed += 1

        # Comprobar colisión con la comida especial
        if special_food and check_food_collision(x, y, special_food_x, special_food_y, snake_block * 2):
            special_food = False
            length_of_snake += 5  # Incremento mayor por comida especial
            score += 5
            snake_speed += 2

        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
    quit()

if __name__ == '__main__':
    game_loop()
