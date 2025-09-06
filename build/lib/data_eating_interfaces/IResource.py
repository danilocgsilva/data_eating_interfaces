from abc import ABC, abstractmethod

class IResource(ABC):
    @abstractmethod
    def getAddress(self) -> str:
        pass
