import pygame
import random

from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import HAMMER, HAMMER_TYPE


class Hammer(PowerUp):
    HAMMER_TYPE = 'hammer'
    image = HAMMER

    def __init__(self):
        super().__init__(HAMMER, HAMMER_TYPE)
        self.hammer_rect = self.image.get_rect()
        self.hammer_rect.x = random.randint(50, 700)
        self.hammer_rect.y = 300
        self.throw_time = 0
        self.is_active = False

    def throw_hammer(self):
        """Fijar el tiempo de lanzamiento al lanzar el martillo"""
        self.throw_time = pygame.time.get_ticks()
        self.is_active = True  # Activamos el martillo al lanzarlo

    def update(self, game_speed, power_ups):
        super().update(game_speed, power_ups)
        if self.throw_time != 0 and pygame.time.get_ticks() - self.throw_time > 1000:
            self.is_active = False

    def draw(self, screen):
        if self.is_active and not self.is_started:
            screen.blit(self.image, self.hammer_rect)
