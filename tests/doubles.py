from src.desconto import IDesconto
from src.settings import Settings


# 1. Stub Didático (do exemplo dos slides)
class StubSemDesconto(IDesconto):
    """Simula um desconto zerado sem executar regras de negócio complexas."""
    def calcular(self, valor: float) -> float:
        return 0.0


# 2. Stub do Jogo Game2D_Alien (Aplicado ao jogo)
class StubSettings(Settings):
    """Simula configurações customizadas para acelerar testes da nave."""
    def __init__(self):
        super().__init__()
        self.ship_speed = 10.0  # Velocidade alterada para verificar movimento rápido no teste
        self.screen_width = 800
        self.screen_height = 600