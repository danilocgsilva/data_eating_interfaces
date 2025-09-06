from data_eating_interfaces.IResourceRepository import IResourceRepository
from tests.Mocks.mock_resource import MockResource

class MockResourceRepository(IResourceRepository):
    def __init__(self):
        self._resources = {}
        self._next_id = 1
    
    def create(self, data):
        resource_id = self._next_id
        self._resources[resource_id] = MockResource(data)
        self._next_id += 1
        return resource_id
    
    def read(self, id: int):
        return self._resources.get(id)
    
    def update(self, id: int, data) -> bool:
        if id in self._resources:
            self._resources[id] = MockResource(data)
            return True
        return False
    
    def delete(self, id: int) -> bool:
        return self._resources.pop(id, None) is not None
    
    def get_all(self):
        return list(self._resources.values())