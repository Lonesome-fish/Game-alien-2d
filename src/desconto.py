import abc

class IDesconto(abc.ABC):
    @abc.abstractmethod
    def calcular(self, valor: float) -> float:
        raise NotImplementedError

class DescontoNormal(IDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.1

class DescontoVIP(IDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.2

class DescontoPremium(IDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.3

class Pedido:
    def __init__(self, desconto: IDesconto):
        self.desconto = desconto

    def total(self, valor: float) -> float:
        return valor - self.desconto.calcular(valor)