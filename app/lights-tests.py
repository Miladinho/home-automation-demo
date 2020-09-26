import unittest
from light import Light
from home import Home
from errors import *
from inMemoryRepository import InMemoryRepository

class LightTests(unittest.TestCase):
    def setUp(self):
        '''
            Given current specs, the JSON file of device data is loaded into memory
            Therefore, instead of creating a mocks and stubs for testing,
            we can just develop the in-momory implementation of the data repository
            as a testing fake object. The benefit is because it is simple CRUD code
            we create the actual repository implementation. A side-effect of this is
            that the test code here will possibly be brittle.
        '''
        self.home = Home(InMemoryRepository())
        self.home.addLight("test")

    def test_add_new_light(self):
        self.home.addLight("test2")
        self.assertTrue(self.home.isConnected("test2"))

    def test_add_existing_light_throws(self):
        self.assertRaises(ComponentAlreadyConnectedError, self.home.addLight, **{"name": "test"})
    
    def test_remove_existing_light(self):
        self.assertTrue(self.home.isConnected("test"))
        light = self.home.removeLight("test")
        self.assertEqual(light, "test")
        self.assertFalse(self.home.isConnected("test"))
    
    def test_remove_non_existing_light_throws(self):
        self.assertRaises(ComponentNotConnectedError, self.home.removeLight, **{"name": "test2"})
    
    def test_read_light_status(self):
        self.assertEqual(self.home.getLightStatus("test"), 0)

    def test_set_light_status_on_and_off(self):
        self.assertEqual(self.home.getLightStatus("test"), 0)
        self.home.setLightStatus("test", 1)
        self.assertEqual(self.home.getLightStatus("test"), 1)
        self.home.setLightStatus("test", 0)
        self.assertEqual(self.home.getLightStatus("test"), 0)

    def test_turn_set_light_status_throws_when_light_not_connected(self):
        self.assertRaises(ComponentNotConnectedError, self.home.setLightStatus,**{"name": "bad light", "value": 1})
        
if __name__ == '__main__':
    unittest.main()
