from abc import ABC, abstractmethod
from typing import Any, Optional, List
from ..Models.IResource import IResource
from ..IRepository import IRepository

class IResourceRepository(IRepository):
    @abstractmethod
    def create(self, data: Any) -> Any:
        pass
    
    @abstractmethod
    def read(self, id: int) -> Optional[IResource]:
        pass
    
    @abstractmethod
    def update(self, id: int, data: Any) -> bool:
        pass
    
    @abstractmethod
    def delete(self, id: int) -> bool:
        pass
    
    @abstractmethod
    def get_all(self) -> List[IResource]:
        pass
