import pygame
from pygame.sprite import Sprite
from src.interfaces import IAtualizavel, IDesenhavel
from settings import Settings
from ship import Ship

class Bullet(Sprite, IAtualizavel, IDesenhavel):
    """Gerencia os projéteis disparados pela nave."""

    def __init__(self, screen: pygame.Surface, settings: Settings, ship: Ship):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.ship = ship
        self.color = self.settings.bullet_color
        
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = self.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self) -> None:
        """Move o projétil para cima na tela."""
        self.y -= self.settings.bullet_speed
        self.rect.y = int(self.y)

    def draw(self) -> None:
        """Desenha o projétil na tela."""
        pygame.draw.rect(self.screen, self.color, self.rect)