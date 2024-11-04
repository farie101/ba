from abc import ABC, abstractmethod

class Weight_Function(ABC):
    @staticmethod
    @abstractmethod
    def calculate_weight(img, type, G, i, j) -> None:
        pass
