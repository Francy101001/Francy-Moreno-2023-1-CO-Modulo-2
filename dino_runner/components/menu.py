import pygame
from dino_runner.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

class Menu:
    half_screen_height = SCREEN_HEIGHT // 2
    half_screen_width = SCREEN_WIDTH // 2

    def __init__(self, message, screen):
        screen.fill((255, 255, 255))
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.half_screen_width, self.half_screen_height)
        

        # Agregamos nuevas variables miembro para las puntuaciones
        self.score_font = pygame.font.Font(FONT_STYLE, 20)
        self.score_text_rect = pygame.Rect(10, 10, 100, 30)
        self.highest_score_text_rect = pygame.Rect(120, 10, 150, 30)
        self.total_deaths_text_rect = pygame.Rect(300, 10, 150, 30)

    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game)

        # Funciones para mostrar las puntuaciones en la pantalla
    def display_score(self, score, screen):
        score_text = self.score_font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, self.score_text_rect)

    def display_highest_score(self, highest_score, screen):
        highest_score_text = self.score_font.render(f"Highest Score: {highest_score}", True, (0, 0, 0))
        screen.blit(highest_score_text, self.highest_score_text_rect)

    def display_total_deaths(self, total_deaths, screen):
        deaths_text = self.score_font.render(f"Total Deaths: {total_deaths}", True, (0, 0, 0))
        screen.blit(deaths_text, self.total_deaths_text_rect)

    def draw(self, screen, score=0, highest_score=0, total_deaths=0):
        screen.blit(self.text, self.text_rect)
        
        
    def reset_screen_color(self, screen):
        screen.fill((255, 255, 255))

    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                game.playing = False
            elif event.type == pygame.KEYDOWN:
                game.run()

    def update_message(self, message):
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.half_screen_width, self.half_screen_height)

    
