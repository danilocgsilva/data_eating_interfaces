from abc import ABC, abstractmethod
from typing import Any, Optional, List

class IResourceRepository(ABC):
    
    @abstractmethod
    def create(self, data: Any) -> Any:
        pass
    
    @abstractmethod
    def read(self, id: Any) -> Optional[Any]:
        pass
    
    @abstractmethod
    def update(self, id: Any, data: Any) -> Optional[Any]:
        pass
    
    @abstractmethod
    def delete(self, id: Any) -> bool:
        pass
    
    @abstractmethod
    def list_all(self) -> List[Any]:
        pass
