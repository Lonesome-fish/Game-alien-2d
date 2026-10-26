import pygame
from pygame.sprite import Sprite
from src.interfaces import IAtualizavel, IDesenhavel
from settings import Settings

class Alien(Sprite, IAtualizavel, IDesenhavel):
    """Gerencia os alienígenas."""

    def __init__(self, screen: pygame.Surface, settings: Settings):
        super().__init__()
        self.screen = screen
        self.settings = settings
        
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        
    def draw(self) -> None:
        """Desenha o alienígena em sua posição atual."""
        self.screen.blit(self.image, self.rect)
        
    def update(self) -> None:
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = int(self.x)
        
    def check_edges(self) -> bool:
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0