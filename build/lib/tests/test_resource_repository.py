import unittest
from data_eating_interfaces.IResourceRepository import IResourceRepository
from data_eating_interfaces.IResource import IResource
from tests.Mocks.mock_resource_repository import MockResourceRepository
from tests.Mocks.mock_resource import MockResource

class TestResourceRepository(unittest.TestCase):
    def setUp(self):
        self.repo = MockResourceRepository()
    
    def test_create_and_read(self):
        resource_id = self.repo.create("test_address")
        resource = self.repo.read(resource_id)
        self.assertIsNotNone(resource)
        self.assertEqual(resource.getAddress(), "test_address")
    
    def test_update(self):
        resource_id = self.repo.create("old_address")
        result = self.repo.update(resource_id, "new_address")
        self.assertTrue(result)
        resource = self.repo.read(resource_id)
        self.assertEqual(resource.getAddress(), "new_address")
    
    def test_delete(self):
        resource_id = self.repo.create("test_address")
        result = self.repo.delete(resource_id)
        self.assertTrue(result)
        self.assertIsNone(self.repo.read(resource_id))
    
    def test_get_all(self):
        self.repo.create("address1")
        self.repo.create("address2")
        resources = self.repo.get_all()
        self.assertEqual(len(resources), 2)

if __name__ == '__main__':
    unittest.main()