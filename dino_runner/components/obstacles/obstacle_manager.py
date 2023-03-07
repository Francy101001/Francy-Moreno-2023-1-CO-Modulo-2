import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.bird = Bird()

    def update(self, game):
        if len(self.obstacles) == 0:
            obstacle_type = random.choices([SMALL_CACTUS, LARGE_CACTUS, BIRD], weights=[0.5, 0.5, 0.25])[0]
            if obstacle_type == BIRD:
                obstacle = self.bird
            else:
                obstacle = Cactus(obstacle_type)
            self.obstacles.append(obstacle)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(100)
                #game.playing = False
                #break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
