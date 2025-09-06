from abc import ABC, abstractmethod
from ..IModel import IModel

class IResource(IModel):
    @abstractmethod
    def getAddress(self) -> str:
        pass
