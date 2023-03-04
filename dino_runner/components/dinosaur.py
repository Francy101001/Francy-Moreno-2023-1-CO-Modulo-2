import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING

class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    JUMP_SPEED = 8.5
    
    def __init__(self):
        super().__init__()
        self.image = RUNNING[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.jump_speed = self.JUMP_SPEED

    def update(self, user_input):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        
        if user_input[pygame.K_SPACE] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
        elif not self.dino_jump:
            self.dino_jump = False
            self.dino_run = True

        if self.step_index >= 10:
            self.step_index = 0

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.step_index += 1
    
    def jump(self):
        self.image = JUMPING
        self.rect.y -= int(self.jump_speed * 4)
        self.jump_speed -= 0.8

        if self.jump_speed < -self.JUMP_SPEED:
            self.rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_speed = self.JUMP_SPEED

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
