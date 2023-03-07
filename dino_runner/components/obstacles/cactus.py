import random
from dino_runner.components.obstacles.obstacle import Obstacle

class Cactus(Obstacle):
    def __init__(self, image):
        if random.randint(0, 1):
            self.type = random.randint(0, 2)
        else:
            self.type = random.randint(3, 5)
        super().__init__(image, self.type)
        self.rect.y = 325
        