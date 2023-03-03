import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING

class Dinosaur(Sprite):
    
    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = 80
        self.dino_rect.y = 310
        self.frame_index = 0
        self.counter = 0

    def update(self):
        # Incrementar el contador de frames
        self.counter += 1

        # Cambiar la imagen del dinosaurio cada 10 fotogramas
        if self.counter % 10 == 0:
            self.frame_index += 1
            self.frame_index %= len(RUNNING)
            self.image = RUNNING[self.frame_index]

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
