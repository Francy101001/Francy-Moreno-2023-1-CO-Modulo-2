import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SCREEN_HEIGHT, BIRD

class Bird(Obstacle):
    def __init__(self):
        super().__init__(BIRD, random.randint(0, 1))
        self.rect.y = [SCREEN_HEIGHT * 0.75, SCREEN_HEIGHT * 0.6, SCREEN_HEIGHT * 0.45][self.obstacle_type]
        self.image_index = 0  # Inicializar el índice de imagen en 0
        
    
    