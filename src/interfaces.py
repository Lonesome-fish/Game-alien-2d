from abc import ABC, abstractmethod
import pygame

class IAtualizavel(ABC):
    """Interface para entidades que possuem lógica de atualização."""
    @abstractmethod
    def update(self) -> None:
        pass

class IDesenhavel(ABC):
    """Interface para entidades que podem ser renderizadas na tela."""
    @abstractmethod
    def draw(self) -> None:
        pass