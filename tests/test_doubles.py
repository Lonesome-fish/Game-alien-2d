import pygame
import pytest
from src.desconto import Pedido
from src.ship import Ship
from tests.doubles import StubSemDesconto, StubSettings


# -------------------------------------------------------------
# Testes Didáticos (Exemplo dos Slides)
# -------------------------------------------------------------

def test_pedido_com_stub():
    """Testa a classe Pedido usando o StubSemDesconto."""
    pedido = Pedido(StubSemDesconto())
    assert pedido.total(100) == 100


def test_pedido_com_mock_desconto(mocker):
    """Testa a classe Pedido simulando e verificando chamadas com Mock."""
    mock_desconto = mocker.Mock()
    mock_desconto.calcular.return_value = 10

    pedido = Pedido(mock_desconto)
    resultado = pedido.total(100)

    assert resultado == 90
    mock_desconto.calcular.assert_called()
    mock_desconto.calcular.assert_called_once_with(100)
    assert mock_desconto.calcular.call_count == 1


# -------------------------------------------------------------
# Testes Aplicados ao Jogo Game2D_Alien
# -------------------------------------------------------------

def test_ship_movimento_com_stub_settings():
    """Testa a velocidade de movimento da nave usando o StubSettings do jogo."""
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    stub_settings = StubSettings()

    ship = Ship(screen, stub_settings)
    x_inicial = ship.x

    ship.moving_right = True
    ship.update()

    # Confirma que a nave moveu exatamente a velocidade definida no Stub (10.0)
    assert ship.x == x_inicial + 10.0


def test_ship_draw_chamada_mock(mocker):
    """Testa se o método draw da nave executa blit na tela usando um Mock para a superfície."""
    mock_screen = mocker.Mock()
    # Define que get_rect() retorna um Rect real do Pygame com tamanho 800x600
    mock_screen.get_rect.return_value = pygame.Rect(0, 0, 800, 600)

    stub_settings = StubSettings()

    # Instancia a nave injetando a tela falsa (Mock)
    ship = Ship(mock_screen, stub_settings)
    ship.draw()

    # Verifica se a tela recebeu a ordem de renderizar (blit)
    mock_screen.blit.assert_called_once_with(ship.image, ship.rect)