import unittest
from unittest.mock import Mock, MagicMock
import inMemoryRepository as repo
from light import Light

class InMemoryRepositoryTests(unittest.TestCase):
    def setUp(self):
        self.validJSONFileName = "valid.json"
        self.testComponent = {"name": "test", "type": "Light", "status": 0}
        self.fileService = Mock()

    def test_non_json_file_name_passed_into_constructor_raises(self):
        fileName = "notJSON.txt"
        self.assertRaises(
            repo.JSONFileNameError, 
            repo.InMemoryRepository.__init__, 
            self.fileService,
            **{
                "fileService": Mock(),
                "fileName": fileName
            }
        )

    def test_file_name_less_than_six_chars_raises(self):
        fileName = ".json"
        self.assertRaises(
            repo.JSONFileNameError, 
            repo.InMemoryRepository.__init__, 
            self.fileService,
            **{
                "fileService": Mock(),
                "fileName": fileName
            }
        )

    def test_init_without_components_key_in_json_raises(self):
        jsonObject = {"name": {}}
        self.fileService.getComponents = MagicMock(return_value=jsonObject)
        memoryRepo = repo.InMemoryRepository(self.fileService, self.validJSONFileName)
        self.assertRaises(
            repo.BadHomeDataFileFormatError, 
            memoryRepo.initFromDataFile, 
            **{}
        )

    def test_duplicate_component_name_in_json_file_raises(self):
        jsonObject = {"components": [self.testComponent, self.testComponent]}
        self.fileService.getComponents = MagicMock(return_value=jsonObject)
        memoryRepo = repo.InMemoryRepository(self.fileService, self.validJSONFileName)
        self.assertRaises(
            repo.BadHomeDataFileFormatError, 
            memoryRepo.initFromDataFile, 
            **{}
        )      

    def test_add_method_writes_changes_to_file(self):
        self.fileService.writeComponentsToFile()
        memoryRepo = repo.InMemoryRepository(self.fileService, self.validJSONFileName)
        memoryRepo.add(Light("test"))
        self.fileService.writeComponentsToFile.assert_called()
    
    def test_remove_method_writes_changes_to_file(self):
        self.fileService.writeComponentsToFile()
        memoryRepo = repo.InMemoryRepository(self.fileService, self.validJSONFileName)
        memoryRepo.add(Light("test"))
        self.fileService.writeComponentsToFile.assert_called()

    def test_update_method_writes_changes_to_file(self):
        self.fileService.writeComponentsToFile()
        memoryRepo = repo.InMemoryRepository(self.fileService, self.validJSONFileName)
        memoryRepo.add(Light("test"))
        self.fileService.writeComponentsToFile.assert_called()

if __name__ == '__main__':
    unittest.main()
