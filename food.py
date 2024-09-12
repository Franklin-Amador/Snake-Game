
import random

def spawn_food(width, height, block_size):
    """Genera una nueva posición para la comida"""
    food_x = round(random.randrange(0, width - block_size) / block_size) * block_size
    food_y = round(random.randrange(0, height - block_size) / block_size) * block_size
    return food_x, food_y

def check_food_collision(x, y, food_x, food_y, block_size):
    """Verifica si la serpiente colisiona con la comida"""
    return (food_x <= x < food_x + block_size or food_x <= x + block_size < food_x + block_size) and \
           (food_y <= y < food_y + block_size or food_y <= y + block_size < food_y + block_size)

