import pygame

class GameRenderer:
    """Gerencia a renderização dos elementos na tela."""

    def __init__(self, screen, bg_color, ship, bullets, aliens):
        self.screen = screen
        self.bg_color = bg_color
        self.ship = ship
        self.bullets = bullets
        self.aliens = aliens

    def _render_screen(self) -> None:
        """Redesenha a tela a cada passagem pelo laço principal."""
        self.screen.fill(self.bg_color)
        
        # Desenha a nave usando o método padronizado .draw()
        self.ship.draw()
        
        # Desenha todos os projéteis ativos
        for bullet in self.bullets.sprites():
            bullet.draw()
            
        # Desenha todos os alienígenas ativos
        for alien in self.aliens.sprites():
            alien.draw()

        pygame.display.flip()