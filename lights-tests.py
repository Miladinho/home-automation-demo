import unittest
from light import Light
from home import Home
from errors import *

class LightTests(unittest.TestCase):
    def setUp(self):
        self.home = Home()
        newLight = Light("test")
        self.home.add(newLight)

    def test_add_new_light(self):
        self.assertTrue(self.home.isConnected("test"))

    def test_add_existing_light_throws(self):
        light = Light("test")
        self.assertRaises(ComponentAlreadyConnectedError, self.home.add, **{"component": light})
    
    def test_remove_existing_light(self):
        self.assertTrue(len(self.home.data) == 1)
        light = self.home.remove("test")
        self.assertTrue(light.name == "test")
        self.assertTrue(len(self.home.data) == 0)
    
    def test_remove_non_existing_light_throws(self):
        self.home.data.clear()
        self.assertRaises(ComponentNotConnectedError, self.home.remove, **{"componentName": "test"})
    
    def test_turn_light_on(self):
        light = self.home.get("test")
        self.assertEqual(light.status, False) # default status
        light.status = True
        self.home.update(light)
        self.assertEqual(self.home.get("test").status, True)
    
    def test_turn_light_off(self):
        self.home.data.clear()
        self.home.add(Light("test", status=True))
        light = self.home.get("test")
        light.status = False
        self.home.update(light)
        self.assertEqual(self.home.get("test").status, False)
        
if __name__ == '__main__':
    unittest.main()
