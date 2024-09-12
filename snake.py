
import pygame

GREEN = (0, 255, 0)

def draw_snake(window, snake_block, snake_list, snake_img):
    """Dibuja la serpiente en la pantalla usando una imagen"""
    for block in snake_list:
        window.blit(snake_img, (block[0], block[1]))

def check_collision(snake_list):
    """Verifica si la serpiente colisiona consigo misma"""
    snake_head = snake_list[-1]
    for block in snake_list[:-1]:
        if block == snake_head:
            return True
    return False
