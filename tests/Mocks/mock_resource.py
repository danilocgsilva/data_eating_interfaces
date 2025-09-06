from data_eating_interfaces.IResource import IResource

class MockResource(IResource):
    def __init__(self, address: str):
        self._address = address
    
    def getAddress(self) -> str:
        return self._address
    
