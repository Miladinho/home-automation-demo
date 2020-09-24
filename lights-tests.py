import unittest
from light import Light
from home import Home
from errors import *

class LightTests(unittest.TestCase):
    def setUp(self):
        self.home = Home()

    def test_add_new_light(self):
        newLight = Light("test")
        self.home.add(newLight)
        self.assertTrue(self.home.isConnected(newLight.name))

    def test_add_existing_light_throws(self):
        light = Light("test")
        self.home.add(light)
        self.assertRaises(Exception, self.home.add, **{"component": light})
    
    def test_remove_existing_light(self):
        light = Light("test")
        self.home.add(light)
        self.assertTrue(len(self.home.data) == 1)
        self.assertTrue(self.home.remove(light.name) == light)
        self.assertTrue(len(self.home.data) == 0)
    
    def test_remove_non_existing_light_throws(self):
        self.assertRaises(ComponentDoesNotExistError, self.home.remove, **{"componentName": "test"})
        
if __name__ == '__main__':
    unittest.main()
